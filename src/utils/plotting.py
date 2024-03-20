import os
import sys
import io
import numpy as np

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import *

import pyqtgraph as pg
import scipy as sp

import utils

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

def remove_landmarks_from_pw(plot_widget):
    """
        removes all landmarks from the plot widget.
        landmarks are InfiniteLines with labels.
    """
    item_list = plot_widget.allChildItems()
    for item in item_list:
        if isinstance(item,pg.InfiniteLine) and hasattr(item,"label"):
            plot_widget.removeItem(item)

def plot_ema_trajectory(data,panels,signal,target_panel,color,label):
    """
        plotting function
        
    """
    panel, axis = int(list(target_panel)[0]), list(target_panel)[-1]
    plot_item_list = panels[panel]["axes"][axis]["viewbox"].allChildItems()
    plot_success = False
    is_already_plotted = any((isinstance(item,pg.PlotCurveItem) for item in plot_item_list))
    if is_already_plotted == False:

        # plot signal if it is not none
        if type(signal) != None:
            curve_item = pg.PlotCurveItem(
                                            data.time.values,
                                            signal,
                                            pen=pg.mkPen(color,width=2)
                                        )
            panels[panel]["axes"][axis]["viewbox"].addItem(curve_item)
            font = QFont("Helvetica",14)
            panels[panel]["axes"][axis]["axis"].setLabel(text=label, color=color)
            panels[panel]["axes"][axis]["axis"].label.setFont(font)

            plot_success = True
        
    return plot_success

def remove_ema_trajectory(panels,target_panel):
    panel, axis = int(list(target_panel)[0]), list(target_panel)[1]

    itemList = panels[panel]["axes"][axis]["viewbox"].allChildItems()
    is_plotted = (any(isinstance(item,pg.PlotCurveItem) for item in itemList))
    for i in range(len(itemList)):
        if isinstance(itemList[i],pg.PlotCurveItem):
            panels[panel]["axes"][axis]["viewbox"].removeItem(itemList[i])
            panels[panel]["axes"][axis]["axis"].setLabel(text="")
            break