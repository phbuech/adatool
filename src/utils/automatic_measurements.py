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
        columns = ["Filename","TargetID","TokenID","Label","Start[s]","Time","Timestep_global","Timestep_local","Time_index"]
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
    elif measurements_info["TYPE"] == "mass-spring parameters":
        columns = ["Filename","TargetID","TokenID","Label","Start[s]"]
        #collect labels
        for i in range(len(measurements_info["measurements"])):
            colname = measurements_info["measurements"][i]["target"] + "_" +  measurements_info["measurements"][i]["landmark"] + "_" + measurements_info["measurements"][i]["parameter"]
            print(colname)
            if colname not in columns:
                columns.append(colname)
        df = pd.DataFrame(columns=columns)
        print(df)
    
    token_number = 0
    fnames = list(files.keys())
    measurements_parts = measurements_info["measurements"]
    counter = 0
    for fname in fnames:
        tiername = target_info[1][0]["tier"]
        annotation = files[fname].annotation
        segment_annotation = annotation[annotation["tierName"] == tiername].reset_index(drop=True)
        for annotation_segment_index in range(len(segment_annotation)):
            for measurements_index in range(len(measurements_parts)):
                if measurements_info["TYPE"] == "trajectories":
                    target_index = measurements_parts[measurements_index]["target"]
                    number_of_segments = len(target_info[target_index])
                    target_labels = np.array([target_info[target_index][i]["label"] for i in range(number_of_segments)])
                    current_annotation_labels = segment_annotation["label"][annotation_segment_index:annotation_segment_index+len(target_labels)].to_numpy()
                    if np.array_equal(target_labels,current_annotation_labels):
                        token_number += 1
                    
                        stepsize = measurements_parts[measurements_index]["stepsize"]
                        range_parameter = measurements_parts[measurements_index]["range"]
                        timestep_global = 0
                        signals = []
                        target_channels = []
                        target_dimensions = []
                        for tmp_segment_idx in range(len(target_labels)):
                            target_channel = target_info[target_index][tmp_segment_idx]["channel"]
                            target_dimension = target_info[target_index][tmp_segment_idx]["dimension"]
                            target_parameter = target_info[target_index][tmp_segment_idx]["parameter"]
                            signal, _ = sp.get_signal(data=files[fname].ema,
                                                channel_dict=channel_dict,
                                                target_channel=target_channel,
                                                target_dimension=target_dimension,
                                                target_parameter=target_parameter)
                            target_channels.append(target_channel)
                            target_dimensions.append(target_dimension)
                            signals.append(signal)

                        for tmp_segment_idx in range(len(target_labels)):
                            #in case of segment time range
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
                                    values["Time_index"] = step_time
                                    values["Label"] = segment_annotation["label"][annotation_segment_index+tmp_segment_idx]
                                    values["Start[s]"] = tmin
                                    time_idx = np.abs(step_time - files[fname].ema.time.values).argmin()
                                    for ii in range(len(signals)):
                                        col = target_channels[ii]+target_dimensions[ii]
                                        values[col] = signals[ii][time_idx]
                                    timestep_global += 1
                                    df.loc[len(df)] = values
                            # in case of ranges between landmarks
                            else:
                                target_landmarks = range_parameter.split(" - ")
                                tmp_tmin = segment_annotation["tmin"][annotation_segment_index+tmp_segment_idx]
                                tmp_tmax = segment_annotation["tmax"][annotation_segment_index+tmp_segment_idx]
                                mid = (tmp_tmin + tmp_tmax)/2
                                landmark_annotation = annotation[annotation["tierName"] == target_info[target_index][tmp_segment_idx]["landmark tier"]].reset_index(drop=True)
                                start_landmark_annotation = landmark_annotation[landmark_annotation["label"].str.contains(landmark_info[target_landmarks[0]])].reset_index(drop=True)
                                end_landmark_annotation = landmark_annotation[landmark_annotation["label"].str.contains(landmark_info[target_landmarks[1]])].reset_index(drop=True)
                                start_landmark_index = np.abs(mid - start_landmark_annotation["tmin"].to_numpy()).argmin()
                                end_landmark_index = np.abs(mid - end_landmark_annotation["tmin"].to_numpy()).argmin()
                                start_landmark_time = start_landmark_annotation["tmin"][start_landmark_index]
                                end_landmark_time = end_landmark_annotation["tmax"][end_landmark_index]
                                step_interval = np.abs(start_landmark_time - end_landmark_time)/stepsize
                                maximum_steps = stepsize
                                if tmp_segment_idx == len(target_labels)-1:
                                    maximum_steps = stepsize + 1
                                for step_idx in range(maximum_steps):
                                    step_time = start_landmark_time + step_idx*step_interval
                                    values = pd.Series(index=df.columns)
                                    values["Filename"] = fname
                                    values["TargetID"] = target_index
                                    values["TokenID"] = token_number
                                    values["Timestep_global"] = timestep_global
                                    values["Timestep_local"] = step_idx
                                    values["Time_index"] = step_time
                                    values["Label"] = segment_annotation["label"][annotation_segment_index+tmp_segment_idx]
                                    values["Start[s]"] = tmp_tmin
                                    time_idx = np.abs(step_time - files[fname].ema.time.values).argmin()
                                    col = target_channels[tmp_segment_idx]+target_dimensions[tmp_segment_idx]
                                    values[col] = signals[tmp_segment_idx][time_idx]
                                    timestep_global += 1
                                    df.loc[len(df)] = values
                elif measurements_info["TYPE"] == "mass-spring parameters":
                    target_index = measurements_parts[measurements_index]["target"]
                    #number_of_segments = len([ for i in range(len(target_info))])
                    target_labels = np.array([target_info[target_index][i]["label"] for i in range(number_of_segments)])
                    current_annotation_labels = segment_annotation["label"][annotation_segment_index:annotation_segment_index+len(target_labels)].to_numpy()
                    if np.array_equal(target_labels,current_annotation_labels):
                        token_number += 1
                    
                        stepsize = measurements_parts[measurements_index]["stepsize"]
                        range_parameter = measurements_parts[measurements_index]["range"]
                        timestep_global = 0
                        signals = []
                        target_channels = []
                        target_dimensions = []
                        for tmp_segment_idx in range(len(target_labels)):
                            target_channel = target_info[target_index][tmp_segment_idx]["channel"]
                            target_dimension = target_info[target_index][tmp_segment_idx]["dimension"]
                            target_parameter = target_info[target_index][tmp_segment_idx]["parameter"]
                            signal, _ = sp.get_signal(data=files[fname].ema,
                                                channel_dict=channel_dict,
                                                target_channel=target_channel,
                                                target_dimension=target_dimension,
                                                target_parameter=target_parameter)
                            values = pd.Series(index=df.columns)
                            values["Filename"] = fname
                            values["TargetID"] = target_index
                            values["TokenID"] = token_number
                            values["Label"] = segment_annotation["label"][annotation_segment_index+tmp_segment_idx]
                            values["Start[s]"] = tmp_tmin
                            for i in range(len(measurements_info["measurements"])):
                                colname = measurements_info["measurements"][i]["target"] + "_" +  measurements_info["measurements"][i]["landmark"] + "_" + measurements_info["measurements"][i]["parameter"]
                                tmp_tmin = segment_annotation["tmin"][annotation_segment_index+tmp_segment_idx]
                                tmp_tmax = segment_annotation["tmax"][annotation_segment_index+tmp_segment_idx]
                                mid = (tmp_tmin + tmp_tmax)/2
                                landmark_annotation = annotation[annotation["tierName"] == target_info[target_index][tmp_segment_idx]["landmark tier"]].reset_index(drop=True)
                                measurement_landmark = measurements_info["measurements"][i]["landmark"]
                                tmp_landmarks = landmark_annotation[landmark_annotation["label"].str.contains(landmark_info[measurement_landmark])].reset_index(drop=True)
                                landmark_index = np.abs(mid - tmp_landmarks["tmin"].to_numpy()).argmin()
                                target_landmark_time = tmp_landmarks["tmin"][landmark_index]
                                if measurements_info["measurements"][i]["parameter"] == "time":
                                    values[colname] = target_landmark_time
                                elif measurements_info["measurements"][i]["parameter"] == "displacement":
                                    time_idx = np.abs(step_time - files[fname].ema.time.values).argmin()
                                    values[colname] = signal[time_idx]
                                elif measurements_info["measurements"][i]["parameter"] == "velocity":
                                    time_idx = np.abs(step_time - files[fname].ema.time.values).argmin()
                                    velocity = sp.derivation(signal=signal,ema_fs=files[fname].ema.attrs["samplerate"],time=files[fname].ema.time.values,order=1)
                                    values[colname] = velocity[time_idx]
                                
        counter += 1
        pbar.setValue(counter)

    return df


