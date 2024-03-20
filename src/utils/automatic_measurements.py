import os
import sys
import numpy as np
import xarray as xr

from scipy.io import wavfile
import chardet
import pyqtgraph as pg
from scipy import signal

import pandas as pd

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#add gui folder to sys.path
absolute_path = os.path.dirname(__file__)
#print(absolute_path)
main_path = "/".join(absolute_path.split("/")[:-2])
#print(main_path)
sys.path.insert(1,main_path+ "/gui/python_files")
sys.path.insert(1,main_path+"/src/data_import_export")
sys.path.insert(1,main_path+"/src/utils")

#load internal modules
import signal_processing as sp



def automatic_measurements(files,target_info,channel_dict,pbar,landmark_info,measurements_info):
    print("target_info",target_info,"landmark_info:",landmark_info,"measurements:",measurements_info)
    if measurements_info["TYPE"] == "trajectories":
        columns = ["Filename","TargetID","TokenID","Label","Start[s]","Time","Timestep_global","Timestep_local"]
        tmp_channels_dimensions = []
        for i in range(len(measurements_info["measurements"])):
            target_index = measurements_info["measurements"][i]["target"]
            tmp = target_info[target_index]
            for j in range(len(tmp)):
                channel = tmp[j]["channel"]
                dimension = tmp[j]["dimension"]
                colname = channel + dimension
                if colname not in columns:
                    columns.append(colname)
        df = pd.DataFrame(columns=columns)
    
    token_number = 0
    fnames = list(files.keys())
    measurements_parts = measurements_info["measurements"]
    for fname in fnames:
        tiername = target_info[1][0]["tier"]
        annotation = files[fname].annotation
        segment_annotation = annotation[annotation["tierName"] == tiername].reset_index(drop=True)
        for annotation_segment_index in range(len(segment_annotation)):
            for measurements_index in range(len(measurements_parts)):
                target_index = measurements_parts[measurements_index]["target"]
                stepsize = measurements_parts[measurements_index]["stepsize"]
                range_parameter = measurements_parts[measurements_index]["range"]
                number_of_segments = len(target_info[target_index])
                target_labels = np.array([target_info[target_index][i]["label"] for i in range(number_of_segments)])
                current_annotation_labels = segment_annotation["label"][annotation_segment_index:annotation_segment_index+len(target_labels)].to_numpy()
                if np.array_equal(target_labels,current_annotation_labels):
                    token_number += 1
                    timestep_global = 0
                    for tmp_segment_idx in range(len(target_labels)):
                        target_channel = target_info[target_index][tmp_segment_idx]["channel"]
                        target_dimension = target_info[target_index][tmp_segment_idx]["dimension"]
                        target_parameter = target_info[target_index][tmp_segment_idx]["parameter"]
                        signal, _ = sp.get_signal(data=files[fname].ema,
                                               channel_dict=channel_dict,
                                               target_channel=target_channel,
                                               target_dimension=target_dimension,
                                               target_parameter=target_parameter)

                        if range_parameter == "tmin - tmax":
                            tmin = segment_annotation["tmin"][annotation_segment_index+tmp_segment_idx]
                            tmax = segment_annotation["tmax"][annotation_segment_index+tmp_segment_idx]
                            step_interval = np.abs(tmin - tmax)/stepsize
                            maximum_steps = stepsize
                            if tmp_segment_idx == len(target_labels)-1:
                                maximum_steps = stepsize + 1
                            for step_idx in range(maximum_steps):
                                step_time = tmin + step_idx*step_interval
                                values = pd.Series(index=df.columns)
                                values["Filename"] = fname
                                values["TargetID"] = target_index
                                values["TokenID"] = token_number
                                values["Timestep_global"] = timestep_global
                                values["Timestep_local"] = step_idx
                                values["Label"] = segment_annotation["label"][annotation_segment_index+tmp_segment_idx]
                                values["Start[s]"] = tmin
                                time_idx = np.abs(step_time - files[fname].ema.time.values).argmin()
                                col = target_channel+target_dimension
                                values[col] = signal[time_idx]
                                timestep_global += 1
                                df.loc[len(df)] = values

    return df

                                
                    
                
        

