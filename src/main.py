
# import modules
import os
import sys

import numpy as np
import platform

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from PySide6.QtUiTools import QUiLoader


#add gui folder to sys.path
absolute_path = os.path.dirname(__file__)


pform = platform.platform()
if "win" in pform or "Win" in pform:
    slash = "\\"
    main_path = slash.join(absolute_path.split(slash)[:-1])
    home_path = slash.join(absolute_path.split(slash)[:3]) + slash
else:
    slash = "/"
    main_path = slash.join(absolute_path.split(slash)[:-1])
    home_path = "~" + slash.join(absolute_path.split(slash)[:3]) + slash


# add path for gui files
sys.path.insert(1,main_path + slash + "gui" + slash + "python_files" + slash)
# add path for data import and export scripts
sys.path.insert(1,main_path + slash + "src" + slash + "data_import_export" + slash)
# add path for inspector windows
sys.path.insert(1,main_path + slash + "src" + slash + "windows" + slash)

# add path for utils
sys.path.insert(1,main_path + slash + "src" + slash + "utils" + slash)


from ui_main_window import Ui_MainWindow
import data_import as din
import data_export as dout
import filter_application

import landmark_detection
import inspector
import inspector2D
import measurements

import pandas as pd
import json

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


class MainWindow(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.submitData = Signal()

        self.files = {}

        self.tier_names = []

        self.plot_configuration = None

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
        self.measurementsButton.clicked.connect(self.openMeasurementsWindow)

        #add function to QActions of toolbar
        self.actionexport_landmarks_to_csv.triggered.connect(lambda: self.export_landmarks("csv"))
        self.actionexport_landmarks_to_JSON.triggered.connect(lambda: self.export_landmarks("JSON"))
        self.actionexport_landmarks_to_TextGrid.triggered.connect(lambda: self.export_landmarks("TextGrid"))
        self.actionexport_EMA_to_netcdf.triggered.connect(lambda: self.export_data("netcdf"))
        self.actionexport_EMA_to_csv.triggered.connect(lambda: self.export_data("csv"))
        self.actionexport_channel_allocation.triggered.connect(self.export_channel_allocation)

        self.actionimport_channel_allocation.triggered.connect(self.import_channel_allocation)
        #self.testButton.clicked.connect(self.test_fun)
        self.landmarkDetectionButton.clicked.connect(self.start_landmark_detection)

        self.multipleSelectionButton.clicked.connect(self.activate_multiple_selection)

    def import_channel_allocation(self):
        if self.dataList.count() > 0:
            self.dataList.setCurrentItem(self.dataList.item(0))
            json_url = QFileDialog().getOpenFileUrl()
            file_path = json_url[0].toLocalFile()
            file = open(file_path,mode="r",encoding="utf8")
            channel_allocation = json.load(file)
            keys = list(channel_allocation.keys())
            for key in keys:
                self.addChannelToChannelTable()
                current_row = self.channelTable.rowCount()-1
                index = self.channelTable.cellWidget(current_row,0).findText(channel_allocation[key]["channel"])
                self.channelTable.cellWidget(current_row,0).setCurrentIndex(index)
                item = QTableWidgetItem()
                item.setText(channel_allocation[key]["label"])
                self.channelTable.setItem(current_row,1,item)


    def export_channel_allocation(self):
        channels = {}
        number_of_rows = self.channelTable.rowCount()
        for i in range(number_of_rows):
            tmp = {}
            print(i,self.channelTable.cellWidget(i,0).currentText())
            tmp["channel"] = self.channelTable.cellWidget(i,0).currentText()
            tmp["label"] = self.channelTable.item(i,1).text()
            channels[i] = tmp
        
        save_dialog = QFileDialog(self,"Save channel allocation file","channel_allocation.json")
        
        save_dialog.setAcceptMode(QFileDialog.AcceptSave)
        save_dialog.exec()
        if not save_dialog.selectedFiles():
            pass
        else:
            path_to_file = save_dialog.selectedFiles()[0]
        with open(path_to_file,mode="w") as output_file:
            json.dump(channels,output_file,indent=4)



    def activate_multiple_selection(self):
        if self.sender().isChecked():
            self.sender().setStyleSheet("background-color: green")
            self.dataList.setSelectionMode(QAbstractItemView.MultiSelection)
        else:
            self.sender().setStyleSheet("background-color: light gray")
            self.dataList.setSelectionMode(QAbstractItemView.SingleSelection)

    def openMeasurementsWindow(self):
        channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
        tiers_to_transmit = []
        file_keys = list(self.files.keys())
        for file_key in file_keys:
            if self.files[file_key].annotation is not None:
                tmp_tiers = self.files[file_key].annotation["tierName"].unique()
                for i in range(len(tmp_tiers)):
                    if tmp_tiers[i] not in tiers_to_transmit:
                        tiers_to_transmit.append(tmp_tiers[i])

        # filter data
        files_to_transmit = self.files.copy()
        file_keys = list(files_to_transmit.keys())
        file_options_keys = list(self.filterOptions.keys())
        for file_key in file_keys:
            for filter_key in file_options_keys:
                if self.filterOptions[filter_key].isChecked():
                    if filter_key == "MAfilter":
                        window_size = int(self.movingAverageInput.text())
                        files_to_transmit[file_key].ema = filter_application.filter_data(dataset=files_to_transmit[file_key].ema,filter_type="mean",window=window_size)
                    elif filter_key == "BWLPfilter":
                        cutoff = int(self.bwLowPassCutoffInput.text())
                        order = int(self.bwLowPassOrderInput.text())
                        files_to_transmit[file_key].ema = filter_application.filter_data(dataset=files_to_transmit[file_key].ema,filter_type="butter",cutoff=15,order=5)
        self.measurementsWindow = measurements.measurements_window(transmittedFiles=files_to_transmit,
                                                                 transmittedTiers=tiers_to_transmit,
                                                                 transmittedChannelAllocation=channel_allocation_dict)
        self.measurementsWindow.setWindowTitle("Measurements")
        #self.measurementsWindow.submitLandmarks.connect(self.on_landmark_detection_store)
        self.measurementsWindow.show()
        
    def start_landmark_detection(self):
        channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
        tiers_to_transmit = []
        file_keys = list(self.files.keys())
        for file_key in file_keys:
            if self.files[file_key].annotation is not None:
                tmp_tiers = self.files[file_key].annotation["tierName"].unique()
                for i in range(len(tmp_tiers)):
                    if tmp_tiers[i] not in tiers_to_transmit:
                        tiers_to_transmit.append(tmp_tiers[i])

        # filter data
        files_to_transmit = self.files.copy()
        file_keys = list(files_to_transmit.keys())
        file_options_keys = list(self.filterOptions.keys())
        for file_key in file_keys:
            for filter_key in file_options_keys:
                if self.filterOptions[filter_key].isChecked():
                    if filter_key == "MAfilter":
                        window_size = int(self.movingAverageInput.text())
                        files_to_transmit[file_key].ema = filter_application.filter_data(dataset=files_to_transmit[file_key].ema,filter_type="mean",window=window_size)
                    elif filter_key == "BWLPfilter":
                        cutoff = int(self.bwLowPassCutoffInput.text())
                        order = int(self.bwLowPassOrderInput.text())
                        files_to_transmit[file_key].ema = filter_application.filter_data(dataset=files_to_transmit[file_key].ema,filter_type="butter",cutoff=15,order=5)
        
        self.lm_detect = landmark_detection.landmark_detection_window(transmittedFiles=files_to_transmit,
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
            if self.files[file_key].annotation is not None:
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

        directory = QFileDialog.getExistingDirectory(caption="select folder") + slash
        number_of_files = self.dataList.count()
        progressDialog = QProgressDialog("Save files",None,0,number_of_files)
        progressDialog.setWindowModality(Qt.WindowModal)
        progressDialog.setMaximum(number_of_files)
        progressDialog.setValue(0)
        progressDialog.setMinimumDuration(0)
        progressDialog.show()
        if fmt == "netcdf":
            for i in range(number_of_files):
                fname = self.dataList.item(i).text()
                self.files[fname].ema.to_netcdf(directory+fname+".nc")
                progressDialog.setValue(i)
        elif fmt == "csv":
            channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
            channel_names = list(channel_allocation_dict.keys())
            for file_index in range(number_of_files):
                cols = ["Time"]
                fname = self.dataList.item(file_index).text()
                channels = self.files[fname].ema.channels.values
                dimensions = self.files[fname].ema.dimensions.values[:-2]
                for i in range(len(channel_names)):
                    for j in range(len(dimensions)):
                        cols.append(str(channel_names[i])+"_"+str(dimensions[j]))
                df = pd.DataFrame(columns=cols)
                
                df["Time"] = self.files[fname].ema.time.values
                for i in range(len(channel_names)):
                    for j in range(len(dimensions)):
                        df[str(channel_names[i])+"_"+str(dimensions[j])] = self.files[fname].ema.sel(channels=channel_allocation_dict[channel_names[i]]).sel(dimensions=dimensions[j]).ema.values
                df.to_csv(directory+fname+".csv",sep=",",encoding="utf8",index=False)
                progressDialog.setValue(file_index)



    def export_landmarks(self, fmt):

        directory = QFileDialog.getExistingDirectory(caption="select folder") + slash
        landmark_tier_names = tier_list_to_transmit = self.collect_articulatory_landmarks()
        number_of_files = self.dataList.count()
        
        if fmt == "JSON":
            for file_idx in range(number_of_files):
                fname = self.dataList.item(file_idx).text()
                tier_names = self.files[fname].annotation["tierName"].unique()
                tmp_dict = {}
                if self.files[fname].annotation is not None:
                    for i in range(len(tier_names)):
                        if tier_names[i] in landmark_tier_names:
                            tmp = {}
                            tmp_landmarks = self.files[fname].annotation[self.files[fname].annotation["tierName"] == tier_names[i]].reset_index(drop=True)
                            for j in range(len(tmp_landmarks)):
                                segment = {}
                                segment["time"] = tmp_landmarks["tmin"][j]
                                segment["label"] = tmp_landmarks["label"][j]
                                tmp[j] = segment
                            tmp_dict[tier_names[i]] = tmp
                        else:
                            tmp = {}
                            tmp_landmarks = self.files[fname].annotation[self.files[fname].annotation["tierName"] == tier_names[i]].reset_index(drop=True)
                            for j in range(len(tmp_landmarks)):
                                segment = {}
                                segment["tmin"] = tmp_landmarks["tmin"][j]
                                segment["tmax"] = tmp_landmarks["tmax"][j]
                                segment["label"] = tmp_landmarks["label"][j]
                                tmp[j] = segment
                            tmp_dict[tier_names[i]] = tmp

                    with open(directory + fname + ".json",mode="w") as output_file:
                        json.dump(tmp_dict,output_file,indent=4)
        elif fmt == "csv":
            for file_idx in range(number_of_files):
                fname = self.dataList.item(file_idx).text()
                tier_names = self.files[fname].annotation["tierName"].unique()
                if self.files[fname].annotation is not None:
                    tmp_landmarks = self.files[fname].annotation[self.files[fname].annotation["tierName"].isin(tier_names)].reset_index(drop=True)
                    tmp_landmarks.to_csv(directory+fname+".csv",sep=",",encoding="utf8",index=False)
        elif fmt == "TextGrid":
            for file_idx in range(number_of_files):
                fname = self.dataList.item(file_idx).text()
                if self.files[fname].annotation is not None:
                    dout.export_annotation_to_TextGrid(directory=directory,fname=fname,annotation=self.files[fname].annotation,landmark_tier_names=landmark_tier_names)

    def openInspectorWindow(self):
        selected_files = self.dataList.selectedItems()
        clicked_data_item_name = selected_files[0].text()
        data = self.files[clicked_data_item_name]
        file_options_keys = list(self.filterOptions.keys())
        for filter_key in file_options_keys:
            if self.filterOptions[filter_key].isChecked():
                if filter_key == "MAfilter":
                    window_size = int(self.movingAverageInput.text())
                    data.ema = filter_application.filter_data(dataset=data.ema,filter_type="mean",window=window_size)
                elif filter_key == "BWLPfilter":
                    cutoff = int(self.bwLowPassCutoffInput.text())
                    order = int(self.bwLowPassOrderInput.text())
                    data.ema = filter_application.filter_data(dataset=data.ema,filter_type="butter",cutoff=15,order=5)

        if self.tierList.rowCount() != 0:
            tier_list_to_transmit = self.collect_articulatory_landmarks()
        else:
            tier_list_to_transmit = []
        channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
        self.insp = inspector.inspector_window(transmittedData=data,
                                               transmittedChannelAllocation=channel_allocation_dict,
                                               transmittedTierList=tier_list_to_transmit,
                                               transmittedPlotConfiguration=self.plot_configuration) 
        self.insp.setWindowTitle(clicked_data_item_name)
        self.insp.submitLandmarks.connect(self.on_inspector_store)
        self.insp.submitPlotConfiguration.connect(self.on_plot_configuration_store)
        self.insp.show()
    
    def openInspector2DWindow(self):
        selected_files = self.dataList.selectedItems()
        clicked_data_item_name = selected_files[0].text()
        data = self.files[clicked_data_item_name]
        file_options_keys = list(self.filterOptions.keys())
        for filter_key in file_options_keys:
            if self.filterOptions[filter_key].isChecked():
                if filter_key == "MAfilter":
                    window_size = int(self.movingAveragInput)
                    data.ema = filter_application.filter_data(dataset=data.ema,filter_type="mean",window=window_size)
                elif filter_key == "BWLPfilter":
                    cutoff = int(self.bwLowPassCutoffInput.text())
                    order = int(self.bwLowPassOrderInput.text())
                    data.ema = filter_application.filter_data(dataset=data.ema,filter_type="butter",cutoff=15,order=5)
        if self.tierList.rowCount() != 0:
            tier_list_to_transmit = self.collect_articulatory_landmarks()
        else:
            tier_list_to_transmit = []
        if len(selected_files) != 0:
            channel_allocation_dict = self.collect_channels(channelTable=self.channelTable)
            self.insp2D = inspector2D.inspector2D_window(data,channel_allocation_dict,tier_list_to_transmit) 
            self.insp2D.setWindowTitle(clicked_data_item_name)
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
            if len(tmp_landmarks) != 0:
                tmp_landmarks = tmp_landmarks[["tierName","tmin","tmax","label"]]
                tiers = tmp_landmarks["tierName"].unique()
                self.files[filename].annotation = self.files[filename].annotation[self.files[filename].annotation["tierName"].isin(tiers) == False].reset_index(drop=True)
                self.files[filename].annotation = pd.concat([self.files[filename].annotation,tmp_landmarks])

    @Slot(object)
    def on_plot_configuration_store(self,plot_configuration):
        self.plot_configuration = plot_configuration

    @Slot(object)
    def on_inspector_store(self,landmarks):
        selected_files = self.dataList.selectedItems()
        clicked_data_item_name = selected_files[0].text()
        previous_annotation = self.files[clicked_data_item_name].annotation
        new_tiers = landmarks["tierName"].unique()
        landmark_tiers = self.collect_articulatory_landmarks()
        previous_annotation = previous_annotation[np.logical_and(previous_annotation["tierName"].isin(new_tiers) == False,previous_annotation["tierName"].isin(landmark_tiers) == False)].reset_index(drop=True)
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
        if not selected_data_item:
            pass
        else:
            self.channelTable.insertRow(number_of_rows)
            selected_data_item_name = selected_data_item[0].text()
            channel_options = self.files[selected_data_item_name].ema.channels.values + 1
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
        ema_format = self.emaFormatComboBox.currentText()
        audio_format = self.audioFormatComboBox.currentText()
        annotation_format = self.annotationFormatComboBox.currentText()
        tmp_files = din.read_data(file_urls = file_urls, 
                                   ema_format = ema_format, 
                                   audio_format = audio_format, 
                                   annotation_format = annotation_format,
                                   slash = slash)
        filenames = list(tmp_files.keys())
        
        for i in range(len(filenames)):
            files_keys = list(self.files.keys())
            if filenames[i] in files_keys:
                number_of_same_name = files_keys.count(filenames[i])
                new_filename = filenames[i] + " - " + str(number_of_same_name)
            else:
                new_filename = filenames[i]
            self.files[new_filename] = tmp_files[filenames[i]]
            dataListEntry = QListWidgetItem(new_filename)
            self.dataList.addItem(dataListEntry)
            if isinstance(self.files[new_filename].annotation, pd.DataFrame):
                tiers = self.files[new_filename].annotation["tierName"].unique()
                for j in range(len(tiers)):
                    if tiers[j] not in self.tier_names:
                        self.tier_names.append(tiers[j])

    def removeFilesFromDataList(self):
        if self.multipleSelectionButton.isChecked():
            selected_items = self.dataList.selectedItems()
            for i in range(len(selected_items)):
                fname = selected_items[i].text()
                self.files.pop(fname)
                file_index = self.dataList.row(selected_items[i])
                self.dataList.takeItem(file_index)
        else:
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
            self.audioDurationInfoLabel.setText(str(clicked_file.audio.attrs["duration"].round(2)) + " s")
            self.audioSamplerateInfoLabel.setText(str(clicked_file.audio.attrs["samplerate"]))
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
w.setWindowTitle("ADA - Articulatory Data Analysis")
w.show()
sys.exit(app.exec())
