import os
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

def mean_filter(data,N):
    return np.convolve(data,np.ones(N)/N,mode="same")

def butter_lowpass(cutoff, nyq_freq, order=4):
    normal_cutoff = float(cutoff) / nyq_freq
    b, a = signal.butter(order, normal_cutoff, btype='lowpass')
    return b, a

def butter_lowpass_filter(data, cutoff_freq, nyq_freq, order):
    # Source: https://github.com/guillaume-chevalier/filtering-stft-and-laplace-transform
    b, a = butter_lowpass(cutoff_freq, nyq_freq, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def add_landmarks_to_pw(plot_widget,landmarks):
    for i in range(len(landmarks)):
        infline = pg.InfiniteLine(
                                    pos = landmarks["tmin"][i],
                                    label = landmarks["label"][i],
                                    movable = True,
                                    pen = pg.mkPen("green",width=4),
                                    labelOpts={"position" : 0.95}
                                )
        plot_widget.addItem(infline)

def filter_data(dataset,cutoff,order,filter_type=None):
    tmp_data = dataset.ema.values.copy()

    if filter_type == "butter":
        for i in range(tmp_data.shape[1]):
            for j in range(tmp_data.shape[2]):
                tmp_data[:,i,j] = butter_lowpass_filter(
                                                    data = tmp_data[:,i,j],
                                                    cutoff_freq=cutoff,
                                                    nyq_freq = dataset.attrs["samplerate"]/2,
                                                    order = order                             
                                                    )

    filtered_dataset = xr.Dataset(
                                    data_vars=dict(
                                                    ema=(["time","channels","dimensions"],tmp_data)
                                                ),
                                    coords=dataset.coords,
                                    attrs=dataset.attrs
                                )
    return filtered_dataset



def remove_landmarks_from_pw(plot_widget):
    """
        removes all landmarks from the plot widget.
        landmarks are InfiniteLines with labels.
    """
    item_list = plot_widget.allChildItems()
    for item in item_list:
        if isinstance(item,pg.InfiniteLine) and hasattr(item,"label"):
            plot_widget.removeItem(item)
            

def collect_landmarks(plot_widget):
    item_list = plot_widget.allChildItems()
    lm_counter = 0
    lm_dict = {}
    for item in item_list:
        if isinstance(item,pg.InfiniteLine):
            if hasattr(item,"label"):
                lm_dict[lm_counter] = {
                                        "position" : item.pos()[0],
                                        "label" : item.label.format
                                    }
                lm_counter += 1
    print(lm_dict)
    return lm_dict

def collect_channels(channelTable):
    number_of_rows = channelTable.rowCount()
    channel_dict = {}
    for i in range(number_of_rows):
        value = int(channelTable.cellWidget(i,0).currentText())-1
        key = channelTable.item(i,1).text()
        channel_dict[key] = value
    return channel_dict
    

def get_channel_indexes(channel_dict,target_channels):
    """
        retrieves channels indexes
        returns a tuple
    """
    tmp_channels = target_channels.split("+")
    channel_indexes = tuple()
    for i in range(len(tmp_channels)): channel_indexes += (channel_dict[tmp_channels[i]],)

    return channel_indexes

def get_signal_for_distance_plot(data,channel_indexes,target_dimension):
    """
        asd
    """
    x1 = data.sel(channels=channel_indexes[0]).sel(dimensions=target_dimension).ema.values
    x2 = data.sel(channels=channel_indexes[1]).sel(dimensions=target_dimension).ema.values

    return np.abs(x1-x2)

def get_euclidean_distance2D(data,channel_indexes,target_dimensions):
    x1 = data.sel(channels=channel_indexes[0]).sel(dimensions=target_dimensions[0]).ema.values
    x2 = data.sel(channels=channel_indexes[0]).sel(dimensions=target_dimensions[1]).ema.values
    y1 = data.sel(channels=channel_indexes[1]).sel(dimensions=target_dimensions[0]).ema.values
    y2 = data.sel(channels=channel_indexes[1]).sel(dimensions=target_dimensions[1]).ema.values

    eucl2D = np.sqrt(
                        (x1 - y1)**2 + (x2 - y2)**2
                    )
    return eucl2D

def get_euclidean_distance3D(data,channel_indexes,target_dimensions):
    x1 = data.sel(channels=channel_indexes[0]).sel(dimensions=target_dimensions[0]).ema.values
    x2 = data.sel(channels=channel_indexes[0]).sel(dimensions=target_dimensions[1]).ema.values
    x3 = data.sel(channels=channel_indexes[0]).sel(dimensions=target_dimensions[2]).ema.values

    y1 = data.sel(channels=channel_indexes[1]).sel(dimensions=target_dimensions[0]).ema.values
    y2 = data.sel(channels=channel_indexes[1]).sel(dimensions=target_dimensions[1]).ema.values
    y3 = data.sel(channels=channel_indexes[1]).sel(dimensions=target_dimensions[2]).ema.values



    eucl3D = np.sqrt(
                        (x1 - y1)**2 + (x2 - y2)**2 + (x3 - y3)**2
                    )
    return eucl3D

def derivation(signal,ema_fs,time,order):
    tmp = signal
    dx = time[1]-time[0]
    for i in range(order):
        tmp = np.gradient(tmp,dx)
    return tmp

def get_tangential_velocity(data,channel_index,dims):
    x = data.sel(channels=channel_index).sel(dimensions=dims[0]).ema.values
    y = data.sel(channels=channel_index).sel(dimensions=dims[1]).ema.values

    x_vel = derivation(
                        signal = x,
                        ema_fs = data.attrs["samplerate"],
                        time = data.time.values,
                        order = 1
                    )
    
    y_vel = derivation(
                        signal = y,
                        ema_fs = data.attrs["samplerate"],
                        time = data.time.values,
                        order = 1
                    )

    tvel = np.sqrt( x_vel**2 + y_vel**2)
    return tvel

def get_signal(data,channel_dict,target_channel,target_dimension,target_parameter):
    signal = None
    #plot position data
    dims = target_dimension.split("+")
    if "+" not in target_channel:
        if "+" not in target_dimension and target_parameter in ["pos","vel","acc"]:
            signal = data.sel(channels=channel_dict[target_channel]).sel(dimensions=target_dimension).ema.values
            if target_parameter == "vel":
                signal = derivation(
                                            signal = signal,
                                            ema_fs = data.attrs["samplerate"],
                                            time = data.time.values,
                                            order = 1
                                        )
            elif target_parameter == "acc":
                signal = derivation(
                                            signal = signal,
                                            ema_fs = data.attrs["samplerate"],
                                            time = data.time.values,
                                            order = 2
                                        )
        elif len(dims) == 2 and target_parameter == "tanvel":
            signal = get_tangential_velocity(
                                                    data = data,
                                                    channel_index = channel_dict[target_channel],
                                                    dims = dims 
                                                )

    #plot distances  
    if "+" in target_channel:
        channel_indexes = get_channel_indexes(channel_dict,target_channel)
        dims = target_dimension.split("+") 
        if len(dims) == 1 and target_parameter == "dist":
            signal = get_signal_for_distance_plot(
                                                        data=data,
                                                        channel_indexes=channel_indexes,
                                                        target_dimension=target_dimension
                                                        )
        elif len(dims) > 1 and target_parameter in ["eucl2D","eucl3D"]:
            if len(dims) == 2:
                signal = get_euclidean_distance2D(
                                                        data = data,
                                                        channel_indexes = channel_indexes,
                                                        target_dimensions = dims
                                                        )
            elif len(dims) == 3:
                signal = get_euclidean_distance3D(
                                                        data = data,
                                                        channel_indexes = channel_indexes,
                                                        target_dimensions = dims
                                                        )
    label = target_channel + " ("+ target_dimension + ", "+ target_parameter + ")"
    return signal, label


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


def collect_landmark_detection_info(treeWidget):
    info = {}
    number_of_targets = treeWidget.topLevelItemCount()
    for i in range(number_of_targets):
        segments = {}
        tmp = {}
        target_item = treeWidget.topLevelItem(i)
        
        tmp["label"] = target_item.text(1)
        tmp["tier"] = treeWidget.itemWidget(target_item,2).currentText()
        tmp["channel"] =  treeWidget.itemWidget(target_item,3).currentText()
        tmp["dimension"] = treeWidget.itemWidget(target_item,4).currentText()
        tmp["parameter"] = treeWidget.itemWidget(target_item,5).currentText()
        tmp["method"] =  treeWidget.itemWidget(target_item,6).currentText()
        tmp["windowed"] = treeWidget.itemWidget(target_item,7).isChecked()
        tmp["padding"] = np.float64(target_item.text(8))
        segments[0] = tmp
        number_of_segments = target_item.childCount()
        for j in range(number_of_segments):
            tmp = {}
            segment_item = target_item.child(j)

            tmp["label"] = segment_item.text(1)
            tmp["tier"] = treeWidget.itemWidget(segment_item,2).currentText()
            tmp["channel"] =  treeWidget.itemWidget(segment_item,3).currentText()
            tmp["dimension"] = treeWidget.itemWidget(segment_item,4).currentText()
            tmp["parameter"] = treeWidget.itemWidget(segment_item,5).currentText()
            tmp["method"] =  treeWidget.itemWidget(segment_item,6).currentText()
            tmp["windowed"] = treeWidget.itemWidget(segment_item,7).isChecked()
            tmp["padding"] = np.float64(segment_item.text(8))
            segments[j+1] = tmp
        info[i] = segments
    return info

def gauss_function(x,mu,sigma):
    return np.exp(-(x-mu )**2/(2*sigma**2))

def build_window(x,g1,g2,tmin,tmax):
    tmp = []
    for xi in range(len(x)):
        if x[xi] < tmin:
            tmp.append(g1[xi])
        elif x[xi] >= tmin and x[xi] <= tmax:
            tmp.append(1.0)
        elif x[xi] > tmax:
            tmp.append(g2[xi])
    return np.array(tmp)

def window_function(x,tmin_pad,tmin_,tmax_,tmax_pad):
    mu1 = tmin_
    sigma1 = np.abs(tmin_pad-tmin_)/4
    gauss_function1 = gauss_function(x,mu1,sigma1)
    
    mu2 = tmax_
    sigma2 = np.abs(tmax_-tmax_pad)/4
    gauss_function2 = gauss_function(x,mu2,sigma2)
    
    
    
    window_fun = build_window(x,gauss_function1,gauss_function2,tmin_,tmax_)
    return window_fun

def automatic_landmark_detection(files,info,channel_dict,pbar):
    target_tier = info[0][0]["tier"]
    keys = list(files.keys())
    missing_segments = 0
    segment_count = 0
    protocol = []
    #progress = QProgressDialog("Process files","abort detection",0,len(files))
    #progress.setWindowModality(Qt.WindowModal)
    landmarks_dataframe = pd.DataFrame(columns=["Filename","tierName","tmin","tmax","label"])
    for key_index in range(len(keys)):
        data = files[keys[key_index]]
        tmp_annotation = data.annotation.copy()
        tmp_annotation  = tmp_annotation[tmp_annotation["tierName"] == target_tier].reset_index(drop=True)
        for segment_annotation_index in range(len(tmp_annotation)):
            for target_index in range(len(info)):
                segment_labels = np.array([info[target_index][ii]["label"] for ii in range(len(info[target_index]))])
                annotation_labels = tmp_annotation["label"][segment_annotation_index:segment_annotation_index+len(segment_labels)].to_numpy()
                if np.array_equal(annotation_labels,segment_labels):
                    for segment_index in range(len(segment_labels)):
                        current_index = segment_annotation_index + segment_index
                        target_channel = info[target_index][segment_index]["channel"]
                        target_dimension = info[target_index][segment_index]["dimension"]
                        target_parameter = info[target_index][segment_index]["parameter"]
                        method = info[target_index][segment_index]["method"]
                        windowed = info[target_index][segment_index]["windowed"]
                        padding = info[target_index][segment_index]["padding"]/1000
                        signal, _ = get_signal(data=data.ema,channel_dict=channel_dict,target_channel=target_channel,target_dimension=target_dimension,target_parameter=target_parameter)
                        tmin = tmp_annotation["tmin"][current_index]
                        tmax = tmp_annotation["tmax"][current_index]
                        if "tvel" in "method":
                            dims = list(detection_algorithm.split("_")[1])
                            velocity = get_tangential_velocity(data=signal,channel_index=channel_dict[target_channel],dims=dims)
                        else:
                            velocity = derivation(signal,ema_fs=data.ema.attrs["samplerate"],time=data.ema.time.values,order=1)
                        tmin_pad = tmin-padding
                        tmax_pad = tmax+padding
                        tmin_pad_index = np.abs(tmin_pad-data.ema.time.values).argmin()
                        tmax_pad_index = np.abs(tmax_pad-data.ema.time.values).argmin()
                        velocity = velocity[tmin_pad_index:tmax_pad_index]
                        time = data.ema.time.values[tmin_pad_index:tmax_pad_index]
                        if windowed:
                            wfun = window_function(x=time,tmin_pad=tmin_pad,tmin_=tmin-0.025,tmax_=tmax+0.025,tmax_pad=tmax_pad)
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
