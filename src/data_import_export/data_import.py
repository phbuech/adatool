import os
import numpy as np
import xarray as xr

import scipy as sp
import chardet
import pandas as pd

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
                tmp_data.annotation = read_TextGrid(main_path + fname + "." + suffixes[suffix_idx])
    
        file_dict[fname] = tmp_data
    
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

    df = pd.DataFrame(columns=["tierName","tmin","tmax","label"])
    for i in range(7,len(annotation_file)):
        if "    item [" in annotation_file[i]:
            tier_name = annotation_file[i+2].replace("name","").replace("\n","").replace("=","").replace(" ","").replace("\"","")
        if "        intervals [" in annotation_file[i]:
            segment_info = pd.Series(index=df.columns)
            segment_info["tierName"] = tier_name
            segment_info["tmin"] = float(annotation_file[i+1].replace("xmin","").replace("=","").replace(" ","").replace("\n",""))
            segment_info["tmax"] = float(annotation_file[i+2].replace("xmax","").replace("=","").replace(" ","").replace("\n",""))
            segment_info["label"] = annotation_file[i+3].replace("text","").replace("=","").replace(" ","").replace("\"","").replace("\n","")
            df.loc[len(df)] = segment_info

    return df