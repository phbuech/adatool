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

def collect_measurements_info(tableWidget,measurements_type):
    measurements_dict = {}
    measurements_dict["TYPE"] = measurements_type
    measurements_dict["measurements"] = {}
    number_of_rows = tableWidget.rowCount()
    if measurements_type == "mass-spring parameters":
        for i in range(number_of_rows):
            tmp = {}
            tmp["label"] = tableWidget.cellWidget(i,0).currentText()
            tmp["landmark"] = tableWidget.cellWidget(i,1).currentText()
            tmp["parameter"] = tableWidget.cellWidget(i,2).currentText()
            measurements_dict["measurements"][i] = tmp
    elif measurements_type == "trajectories":
        for i in range(number_of_rows):
            tmp = {}
            tmp["target"] = int(tableWidget.cellWidget(i,0).currentText())
            tmp["range"] = tableWidget.cellWidget(i,1).currentText()
            tmp["stepsize"] = int(tableWidget.item(i,2).text())
            measurements_dict["measurements"][i] = tmp
    return measurements_dict





def collect_landmark_info(treeWidget):
    info = {}
    number_of_targets = treeWidget.topLevelItemCount()
    for i in range(number_of_targets):
        segments = {}
        tmp = {}
        target_item = treeWidget.topLevelItem(i)
        
        tmp["label"] = target_item.text(1)
        tmp["tier"] = treeWidget.itemWidget(target_item,2).currentText()
        tmp["landmark tier"] = treeWidget.itemWidget(target_item,3).currentText()
        tmp["channel"] =  treeWidget.itemWidget(target_item,4).currentText()
        tmp["dimension"] = treeWidget.itemWidget(target_item,5).currentText()
        tmp["parameter"] = treeWidget.itemWidget(target_item,6).currentText()
        tmp["padding"] = np.float64(target_item.text(7))
        segments[0] = tmp
        number_of_segments = target_item.childCount()
        for j in range(number_of_segments):
            tmp = {}
            segment_item = target_item.child(j)

            tmp["label"] = segment_item.text(1)
            tmp["tier"] = treeWidget.itemWidget(segment_item,2).currentText()
            tmp["landmark tier"] = treeWidget.itemWidget(target_item,3).currentText()
            tmp["channel"] =  treeWidget.itemWidget(segment_item,4).currentText()
            tmp["dimension"] = treeWidget.itemWidget(segment_item,5).currentText()
            tmp["parameter"] = treeWidget.itemWidget(segment_item,6).currentText()
            tmp["padding"] = np.float64(segment_item.text(7))
            segments[j+1] = tmp
        info[i+1] = segments
    return info



def collect_measurements_label_info(treeWidget):
    info = {}
    number_of_targets = treeWidget.topLevelItemCount()
    for i in range(number_of_targets):
        segments = {}
        tmp = {}
        target_item = treeWidget.topLevelItem(i)
        tmp["label"] = target_item.text(1)
        segments[0] = tmp
        number_of_segments = target_item.childCount()
        for j in range(number_of_segments):
            tmp = {}
            segment_item = target_item.child(j)
            tmp["label"] = segment_item.text(1)
            segments[j+1] = tmp
        info[i] = segments
    return info

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
        segments[i+1] = tmp
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