
# import modules
import os
import sys

import numpy as np

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from PySide2.QtUiTools import QUiLoader

import json

#add gui folder to sys.path
absolute_path = os.path.dirname(__file__)
main_path = "/".join(absolute_path.split("/")[:-1]) + "/"
# add path for gui files
sys.path.insert(1,main_path+ "/gui/python_files/")
# add path for data import and export scripts
sys.path.insert(1,main_path+ "/src/data_import_export/")
# add path for inspector windows
sys.path.insert(1,main_path+ "/src/windows/")

# add path for utils
sys.path.insert(1,main_path+ "/src/utils/")


from main_window import Ui_MainWindow
import data_import as di
import filter_application

import inspector


class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.submitData = Signal()

        self.files = {}

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

        # inspector windows
        self.openInspectorWindowButton.clicked.connect(self.openInspectorWindow)
        self.open2DInspectorWindowButton.clicked.connect(self.openInspector2DWindow)
        #self.open3DInspectorWindowButton.clicked.connect(self.openInspector3DWindow)

        #add function to QActions of toolbar
        self.actionexport_landmark_to_JSON.triggered.connect(lambda: self.export_landmarks("JSON"))
        self.actionexport_EMA_to_netcdf.triggered.connect(lambda: self.export_data("netcdf"))

    def export_data(self, fmt):

        directory = QFileDialog.getExistingDirectory(caption="select folder") + "/"
        if fmt == "netcdf":
            number_of_files = self.dataList.count()
            for i in range(number_of_files):
                fname = self.dataList.item(i).text()
                self.files[fname].ema.to_netcdf(directory+fname+".nc")


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
        
        if len(selected_files) != 0:
            channel_allocation_dict = self.collect_channels(self.channelTable)
            self.insp = inspector.inspector_window(data,channel_allocation_dict) 
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

    
    def collect_channels(channelTable):
        number_of_rows = channelTable.rowCount()
        channel_dict = {}
        for i in range(number_of_rows):
            value = int(channelTable.cellWidget(i,0).currentText())-1
            key = channelTable.item(i,1).text()
            channel_dict[key] = value
        return channel_dict


    @Slot(object)
    def on_inspector_store(self,landmarks):
        selected_files = self.dataList.selectedItems()
        clicked_data_item_name = selected_files[0].text()
        self.files[clicked_data_item_name].annotation["ema"] = landmarks

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
        
            

    def addFilesToDataList(self):
        file_urls = QFileDialog().getOpenFileUrls()
        #get main path
        self.files = di.read_data(file_urls = file_urls, file_dict = self.files)
        filenames = list(self.files.keys())
        
        for i in range(len(filenames)):
            dataListEntry = QListWidgetItem(filenames[i])
            self.dataList.addItem(dataListEntry)

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
        if clicked_file.annotation != None:
            len_audio, len_ema = 0,0
            if clicked_file.annotation["audio"] != None:
                len_audio = len(clicked_file.annotation["audio"]["tiers"])
            if clicked_file.annotation["ema"] is not None:
                    len_ema = len(clicked_file.annotation["audio"]["tiers"])
            else:
                    len_ema = 0
            self.annotationTierNumberInfoLabel.setText("audio: "+str(len_audio)+"\nema: "+str(len_ema))

            tier_names_audio = []
            tier_names_ema = []
            audio_tiers = ""
            ema_tiers = ""
            if len_audio != 0:
                
                for i in range(len_audio):
                    tier_names_audio.append(clicked_file.annotation["audio"]["tiers"][i]["tier_name"])
                audio_tiers = ",\n".join(tier_names_audio)

            if len_ema != 0:
                tier_names_ema = []
                keys = list(clicked_file.annotation["ema"].keys())
                ema_tiers = ",\n".join(keys)
            self.annotationTierNamesInfoLabel.setText("audio: "+audio_tiers+"\nema:"+ema_tiers)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
