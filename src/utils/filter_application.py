import os
import numpy as np
import xarray as xr
from scipy import signal


def mean_filter(data,N):
    return np.convolve(data,np.ones(N)/N,mode="same")


# butterworth lowpass filter according to:
# https://github.com/guillaume-chevalier/filtering-stft-and-laplace-transform
def butter_lowpass(cutoff, nyq_freq, order=4):
    normal_cutoff = float(cutoff) / nyq_freq
    b, a = signal.butter(order, normal_cutoff, btype='lowpass')
    return b, a

def butter_lowpass_filter(data, cutoff_freq, nyq_freq, order):
    b, a = butter_lowpass(cutoff_freq, nyq_freq, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def filter_data(dataset,cutoff=None,order=None,window=None,filter_type=None):
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
    elif filter_type == "mean":
        for i in range(tmp_data.shape[1]):
            for j in range(tmp_data.shape[2]):
                tmp_data[:,i,j] = mean_filter(data = tmp_data[:,i,j],
                                            N = window
                                            )
    filtered_dataset = xr.Dataset(
                                    data_vars=dict(
                                                    ema=(["time","channels","dimensions"],tmp_data)
                                                ),
                                    coords=dataset.coords,
                                    attrs=dataset.attrs
                                )
    return filtered_dataset