import os
import numpy as np
import xarray as xr

import scipy
from scipy.io import wavfile
import chardet
import pyqtgraph as pg
from scipy import signal
import librosa

import pandas as pd

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import *

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def calculate_rms(input_signal):
    intensity = librosa.feature.rms(y=input_signal)
    return intensity[0]

def calculate_f0_pyin(input_signal,time,fs):
    resampled_signal = signal.resample(x=input_signal,num=int(time[-1]/(1/8000)))
    f0, voiced_flag, voiced_prob = librosa.pyin(y=resampled_signal,
                                                fmin=65,
                                                fmax=1000,
                                                sr=8000,
                                                frame_length=int(8000*0.04),
                                                win_length=int(8000*0.02),
                                                hop_length=int(8000*0.01))
    return f0

def calculate_f0_yin(input_signal,time,fs):
    resampled_signal = signal.resample(x=input_signal,num=int(time[-1]/(1/8000)))
    f0 = librosa.yin(y=resampled_signal,
                     fmin=65,
                     fmax=700,
                     sr=8000,
                     frame_length=int(8000*0.04),
                     win_length=int(8000*0.02),
                     hop_length=int(8000*0.01))
    return f0

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

