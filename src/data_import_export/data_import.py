import os
import numpy as np
import xarray as xr

import scipy as sp
import chardet

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

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

def read_data(file_urls,file_dict):
    #get main path:
    main_path = "/".join(file_urls[0][0].toLocalFile().split("/")[:-1]) + "/"
    #get file names
    files = [file_urls[0][i].toLocalFile().split("/")[-1] for i in range(len(file_urls[0]))]
    #extract filenames and suffixes
    files = np.array([files[i].split(".") for i in range(len(files))])
    fnames = np.unique(files[:,0])
    suffixes = np.unique(files[:,1])
    progress = QProgressDialog("loading files...","abort loading",0,len(fnames))
    for fname_idx in range(len(fnames)):
        fname = fnames[fname_idx]
        tmp_data = dataContainer()
        for suffix_idx in range(len(suffixes)):
            if suffixes[suffix_idx] == "pos":
                try:
                    tmp_data.ema = read_AG50x(main_path + fname + "."+suffixes[suffix_idx])
                except:
                    tmp_data.ema = None
            if suffixes[suffix_idx] in ["wav","WAV"]:
                try:
                    tmp_data.audio = read_wav(main_path + fname + "." + suffixes[suffix_idx])
                except:
                    tmp_data.audio = None
            if suffixes[suffix_idx] in ["TextGrid"]:
                tmp_dict = {
                        "audio": None,
                        "ema" : None
                    }
                try:
                    tmp_dict["audio"] = read_TextGrid(main_path + fname + "." + suffixes[suffix_idx])
                except:
                    pass
                tmp_data.annotation = tmp_dict
            progress.setValue(fname_idx)
            if progress.wasCanceled():
                break
    
        file_dict[fname] = tmp_data
    progress.setValue(len(fnames))
    
    return file_dict



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




def read_TextGrid(path_to_TextGrid):

    #check for encoding
    rawdata = open(path_to_TextGrid,"rb").read()
    result = chardet.detect(rawdata)
    enc = result["encoding"]

    annotation_file = list(open(path_to_TextGrid,"r",encoding=enc))

    fname = path_to_TextGrid.split("/")[-1].split(".")[0]

    tg = {
            "filename" : fname,
            "tmin" : float(annotation_file[3].replace("xmin = ","").replace(" ","").replace("\n","")),
            "tmax" : float(annotation_file[4].replace("xmax = ","").replace(" ","").replace("\n","")),
            "number_of_tiers": int(annotation_file[6].replace("size = ","").replace(" ","").replace("\n","")),
            "tiers" : {}
        }

    tier_counter = 0
    for i in range(7,len(annotation_file)):
        if "    item [" in annotation_file[i]:
            tmp_tier = {
                        "tier_name" : annotation_file[i+2].replace("name","").replace("\n","").replace("=","").replace(" ","").replace("\"",""),
                        "tmin" : float(annotation_file[i+3].replace("xmin","").replace("\n","").replace("=","").replace(" ","")),
                        "tmax" : float(annotation_file[i+4].replace("xmax","").replace("\n","").replace("=","").replace(" ",""))
                        }
            segment_counter = 0
            tmp_intervals = {}
            tg["tiers"][tier_counter] = tmp_tier
            tier_counter += 1
        elif i == len(annotation_file)-1:
            tg["tiers"][tier_counter] = tmp_tier

        elif "        intervals [" in annotation_file[i]:
            if len(tmp_intervals) != 0:
                tmp_tier["intervals"] = tmp_intervals

            tmp_segment = {
                    "tmin" : float(annotation_file[i+1].replace("xmin","").replace("=","").replace(" ","").replace("\n","")),
                    "tmax" : float(annotation_file[i+2].replace("xmax","").replace("=","").replace(" ","").replace("\n","")),
                    "label" : annotation_file[i+3].replace("text","").replace("=","").replace(" ","").replace("\"","").replace("\n","")
                }
            tmp_intervals[segment_counter] = tmp_segment
            segment_counter += 1

    return tg