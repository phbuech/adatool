import os
import numpy as np
import xarray as xr

from scipy.io import wavfile
import chardet
import pyqtgraph as pg
from scipy import signal

import pandas as pd
import utils

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import signal_processing as sp


def detect_landmarks_vel(time,velocity,tmin,tmax,factor):
    landmarks = {}
    tmin_idx = np.abs(tmin - time).argmin()
    tmax_idx = np.abs(tmax - time).argmin()
    velocity = velocity[tmin_idx:tmax_idx]
    maximum = np.where(velocity == np.max(velocity))[0][0]
    minimum = np.where(velocity == np.min(velocity))[0][0]
    if maximum > minimum:
        pvel_to_idx = minimum
        pvel_fro_idx = maximum
    else:
        pvel_to_idx = maximum
        pvel_fro_idx = minimum

    velmax_pvel_to = velocity[pvel_to_idx]*factor
    velmax_pvel_fro = velocity[pvel_fro_idx]*factor

    tgt_idx = np.abs(velmax_pvel_to - velocity[pvel_to_idx:pvel_fro_idx]).argmin() + pvel_to_idx
    release_idx = np.abs(velmax_pvel_fro - velocity[pvel_to_idx:pvel_fro_idx]).argmin() + pvel_to_idx

    onset_idx = np.abs(velmax_pvel_to -velocity[:pvel_to_idx]).argmin()
    offset_idx = np.abs(velmax_pvel_fro - velocity[pvel_fro_idx:]).argmin() + pvel_fro_idx

    landmarks["pvel_to"] = time[pvel_to_idx]
    landmarks["pvel_fro"] =time[pvel_fro_idx]
    landmarks["target"] = time[tgt_idx]
    landmarks["release"] = time[release_idx]
    landmarks["onset"] = time[onset_idx]
    landmarks["offset"] = time[offset_idx]

    return landmarks

def detect_landmarks_tvel(time,tangential_velocity,tmin,tmax,factor):
    landmarks = {}
    tmin_idx = np.abs(tmin - time).argmin()
    tmax_idx = np.abs(tmax - time).argmin()
    mid = (tmin + tmax)/2
    mid_idx = np.abs(mid - time).argmin()
    pvel_to_idx = tmin_idx + tangential_velocity[tmin_idx:mid_idx].argmax()
    pvel_fro_idx = mid_idx + tangential_velocity[mid_idx:tmax_idx].argmax()
    velmax_pvel_to = tangential_velocity[tmin_idx:mid_idx].max()
    velmax_pvel_fro = tangential_velocity[mid_idx:tmax_idx].max()
    minimum_idx = pvel_to_idx + tangential_velocity[pvel_to_idx:pvel_fro_idx].argmin()

    target_idx = pvel_to_idx + np.abs((velmax_pvel_to)*factor - tangential_velocity[pvel_to_idx:minimum_idx]).argmin()
    release_idx = minimum_idx + np.abs((velmax_pvel_fro)*factor - tangential_velocity[minimum_idx:pvel_fro_idx]).argmin()
    onset_idx = tmin_idx + tangential_velocity[tmin_idx:pvel_to_idx].argmin()
    offset_idx = pvel_fro_idx + tangential_velocity[pvel_fro_idx:tmax_idx].argmin()
    

    landmarks["pvel_to"] = time[pvel_to_idx]
    landmarks["pvel_fro"] = time[pvel_fro_idx]
    landmarks["target"] = time[target_idx]
    landmarks["release"] = time[release_idx]
    landmarks["onset"] = time[onset_idx]
    landmarks["offset"] = time[offset_idx]

    return landmarks


def automatic_landmark_detection(files,info,channel_dict,pbar):
    print(info)
    target_tier = info[0][1]["tier"]
    keys = list(files.keys())
    missing_segments = 0
    segment_count = 0
    protocol = []
    #progress = QProgressDialog("Process files","abort detection",0,len(files))
    #progress.setWindowModality(Qt.WindowModal)
    landmarks_dataframe = pd.DataFrame(columns=["Filename","tierName","tmin","tmax","label"])
    for key_index in range(len(keys)):
        data = files[keys[key_index]]
        if data.annotation is not None:
            tmp_annotation = data.annotation.copy()
            tmp_annotation  = tmp_annotation[tmp_annotation["tierName"] == target_tier].reset_index(drop=True)
            for segment_annotation_index in range(len(tmp_annotation)):
                for target_index in range(len(info)):
                    print(info)
                    segment_labels = np.array([info[target_index][ii+1]["label"] for ii in range(len(info[target_index]))])
                    annotation_labels = tmp_annotation["label"][segment_annotation_index:segment_annotation_index+len(segment_labels)].to_numpy()
                    if np.array_equal(annotation_labels,segment_labels):
                        for segment_index in range(len(segment_labels)):
                            current_index = segment_annotation_index + segment_index
                            target_channel = info[target_index][segment_index+1]["channel"]
                            target_dimension = info[target_index][segment_index+1]["dimension"]
                            target_parameter = info[target_index][segment_index+1]["parameter"]
                            method = info[target_index][segment_index+1]["method"]
                            windowed = info[target_index][segment_index+1]["windowed"]
                            padding = info[target_index][segment_index+1]["padding"]/1000
                            signal, _ = sp.get_signal(data=data.ema,channel_dict=channel_dict,target_channel=target_channel,target_dimension=target_dimension,target_parameter=target_parameter)
                            tmin = tmp_annotation["tmin"][current_index]
                            tmax = tmp_annotation["tmax"][current_index]
                            if "tvel" in "method":
                                dims = list(detection_algorithm.split("_")[1])
                                velocity = sp.get_tangential_velocity(data=signal,channel_index=channel_dict[target_channel],dims=dims)
                            else:
                                velocity = sp.derivation(signal,ema_fs=data.ema.attrs["samplerate"],time=data.ema.time.values,order=1)
                            tmin_pad = tmin-padding
                            tmax_pad = tmax+padding
                            tmin_pad_index = np.abs(tmin_pad-data.ema.time.values).argmin()
                            tmax_pad_index = np.abs(tmax_pad-data.ema.time.values).argmin()
                            velocity = velocity[tmin_pad_index:tmax_pad_index]
                            time = data.ema.time.values[tmin_pad_index:tmax_pad_index]
                            if windowed:
                                wfun = sp.window_function(x=time,tmin_pad=tmin_pad,tmin_=tmin-0.025,tmax_=tmax+0.025,tmax_pad=tmax_pad)
                                velocity = velocity*wfun
                            is_missing = False
                            if "tvel20" in method:
                                try:
                                    landmarks = detect_landmarks_tvel(time=time,tangential_velocity=velocity,tmin=tmin_pad,tmax=tmax_pad,factor=0.2)
                                except:
                                    missing_segments += 1
                                    is_missing = True
                            elif "tvel15" in method:
                                try:
                                    landmarks = detect_landmarks_tvel(time=time,tangential_velocity=velocity,tmin=tmin_pad,tmax=tmax_pad,factor=0.15)
                                except:
                                    missing_segments += 1
                                    is_missing = True
                            elif method == "vel20":
                                try:
                                    landmarks = detect_landmarks_vel(time=time,velocity=velocity,tmin=tmin_pad,tmax=tmax_pad,factor=0.2)
                                except:
                                    missing_segments += 1
                                    is_missing = True
                            elif method == "vel15":
                                try:
                                    landmarks = detect_landmarks_vel(time=time,velocity=velocity,tmin=tmin_pad,tmax=tmax_pad,factor=0.15)
                                except:
                                    missing_segments += 1
                                    is_missing = True
                            if is_missing == False:
                                landmark_keys = list(landmarks.keys())
                                segment_count += 1
                                for landmark_key in landmark_keys:
                                    landmark = pd.Series(index=landmarks_dataframe.columns)
                                    landmark["Filename"] = keys[key_index]
                                    landmark["tierName"] = segment_labels[segment_index]
                                    landmark["tmin"] = landmarks[landmark_key]
                                    landmark["tmax"] = landmarks[landmark_key]
                                    landmark["label"] = landmark_key
                                    landmarks_dataframe.loc[len(landmarks_dataframe)] = landmark
                            else:
                                row = [keys[key_index], target_tier, segment_labels[segment_index], tmin]
                                protocol.append(row)
        pbar.setValue(key_index+1)
        print(landmarks_dataframe)
    return landmarks_dataframe, protocol, segment_count