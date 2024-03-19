import os
import sys
import io
import numpy as np
import scipy as sp
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import *


from PySide6.QtUiTools import QUiLoader

#add gui folder to sys.path
absolute_path = os.path.dirname(__file__)
#print(absolute_path)
main_path = "/".join(absolute_path.split("/")[:-2])
#print(main_path)
sys.path.insert(1,main_path+ "/gui/python_files")
sys.path.insert(1,main_path+"/src/data_import_export")
sys.path.insert(1,main_path+"/src/utils")

from ui_landmark_detection import Ui_LM_DETECT
#import inspector_plotting as iplt

import pyqtgraph as pg

import data_import
import plotting as plt

import utils


class landmark_detection_window(QWidget, Ui_LM_DETECT):
    submitLandmarks = Signal(object)

    def __init__(self, transmittedFiles,transmittedTiers,transmittedChannelAllocation):
        super().__init__()
        self.setupUi(self)

        self.files = transmittedFiles
        self.tiers = transmittedTiers
        self.channel_dict = transmittedChannelAllocation

        self.detectedLandmarks = None

        self.channels = list(self.channel_dict.keys())
        self.dimensions = ["x","y","z","x+y","x+z","y+z"]
        self.parameters = ["pos","eucl2D","eucl3D"]
        self.methods = ["vel20","vel15","tvel20_xy","tvel20_xz","tvel20_yz","tvel15_xy","tvel15_xz","tvel15_yz"]

        # get channel denominations
        self.channel_list = self.channels
        self.channel_list1 = self.channel_list.copy()
        self.channel_list2 = self.channel_list.copy()
        # update channel list
        for i in range(len(self.channel_list1)):
            for j in range(len(self.channel_list2)):
                if self.channel_list[i] != self.channel_list1[j] and self.channel_list1[j] + "+" + self.channel_list2[i] not in self.channel_list: self.channel_list.append(self.channel_list1[i] + "+" + self.channel_list2[j])


        self.selectionTreeWidget.setColumnCount(8)
        self.selectionTreeWidget.setHeaderLabels(["","SEGMENT","TIER","CHANNEL","DIMENSION","PARAMETER","METHOD","WINDOWED","PADDING"])
        for i in range(8): self.selectionTreeWidget.header().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        self.selectionTreeWidget.expandAll()

        self.addTargetButton.clicked.connect(self.addTarget)
        self.removeTargetButton.clicked.connect(self.removeTarget)
        self.addSegmentButton.clicked.connect(self.addSegment)
        self.removeSegmentButton.clicked.connect(self.removeSegment)
        self.runLandmarkDetectionButton.clicked.connect(self.run_landmark_detection)
        self.progressBar.setMaximum(len(self.files))
        self.storeLandmarksButton.clicked.connect(self.store_landmarks)

    def run_landmark_detection(self):
        info = utils.collect_landmark_detection_info(self.selectionTreeWidget)
        landmarks, protocol, processed_segments = utils.automatic_landmark_detection(files=self.files,info=info,channel_dict=self.channel_dict,pbar=self.progressBar)
        self.detectedLandmarks = landmarks
        self.progressBar.setValue(len(self.files))
        if processed_segments > 0:
            dlg = QMessageBox()
            dlg.setWindowTitle("Files processes")
            dlg.setText(str(len(self.files))+" files processed and "+str(processed_segments)+" annotated")
            button = dlg.exec_()
            if len(landmarks) != 0:
                self.storeLandmarksButton.setEnabled(True)
        if len(protocol) > 0:
            dlg = QMessageBox.question(self,"log output",str(len(protocol))+" segments not annotated. Print log file?")
            if dlg == QMessageBox.Yes:
                print("rpinted")
            if dlg == QMessageBox.No:
                print("blub")
        
    def store_landmarks(self):
        if self.detectedLandmarks is not None:
            self.submitLandmarks.emit(self.detectedLandmarks)



    def addSegment(self):
        selected_item = self.selectionTreeWidget.selectedItems()[0]
        if selected_item.parent() == None:
            item = QTreeWidgetItem()
            item.setText(0,"")
            item.setText(8,"100")
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            
            #self.selectionTreeWidget(selected_item,item)
            selected_item.insertChild(selected_item.childCount(),item)

            tiers_combobox = QComboBox(self.selectionTreeWidget)
            tiers_combobox.addItems(self.tiers)
            tiers_combobox.currentTextChanged.connect(self.adjust_tier)
            self.selectionTreeWidget.setItemWidget(item,2,tiers_combobox)
            channel_combobox = QComboBox(self.selectionTreeWidget)
            channel_combobox.addItems(self.channel_list)
            self.selectionTreeWidget.setItemWidget(item,3,channel_combobox)
            dimensions_combobox = QComboBox(self.selectionTreeWidget)
            dimensions_combobox.addItems(self.dimensions)
            self.selectionTreeWidget.setItemWidget(item,4,dimensions_combobox)
            parameters_combobox = QComboBox(self.selectionTreeWidget)
            parameters_combobox.addItems(self.parameters)
            self.selectionTreeWidget.setItemWidget(item,5,parameters_combobox)
            methods_combobox = QComboBox(self.selectionTreeWidget)
            methods_combobox.addItems(self.methods)
            self.selectionTreeWidget.setItemWidget(item,6,methods_combobox)
            window_button = QPushButton(" ")
            window_button.setCheckable(True)
            window_button.clicked.connect(self.check_windowed)
            self.selectionTreeWidget.setItemWidget(item,7,window_button)
            self.selectionTreeWidget.expandAll()
            
    
    def removeTarget(self):
        selected_item = self.selectionTreeWidget.selectedItems()[0]
        root = self.selectionTreeWidget.invisibleRootItem()
        if selected_item.parent() == None:
            item_index = self.selectionTreeWidget.indexOfTopLevelItem(selected_item)
            root.removeChild(selected_item)
            number_of_targets = self.selectionTreeWidget.topLevelItemCount()
            print(number_of_targets)
            for i in range(number_of_targets):
                item = self.selectionTreeWidget.topLevelItem(i)
                item.setText(0,str(i+1))


    def removeSegment(self):
        selected_item = self.selectionTreeWidget.selectedItems()[0]
        if selected_item.parent() != None:
            selected_item.parent().removeChild(selected_item)

    def addTarget(self):
        rowcount = self.selectionTreeWidget.topLevelItemCount()
        item = QTreeWidgetItem()
        item.setText(0,str(rowcount+1))
        item.setText(8,"100")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.selectionTreeWidget.insertTopLevelItem(rowcount,item)
        tiers_combobox = QComboBox(self.selectionTreeWidget)
        tiers_combobox.addItems(self.tiers)
        tiers_combobox.currentTextChanged.connect(self.adjust_tier)
        self.selectionTreeWidget.setItemWidget(item,2,tiers_combobox)
        channel_combobox = QComboBox(self.selectionTreeWidget)
        channel_combobox.addItems(self.channel_list)
        self.selectionTreeWidget.setItemWidget(item,3,channel_combobox)
        dimensions_combobox = QComboBox(self.selectionTreeWidget)
        dimensions_combobox.addItems(self.dimensions)
        self.selectionTreeWidget.setItemWidget(item,4,dimensions_combobox)
        parameters_combobox = QComboBox(self.selectionTreeWidget)
        parameters_combobox.addItems(self.parameters)
        self.selectionTreeWidget.setItemWidget(item,5,parameters_combobox)
        methods_combobox = QComboBox(self.selectionTreeWidget)
        methods_combobox.addItems(self.methods)
        self.selectionTreeWidget.setItemWidget(item,6,methods_combobox)
        window_button = QPushButton(" ")
        window_button.setCheckable(True)
        window_button.clicked.connect(self.check_windowed)
        self.selectionTreeWidget.setItemWidget(item,7,window_button)

    def check_windowed(self):
        if self.sender().isChecked():
            self.sender().setText("✔")
        else:
            self.sender().setText(" ")

    def adjust_tier(self):
        current_text = self.sender().currentText()
        number_of_targets = self.selectionTreeWidget.topLevelItemCount()
        for i in range(number_of_targets):
            target_item = self.selectionTreeWidget.topLevelItem(i)
            index = self.selectionTreeWidget.itemWidget(target_item,2).findText(current_text,Qt.MatchFixedString)
            self.selectionTreeWidget.itemWidget(target_item,2).setCurrentIndex(index)
            number_of_segments = target_item.childCount()
            for j in range(number_of_segments):
                segment_item = target_item.child(j)
                index = self.selectionTreeWidget.itemWidget(target_item,2).findText(current_text,Qt.MatchFixedString)
                self.selectionTreeWidget.itemWidget(segment_item,2).setCurrentIndex(index)


"""
# testing

files = {}
posfile = "/home/philipp/test/0005.pos"
wavfile = "/home/philipp/test/0005.wav"
tgfile = "/home/philipp/test/0005.TextGrid"

dat = data_import.dataContainer()
dat.ema = data_import.read_AG50x(posfile)
dat.audio = data_import.read_wav(wavfile)

dat.annotation = data_import.read_TextGrid(tgfile)

files["0005"] = dat

posfile = "/home/philipp/test/0006.pos"
wavfile = "/home/philipp/test/0006.wav"
tgfile = "/home/philipp/test/0006.TextGrid"

dat = data_import.dataContainer()
dat.ema = data_import.read_AG50x(posfile)
dat.audio = data_import.read_wav(wavfile)

dat.annotation = data_import.read_TextGrid(tgfile)

files["0006"] = dat

channels = {
    "TBO": 2,
    "TMID": 3,
    "TTIP" : 4,
    "ULIP" : 5,
    "LLIP" : 6
}

keys = list(files.keys())
tiers = []
for i in range(len(keys)):
    tmp_tiers = files[keys[i]].annotation["tierName"].unique()
    for j in range(len(tmp_tiers)):
        if tmp_tiers[j] not in tiers:
            tiers.append(tmp_tiers[j])
print(tiers)

app = QApplication(sys.argv)
w = landmark_detection_window(transmittedFiles=files,transmittedTiers=tiers,transmittedChannelAllocation=channels)
w.show()
sys.exit(app.exec_())
"""