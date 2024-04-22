import os
import numpy as np
import xarray as xr

import scipy as sp
import chardet
import pandas as pd
import librosa

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class dataContainer:
    """
        class for the data. Consists of 
        filename (string)
        ema data (xarray)
        audio data (xarray)
        annotation (dictionary)
    """
    def __init__(self,filename=None,ema=None,audio=None,annotation=None):
        self.filename = filename
        self.ema = ema
        self.audio = audio
        self.annotation = annotation

def read_data(file_urls,ema_format,audio_format,annotation_format,slash):
    file_dict = {}
    #get main path:
    main_path = slash.join(file_urls[0][0].toLocalFile().replace("/",slash).split(slash)[:-1]) + slash
    #get file names
    files = [file_urls[0][i].toLocalFile().replace("/",slash).split(slash)[-1] for i in range(len(file_urls[0]))]
    #extract filenames and suffixes
    files = np.array([files[i].split(".") for i in range(len(files))])
    fnames = np.unique(files[:,0])
    suffixes = np.unique(files[:,1])

    #create progres dialog
    progressDialog = QProgressDialog("loading files",None,0,len(files))
    progressDialog.setWindowTitle("Loading files...")
    progressDialog.setWindowModality(Qt.WindowModal)
    progressDialog.setMaximum(len(files))
    progressDialog.setValue(0)
    progressDialog.setMinimumDuration(0)
    progressDialog.show()
    for fname_idx in range(len(fnames)):
        fname = fnames[fname_idx]
        tmp_data = dataContainer()
        if ema_format == "AG50x":
            try:
                tmp_data.ema = read_AG50x(main_path + fname + ".pos")
            except:
                tmp_data.ema = None
        elif ema_format == "netcdf":
            try:
                tmp_data.ema = read_netcdf(main_path + fname + ".nc")
            except:
                tmp_data.ema = None
        if audio_format == "wav":
            try:
                tmp_data.audio = read_wav(main_path + fname + ".wav")
            except:
                tmp_data.audio = None
        elif audio_format == "mp3" :
            try:
                tmp_data.audio = read_mp3_ogg(main_path + fname + ".mp3")
            except:
                tmp_data.audio = None
        elif audio_format == "ogg" :
            try:
                tmp_data.audio = read_mp3_ogg(main_path + fname + ".ogg")
            except:
                tmp_data.audio = None
        if annotation_format == "TextGrid":
            try:
                tmp_data.annotation = read_TextGrid(main_path + fname + ".TextGrid")
            except:
                tmp_data.annotation = None
        elif annotation_format == "json":
            try:
                tmp_data.annotation = read_json(main_path + fname + ".json")
            except:
                tmp_data.annotation = None
        elif annotation_format == "csv":
            try:
                tmp_data.annotation = read_csv(main_path + fname + ".csv")
            except:
                tmp_data.annotation = None
        
        progressDialog.setValue(fname_idx)
        file_dict[fname] = tmp_data
    return file_dict

def read_netcdf(path_to_nc_file):
    nc_file = xr.open_dataset(path_to_nc_file)
    return nc_file

def read_AG50x(path_to_pos_file):
    dims = ["x","z","y","phi","theta","rms","extra"]
    channel_sample_size = {
        8 : 56,
        16 : 112,
        32 : 256
        }
    #read file
    pos_file = open(path_to_pos_file,mode="rb")
    file_content = pos_file.read()
    #read header
    pos_file.seek(0)
    pos_file.readline()
    #extract header
    header_size = int(pos_file.readline().decode("utf8"))
    header_section = file_content[0:header_size]
    header = header_section.decode("utf8").split("\n")
    #extract file information (number of channels, ema samplerate)
    num_of_channels = int(header[2].split("=")[1])
    ema_samplerate = int(header[3].split("=")[1])
    #read data
    data = file_content[header_size:]
    data = np.frombuffer(data,np.float32)
    data = np.reshape(data,newshape=(-1,channel_sample_size[num_of_channels]))
    pos = data.reshape(len(data),-1,7) # reshape to [sample, channel, values]
    time = np.linspace(0,pos.shape[0]/ema_samplerate,pos.shape[0])
    ema_data = xr.Dataset(
                            data_vars=dict(
                                            ema=(["time","channels","dimensions"],pos)
                                        ),
                            coords=dict(
                                        time=(["time"],time),
                                        channels=(["channels"],np.arange(pos.shape[1])),
                                        dimensions=(["dimensions"],dims)
                                        ),
                            attrs=dict(
                                        device="AG50x",
                                        duration=time[-1],
                                        samplerate=ema_samplerate

                            )

                        )
    return ema_data

def read_mp3_ogg(path_to_file):
    signal, fs = librosa.load(path_to_file)
    time = np.linspace(0,len(signal)/fs,len(signal))
    audio = xr.Dataset(
                        data_vars=dict(signal=(["time"],signal)),
                        coords=dict(time=(["time"],time)),
                        attrs=dict(
                                    duration=time[-1],
                                    samplerate=fs
                                )
                    )
    return audio

def read_wav(path_to_wav_file):
    fs, signal = sp.io.wavfile.read(path_to_wav_file)
    time = np.linspace(0,len(signal)/fs,len(signal))
    signal = signal/np.max(np.abs(signal))
    audio = xr.Dataset(
                        data_vars=dict(signal=(["time"],signal)),
                        coords=dict(time=(["time"],time)),
                        attrs=dict(
                                    duration=time[-1],
                                    samplerate=fs
                                )
                    )
    return audio

def read_csv(path_to_csv_file):
    df = pd.read_csv(path_to_csv_file,sep=",",encoding="utf8")
    return df

def read_json(path_to_json_file):
    file = open(path_to_json_file,mode="r",encoding="utf8")
    data = json.load(file)
    df = pd.DataFrame(columns=["tierName","tmin","tmax","label"])
    tier_keys = list(data.keys())
    for i in range(len(tier_keys)):
        segments = data[tier_keys[i]]
        for j in range(len(segments)):
            line = pd.Series(index=df.columns)
            line["tierName"] = tier_keys[i]
            line["tmin"] = segments[str(j)]["tmin"]
            line["tmax"] = segments[str(j)]["tmax"]
            line["label"] =segments[str(j)]["label"]
            df.loc[len(df)] = line

    return df


def read_TextGrid(path_to_TextGrid):

    #check for encoding
    rawdata = open(path_to_TextGrid,"rb").read()
    result = chardet.detect(rawdata)
    enc = result["encoding"]

    annotation_file = list(open(path_to_TextGrid,"r",encoding=enc))

    df = pd.DataFrame(columns=["tierName","tmin","tmax","label"])
    tier_class = "IntervalTier"
    for i in range(7,len(annotation_file)):
        if "    item [" in annotation_file[i]:
            tier_name = annotation_file[i+2].replace("name","").replace("\n","").replace("=","").replace(" ","").replace("\"","")
            tier_class = annotation_file[i+1].replace("class = \"","").replace("\n","").replace("\"","").replace(" ","")
        if tier_class == "IntervalTier":
            if "        intervals [" in annotation_file[i]:
                segment_info = pd.Series(index=df.columns)
                segment_info["tierName"] = tier_name
                segment_info["tmin"] = float(annotation_file[i+1].replace("xmin","").replace("=","").replace(" ","").replace("\n",""))
                segment_info["tmax"] = float(annotation_file[i+2].replace("xmax","").replace("=","").replace(" ","").replace("\n",""))
                segment_info["label"] = annotation_file[i+3].replace("text","").replace("=","").replace(" ","").replace("\"","").replace("\n","")
                df.loc[len(df)] = segment_info
        elif tier_class == "TextTier":
            if "        points [" in annotation_file[i]:
                segment_info = pd.Series(index=df.columns)
                segment_info["tierName"] = tier_name
                segment_info["tmin"] = float(annotation_file[i+1].replace("number","").replace("=","").replace(" ","").replace("\n",""))
                segment_info["tmax"] = float(annotation_file[i+1].replace("number","").replace("=","").replace(" ","").replace("\n",""))
                segment_info["label"] = annotation_file[i+2].replace("mark","").replace("=","").replace(" ","").replace("\"","").replace("\n","")
                df.loc[len(df)] = segment_info
    return df