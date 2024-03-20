
# import modules
import os
import sys

import numpy as np

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtUiTools import QUiLoader

#add gui folder to sys.path
absolute_path = os.path.dirname(__file__)
main_path = "/".join(absolute_path.split("/")[:-1])
# add path for gui files
sys.path.insert(1,main_path+ "/gui/python_files/")
# add path for data import and export scripts
sys.path.insert(1,main_path+ "/src/data_import_export/")
# add path for inspector windows
sys.path.insert(1,main_path+ "/src/windows/")

# add path for utils
sys.path.insert(1,main_path+ "/src/utils/")


from ui_main_window import Ui_MainWindow
import data_import as di
import filter_application

import landmark_detection
import inspector
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.submitData = Signal()

        self.files = {}

        self.tier_names = []

        #add functionality to interface components
        # data list
        self.dataList.itemClicked.connect(self.display_information)
        self.addFilesToDataListButton.clicked.connect(self.addFilesToDataList)
        self.removeFilesFromDataListButton.clicked.connect(self.removeFilesFromDataList)

        # initialize channel table
        self.channelTable.setColumnCount(2)
        self.channelTable.setHorizontalHeaderLabels(["CHANNEL","NAME"])
        channelTableHeader = self.channelTable.horizontalHeader()
        channelTableHeader.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        channelTableHeader.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        # channel buttons
        self.addChannelToChannelTableButton.clicked.connect(self.addChannelToChannelTable)
        self.removeChannelFromChannelTableButton.clicked.connect(self.removeChannelFromChannelTable)

        self.filterOptions =  {
            "None" : self.filterRadioButtonNone,
            "MAfilter" : self.filterRadioButtonMovingAverage,
            "BWLPfilter" : self.filterRadioButtonBWLP

        }

        self.tierList.setColumnCount(1)
        self.tierList.setHorizontalHeaderLabels(["SELECT LANDMARK TIERS"])
        tierListHeader = self.tierList.horizontalHeader()
        tierListHeader.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        
        self.addTierNameToTierListButton.clicked.connect(self.add_tier_name_to_tier_list)
        self.removeTierNameFromTierListButton.clicked.connect(self.remove_tier_name_from_tier_list)

        # inspector windows
        self.openInspectorWindowButton.clicked.connect(self.openInspectorWindow)
        self.open2DInspectorWindowButton.clicked.connect(self.openInspector2DWindow)
        #self.open3DInspectorWindowButton.clicked.connect(self.openInspector3DWindow)

        #add function to QActions of toolbar
        self.actionexport_landmarks_to_csv.triggered.connect(lambda: self.export_landmarks("csv"))
        self.actionexport_landmarks_to_JSON.triggered.connect(lambda: self.export_landmarks("JSON"))
        self.actionexport_landmarks_to_TextGrid.triggered.connect(lambda: self.export_landmark("TextGrid"))
        self.actionexport_EMA_to_netcdf.triggered.connect(lambda: self.export_data("netcdf"))
        self.actionexport_EMA_to_csv.triggered.connect(lambda: self.export_data("csv"))
        self.testButton.clicked.connect(self.test_fun)
        self.landmarkDetectionButton.clicked.connect(self.start_landmark_detection)

    def start_landmark_detection(self):
        channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
        tiers_to_transmit = []
        file_keys = list(self.files.keys())
        for file_key in file_keys:
            tmp_tiers = self.files[file_key].annotation["tierName"].unique()
            for i in range(len(tmp_tiers)):
                if tmp_tiers[i] not in tiers_to_transmit:
                    tiers_to_transmit.append(tmp_tiers[i])
        
        self.lm_detect = landmark_detection.landmark_detection_window(transmittedFiles=self.files,
                                                                 transmittedTiers=tiers_to_transmit,
                                                                 transmittedChannelAllocation=channel_allocation_dict)
        self.lm_detect.setWindowTitle("landmark detection")
        self.lm_detect.submitLandmarks.connect(self.on_landmark_detection_store)
        self.lm_detect.show()

    def test_fun(self):
        clicked_file_name = self.dataList.selectedItems()[0].text()
        print(self.files[clicked_file_name].annotation)



    def remove_tier_name_from_tier_list(self):
        current_row = self.tierList.currentRow()
        if current_row != -1:
            self.tierList.removeRow(current_row)
        else:
            self.tierList.removeRow(self.tierList.rowCount())

    def add_tier_name_to_tier_list(self):
        tier_names = []
        file_keys = list(self.files.keys())
        for file_key in file_keys:
            tiers = self.files[file_key].annotation["tierName"].unique()
            for tier in tiers:
                if tier not in tier_names:
                    tier_names.append(tier)
        number_of_rows = self.tierList.rowCount()
        self.tierList.insertRow(number_of_rows)
        comboBox = QComboBox()
        for i in range(len(tier_names)): comboBox.addItem(tier_names[i])
        self.tierList.setCellWidget(number_of_rows,0,comboBox)


    def export_data(self, fmt):

        directory = QFileDialog.getExistingDirectory(caption="select folder") + "/"
        number_of_files = self.dataList.count()
        if fmt == "netcdf":
            for i in range(number_of_files):
                fname = self.dataList.item(i).text()
                self.files[fname].ema.to_netcdf(directory+fname+".nc")
        elif fmt == "csv":
            for i in range(number_of_files):
                cols = ["Time"]
                fname = self.dataList.item(i).text()
                file = self.files[fname].ema.channels
                print(file)
                df = pd.DataFrame(columns=cols)



    def export_landmarks(self, fmt):

        directory = QFileDialog.getExistingDirectory(caption="select folder") + "/"
        if fmt == "JSON":
            number_of_files = self.dataList.count()
            for i in range(number_of_files):
                fname = self.dataList.item(i).text()
                if isinstance(self.files[fname].annotation["ema"],type(None)) == False:
                    landmarks = self.files[fname].annotation["ema"]
                    with open(directory + fname + ".json",mode="w") as output_file:
                        json.dump(landmarks,output_file,indent=4)
        



    def openInspectorWindow(self):
        
        selected_files = self.dataList.selectedItems()
        clicked_data_item_name = selected_files[0].text()
        data = self.files[clicked_data_item_name]
        
        data.ema = filter_application.filter_data(dataset=data.ema,filter_type="butter",cutoff=15,order=5)

        if self.tierList.rowCount() != 0:
            tier_list_to_transmit = self.collect_articulatory_landmarks()
        else:
            tier_list_to_transmit = []
        if len(selected_files) != 0:
            channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
            self.insp = inspector.inspector_window(transmittedData=data,transmittedChannelAllocation=channel_allocation_dict,transmittedTierList=tier_list_to_transmit) 
            self.insp.setWindowTitle(clicked_data_item_name)
            self.insp.submitLandmarks.connect(self.on_inspector_store)
            self.insp.show()
    
    def openInspector2DWindow(self):
        selected_files = self.dataList.selectedItems()
        clicked_data_item_name = selected_files[0].text()
        data = self.files[clicked_data_item_name]
        data.ema = filter_application.filter_data(dataset=data.ema,filter_type="butter",cutoff=15,order=5)
        if len(selected_files) != 0:
            channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
            self.insp2D = inspector2D.inspector2D_window(data,channel_allocation_dict) 
            self.insp2D.show()

    #def openInspector3DWindow(self):
    #    selected_files = self.dataList.selectedItems()
    #    clicked_data_item_name = selected_files[0].text()
    #    data = self.files[clicked_data_item_name]
    #    if len(selected_files) != 0:
    #        channel_allocation_dict = utils.collect_channels(self.channelTable)
    #        self.insp3D = inspector3D.inspector3D_window(data,channel_allocation_dict) 
    #        self.insp3D.show()

    
    def collect_channels(self,channelTable):
        number_of_rows = channelTable.rowCount()
        channel_dict = {}
        for i in range(number_of_rows):
            value = int(channelTable.cellWidget(i,0).currentText())-1
            key = channelTable.item(i,1).text()
            channel_dict[key] = value
        return channel_dict


    @Slot(object)
    def on_landmark_detection_store(self,landmark_dataframe):
        filenames = landmark_dataframe["Filename"].unique()
        for filename in filenames:
            tmp_landmarks = landmark_dataframe[landmark_dataframe["Filename"] == filename].reset_index(drop=True)
            tmp_landmarks = tmp_landmarks[["tierName","tmin","tmax","label"]]
            print(tmp_landmarks)
            self.files[filename].annotation = pd.concat([self.files[filename].annotation,tmp_landmarks])

    @Slot(object)
    def on_inspector_store(self,landmarks):
        selected_files = self.dataList.selectedItems()
        clicked_data_item_name = selected_files[0].text()
        previous_annotation = self.files[clicked_data_item_name].annotation
        new_tiers = landmarks["tierName"].unique()
        porevious_annotation = previous_annotation[previous_annotation["tierName"].isin(new_tiers) == False].reset_index(drop=True)
        updated_annotation = pd.concat([previous_annotation,landmarks]).reset_index(drop=True)
        self.files[clicked_data_item_name].annotation = updated_annotation
        tier_names = updated_annotation["tierName"].unique()
        for i in range(len(tier_names)):
            if tier_names[i] not in self.tier_names:
                self.tier_names.append(tier_names[i])

    def removeChannelFromChannelTable(self):
        current_row = self.channelTable.currentRow()
        if current_row != -1:
            self.channelTable.removeRow(current_row)
        else:
            self.channelTable.removeRow(self.channelTable.rowCount())
        

    def addChannelToChannelTable(self):
        #add new row
        number_of_rows = self.channelTable.rowCount()
        #add combobox for channel selection
        selected_data_item = self.dataList.selectedItems()
        print(selected_data_item)
        if not selected_data_item:
            pass
        else:
            self.channelTable.insertRow(number_of_rows)
            selected_data_item_name = selected_data_item[0].text()
            channel_options = self.files[selected_data_item_name].ema.channels.values + 1
            print(channel_options)
            comboBox = QComboBox()
            for i in range(len(channel_options)) : comboBox.addItem(str(channel_options[i]))
            self.channelTable.setCellWidget(number_of_rows,0,comboBox)
        
    def collect_articulatory_landmarks(self):
        number_of_rows = self.tierList.rowCount()
        landmark_tier_list = []
        for i in range(number_of_rows):
            tier = self.tierList.cellWidget(i,0).currentText()
            landmark_tier_list.append(tier)
        return landmark_tier_list



    def addFilesToDataList(self):
        file_urls = QFileDialog().getOpenFileUrls()
        #get main path
        self.files = di.read_data(file_urls = file_urls, file_dict = self.files)
        filenames = list(self.files.keys())
        
        for i in range(len(filenames)):
            dataListEntry = QListWidgetItem(filenames[i])
            self.dataList.addItem(dataListEntry)
            if isinstance(self.files[filenames[i]].annotation, pd.DataFrame):
                tiers = self.files[filenames[i]].annotation["tierName"].unique()
                for j in range(len(tiers)):
                    if tiers[j] not in self.tier_names:
                        self.tier_names.append(tiers[j])

    def removeFilesFromDataList(self):
        clicked_item = self.dataList.selectedItems()[0]
        clicked_item_index = self.dataList.currentRow()
        self.files.pop(clicked_item.text())
        self.dataList.takeItem(clicked_item_index)

    def display_information(self):
        clicked_item_name = self.dataList.selectedItems()[0].text()
        clicked_file = self.files[clicked_item_name]
        if clicked_file.ema != None:
            self.emaDeviceInfoLabel.setText(clicked_file.ema.attrs["device"])
            self.emaDurationInfoLabel.setText(str(clicked_file.ema.attrs["duration"].round(2))+ " s")
            self.emaChannelInfoLabel.setText(str(len(clicked_file.ema.channels)))
            self.emaSamplerateInfoLabel.setText(str(clicked_file.ema.attrs["samplerate"]))    
        else:
            self.emaDeviceInfoLabel.setText("NA")
            self.emaDurationInfoLabel.setText("NA")
            self.emaChannelInfoLabel.setText("NA")
            self.emaSamplerateInfoLabel.setText("NA")
        if clicked_file.audio != None:
            self.audioDurationInfoLabel.setText(str(clicked_file.audio.attrs["samplerate"]))
            self.audioSamplerateInfoLabel.setText(str(clicked_file.audio.attrs["duration"].round(2)) + " s")
        else:
            self.audioDurationInfoLabel.setText("NA")
            self.audioSamplerateInfoLabel.setText("NA")
        if isinstance(clicked_file.annotation, pd.DataFrame):
            number_of_tiers = len(clicked_file.annotation["tierName"].unique())
            self.annotationTierNumberInfoLabel.setText(str(number_of_tiers))
            tiers = clicked_file.annotation["tierName"].unique()
            number_of_rows = self.tierList.rowCount()
            # update comboboxews
            #if number_of_rows != 0:
            #    for i in range(number_of_rows):
            #        items = []

        else:
            self.annotationTierNumberInfoLabel.setText("NA")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
