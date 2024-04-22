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

from ui_measurements import Ui_MEASUREMENTS
#import inspector_plotting as iplt

import pyqtgraph as pg

#load internal modules
import data_import
import plotting as plt
import information_collection as icoll
import automatic_measurements as am

import utils


class measurements_window(QWidget, Ui_MEASUREMENTS):

    def __init__(self, transmittedFiles,transmittedTiers,transmittedChannelAllocation):
        super().__init__()
        self.setupUi(self)


        self.files = transmittedFiles
        self.tiers = transmittedTiers
        self.channel_dict = transmittedChannelAllocation
        self.channels = list(self.channel_dict.keys())
        self.dimensions = ["x","y","z","x+y","x+z","y+z"]
        self.parameters = ["pos","eucl2D","eucl3D"]
        self.measurements = None

        self.default_landmark_dict = {
            "onset": "onset",
            "pvel1": "pvel1",
            "target" : "target",
            "release" : "release",
            "pvel2" : "pvel2",
            "offset" : "offset"
        }

        # get channel denominations
        self.channel_list = self.channels
        self.channel_list1 = self.channel_list.copy()
        self.channel_list2 = self.channel_list.copy()
        # update channel list
        for i in range(len(self.channel_list1)):
            for j in range(len(self.channel_list2)):
                if self.channel_list[i] != self.channel_list1[j] and self.channel_list1[j] + "+" + self.channel_list2[i] not in self.channel_list: self.channel_list.append(self.channel_list1[i] + "+" + self.channel_list2[j])

        self.selectionTreeWidget.setColumnCount(8)
        self.selectionTreeWidget.setHeaderLabels(["","SEGMENT","TIER","LANDMARK TIER","CHANNEL","DIMENSION","PARAMETER","PADDING"])
        for i in range(8): self.selectionTreeWidget.header().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        self.selectionTreeWidget.expandAll()

        self.landmark_comboboxes = {
            0: self.landmarkAllocationComboBox_1,
            1: self.landmarkAllocationComboBox_2,
            2: self.landmarkAllocationComboBox_3,
            3: self.landmarkAllocationComboBox_4,
            4: self.landmarkAllocationComboBox_5,
            5: self.landmarkAllocationComboBox_6
        }

        self.landmark_checkboxes = {
            0: self.landmarkCheckBox_1,
            1: self.landmarkCheckBox_2,
            2: self.landmarkCheckBox_3,
            3: self.landmarkCheckBox_4,
            4: self.landmarkCheckBox_5,
            5: self.landmarkCheckBox_6
        }

        self.landmark_line_edits = {
            0: self.landmarkLineEdit_1,
            1: self.landmarkLineEdit_2,
            2: self.landmarkLineEdit_3,
            3: self.landmarkLineEdit_4,
            4: self.landmarkLineEdit_5,
            5: self.landmarkLineEdit_6
        }

        self.landmark_list = ["onset","pvel1","target","release","pvel2","offset"]
        for i in range(6): self.landmark_comboboxes[i].addItems(self.landmark_list)
        self.measurementsRadioButtons = [
            self.massSpringParametersRadioButton,
            self.trajectoriesRadioButton
        ]

        self.measurementsRadioButtons[0].clicked.connect(self.adjustMeasurementsTable)
        self.measurementsRadioButtons[1].clicked.connect(self.adjustMeasurementsTable)
        self.measurementsRadioButtons[0].click()
        

        self.addTargetButton.clicked.connect(self.addTarget)
        self.removeTargetButton.clicked.connect(self.removeTarget)
        self.addSegmentButton.clicked.connect(self.addSegment)
        self.removeSegmentButton.clicked.connect(self.removeSegment)
        self.addMeasurementButton.clicked.connect(self.addMeasurement)
        self.removeMeasurementButton.clicked.connect(self.removeMeasurement)

        self.runMeasurementsButton.clicked.connect(self.run_measurements)
        self.storeMeasurementsButton.clicked.connect(self.store_measurements)
        self.storeMeasurementsButton.setEnabled(False)
        self.progressBar.setMaximum(len(self.files))

    def store_measurements(self):
        # code from https://stackoverflow.com/questions/61237159/qt-how-to-save-a-generated-file-by-the-program-into-users-machine
        save_dialog = QFileDialog(self,"Save measurements file","measurements.csv")
        
        save_dialog.setAcceptMode(QFileDialog.AcceptSave)
        save_dialog.exec()
        if not save_dialog.selectedFiles():
            pass
        else:
            path_to_file = save_dialog.selectedFiles()[0]
            self.measurements.to_csv(path_to_file,sep=",",encoding="utf8",index=False)

    def run_measurements(self):
        tmp_landmark_dict = self.default_landmark_dict.copy()
        for i in range(len(self.landmark_checkboxes)):
            if self.landmark_checkboxes[i].isChecked():
                tmp_landmark_dict[self.landmark_comboboxes[i].currentText()] = self.landmark_line_edits[i].text()
        target_info = icoll.collect_landmark_info(self.selectionTreeWidget)
        if self.measurementsRadioButtons[0].isChecked():
            measurements_type = self.measurementsRadioButtons[0].text()
        else:
            measurements_type = self.measurementsRadioButtons[1].text()
        measurements_info = icoll.collect_measurements_info(tableWidget=self.measurementsTableWidget,measurements_type=measurements_type)
        self.measurements = am.automatic_measurements(files = self.files,
                                    target_info = target_info,
                                    channel_dict = self.channel_dict,
                                    pbar = self.progressBar,
                                    landmark_info = tmp_landmark_dict,
                                    measurements_info = measurements_info)
        self.storeMeasurementsButton.setEnabled(True)

    def removeMeasurement(self):
        current_row = self.measurementsTableWidget.currentRow()
        if current_row == -1:
            current_row = self.measurementsTableWidget.rowCount() -1
        self.measurementsTableWidget.removeRow(current_row)

    def addMeasurement(self):
        number_of_rows = self.measurementsTableWidget.rowCount()
        self.measurementsTableWidget.insertRow(number_of_rows)
        if self.measurementsRadioButtons[0].isChecked():
            #collect  labels
            label_info = icoll.collect_measurements_label_info(self.selectionTreeWidget)
            labels = []
            for i in range(len(label_info)):
                for j in range(len(label_info[i])):
                    if label_info[i][j]["label"] not in labels:
                        labels.append(label_info[i][j]["label"])
            label_combobox = QComboBox(self.measurementsTableWidget)
            label_combobox.addItems(labels)
            self.measurementsTableWidget.setCellWidget(number_of_rows,0,label_combobox)
            landmarks_combobox = QComboBox(self.measurementsTableWidget)
            landmarks_combobox.addItems(["onset","pvel1","target","release","pvel2","offset"])
            self.measurementsTableWidget.setCellWidget(number_of_rows,1,landmarks_combobox)
            parameters_combobox = QComboBox(self.measurementsTableWidget)
            parameters_combobox.addItems(["position","time","velocity"])
            self.measurementsTableWidget.setCellWidget(number_of_rows,2,parameters_combobox)
        elif self.measurementsRadioButtons[1].isChecked():
            number_of_targets = self.selectionTreeWidget.topLevelItemCount()
            target_list = [str(i+1) for i in range(number_of_targets)]
            target_combobox = QComboBox(self.measurementsTableWidget)
            target_combobox.addItems(target_list)
            self.measurementsTableWidget.setCellWidget(number_of_rows,0,target_combobox)
            range_combobox = QComboBox(self.measurementsTableWidget)
            range_combobox.addItems(["tmin - tmax","onset - offset","onset - target","onset - release","tartet - release","target - offset","release - offset"])
            self.measurementsTableWidget.setCellWidget(number_of_rows,1,range_combobox)
            

    def adjustMeasurementsTable(self):
        number_of_rows = self.measurementsTableWidget.rowCount()
        if self.sender().text() == "mass-spring parameters":
            if number_of_rows != 0:
                for i in range(number_of_rows):
                    self.removeMeasurementButton.click()
            self.measurementsTableWidget.clear()
            self.measurementsTableWidget.setColumnCount(3)
            self.measurementsTableWidget.setHorizontalHeaderLabels(["LABEL","LANDMARK","MEASURE"])
            measurementsTableWidgetHeader = self.measurementsTableWidget.horizontalHeader()
            for i in range(3): measurementsTableWidgetHeader.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        elif self.sender().text() == "trajectories":
            if number_of_rows != 0:
                for i in range(number_of_rows):
                    self.removeMeasurementButton.click()
            self.measurementsTableWidget.clear()
            self.measurementsTableWidget.setColumnCount(3)
            self.measurementsTableWidget.setHorizontalHeaderLabels(["TARGET","RANGE","STEPSIZE"])
            measurementsTableWidgetHeader = self.measurementsTableWidget.horizontalHeader()
            for i in range(3): measurementsTableWidgetHeader.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

    def addSegment(self):
        selected_item = self.selectionTreeWidget.selectedItems()[0]
        if selected_item.parent() == None:
            item = QTreeWidgetItem()
            item.setText(0,"")
            item.setText(7,"100")
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            
            #self.selectionTreeWidget(selected_item,item)
            selected_item.insertChild(selected_item.childCount(),item)

            tiers_combobox = QComboBox(self.selectionTreeWidget)
            tiers_combobox.addItems(self.tiers)
            tiers_combobox.currentTextChanged.connect(self.adjust_tier)
            self.selectionTreeWidget.setItemWidget(item,2,tiers_combobox)
            landmark_tiers_combobox = QComboBox(self.selectionTreeWidget)
            landmark_tiers_combobox.addItems(self.tiers)
            self.selectionTreeWidget.setItemWidget(item,3,landmark_tiers_combobox)
            channel_combobox = QComboBox(self.selectionTreeWidget)
            channel_combobox.addItems(self.channel_list)
            self.selectionTreeWidget.setItemWidget(item,4,channel_combobox)
            dimensions_combobox = QComboBox(self.selectionTreeWidget)
            dimensions_combobox.addItems(self.dimensions)
            self.selectionTreeWidget.setItemWidget(item,5,dimensions_combobox)
            parameters_combobox = QComboBox(self.selectionTreeWidget)
            parameters_combobox.addItems(self.parameters)
            self.selectionTreeWidget.setItemWidget(item,6,parameters_combobox)
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
        item.setText(7,"100")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.selectionTreeWidget.insertTopLevelItem(rowcount,item)
        tiers_combobox = QComboBox(self.selectionTreeWidget)
        tiers_combobox.addItems(self.tiers)
        tiers_combobox.currentTextChanged.connect(self.adjust_tier)
        self.selectionTreeWidget.setItemWidget(item,2,tiers_combobox)
        landmark_tiers_combobox = QComboBox(self.selectionTreeWidget)
        landmark_tiers_combobox.addItems(self.tiers)
        self.selectionTreeWidget.setItemWidget(item,3,landmark_tiers_combobox)
        channel_combobox = QComboBox(self.selectionTreeWidget)
        channel_combobox.addItems(self.channel_list)
        self.selectionTreeWidget.setItemWidget(item,4,channel_combobox)
        dimensions_combobox = QComboBox(self.selectionTreeWidget)
        dimensions_combobox.addItems(self.dimensions)
        self.selectionTreeWidget.setItemWidget(item,5,dimensions_combobox)
        parameters_combobox = QComboBox(self.selectionTreeWidget)
        parameters_combobox.addItems(self.parameters)
        self.selectionTreeWidget.setItemWidget(item,6,parameters_combobox)

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
posfile = "/home/philipp/test2/0005.pos"
wavfile = "/home/philipp/test2/0005.wav"
tgfile = "/home/philipp/test2/0005.TextGrid"

dat = data_import.dataContainer()
dat.ema = data_import.read_AG50x(posfile)
dat.audio = data_import.read_wav(wavfile)

dat.annotation = data_import.read_TextGrid(tgfile)

files["0005"] = dat

posfile = "/home/philipp/test2/0006.pos"
wavfile = "/home/philipp/test2/0006.wav"
tgfile = "/home/philipp/test2/0006.TextGrid"

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
w = measurements_window(transmittedFiles=files,transmittedTiers=tiers,transmittedChannelAllocation=channels)
w.show()
sys.exit(app.exec_())
"""