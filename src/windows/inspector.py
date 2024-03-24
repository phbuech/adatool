# load external modules
import os
import sys
import io
import numpy as np
import pandas as pd
import scipy as scp

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

from ui_inspector import Ui_INSPECTOR
#import inspector_plotting as iplt


import sounddevice as sd
import pyqtgraph as pg

#load internal modules
import data_import
import plotting as plt
import information_collection as icoll
import signal_processing as sp
import landmark_detection_backend as ldb

import inspector



#uiclass, baseclass = pg.Qt.loadUiType(absolute_path+"/gui/inspector.ui")

class inspector_window(QMainWindow, Ui_INSPECTOR):
    submitLandmarks = Signal(object)

    def __init__(self, transmittedData,transmittedChannelAllocation,transmittedTierList):
        super().__init__()
        self.setupUi(self)

        
        self.data = transmittedData
        self.channels = transmittedChannelAllocation
        self.tierList = transmittedTierList

        
        

        # make dictead
        self.emaPanelDict = {}
        self.emaPanelDict[1] = {
                                "Panel": self.emaPanel1,
                                "PlotWidget": self.emaPlotWidget1,
                                "axes" : self.initialize_ema_axes(self.emaPlotWidget1)
                                }
        self.emaPanelDict[2] = {
                                "Panel": self.emaPanel2,
                                "PlotWidget": self.emaPlotWidget2,
                                "axes" : self.initialize_ema_axes(self.emaPlotWidget2)
                                }
        self.emaPanelDict[3] = {
                                "Panel": self.emaPanel3,
                                "PlotWidget": self.emaPlotWidget3,
                                "axes" : self.initialize_ema_axes(self.emaPlotWidget3)
                                }

        #assign tiers to combobox
        try:
            if self.data.annotation is not None:
                tiers = self.data.annotation["tierName"].unique()
                for i in range(len(tiers)): 
                    if tiers[i] not in self.tierList:
                        self.audioAnnotationComboBox.addItem(tiers[i])
        except:
            pass

        self.displayAnnotationPushButton.clicked.connect(self.displayAudioAnnotations)
        self.toolBox.setStyleSheet("background-color:dark gray")
        
        self.landmarkRegister = pd.DataFrame(columns=["tierName","tmin","tmax","label"])
        
        #self.temporaryLandmarkRegister = {}

        # initialize waveform plot
        if self.data.audio != None:
            self.plot_audio_waveform()
        self.waveformPlotWidget.setMouseEnabled(x=False,y=False)
        for i in range(1,4): self.emaPanelDict[i]["PlotWidget"].setMouseEnabled(x=False,y=False)

        #self.waveformPlotWidget.scene().installEventFilter(self)

        self.waveformSlider.setMaximum(0)
        self.waveformSlider_2.setMaximum(0)
        # add functionality to slider
        self.waveformSlider.valueChanged.connect(self.sliderMovePlot)
        self.waveformSlider_2.valueChanged.connect(self.sliderMovePlot)
        #self.waveformPlotWidget.sigXRangeChanged.connect(self.move_slider)

        # show grids for all plotwidgets
        self.waveformPlotWidget.showGrid(x=True,y=True)        
        #for i in range(1,4): self.emaPanelDict[i]["PlotWidget"].showGrid(x=True,y=True)
        self.spectrogramFrame.hide()
        self.showSpectrogramButton.clicked.connect(self.show_spectrogram)
        self.spectrogramWidget.setMouseEnabled(x=False,y=False)
        self.plot_spectrogram()
        self.spectrogramWidget.setXLink(self.waveformPlotWidget)


        # hide ema panels 2 and 3
        self.emaPanelDict[2]["Panel"].hide()
        self.emaPanelDict[3]["Panel"].hide()
        
        self.displayEmaPanel1PushButton.clicked.connect(self.show_ema_panel)
        self.displayEmaPanel1PushButton.setStyleSheet("background-color : green")
        self.displayEmaPanel2PushButton.clicked.connect(self.show_ema_panel)
        self.displayEmaPanel3PushButton.clicked.connect(self.show_ema_panel)


        # initialize zoom buttons
        self.zoomInButton.clicked.connect(lambda: self.zoom("in"))
        self.zoomOutButton.clicked.connect(lambda: self.zoom("out"))


        # initialize plot controls for ema
        self.emaControlTable.setColumnCount(6)
        self.emaControlTable.setHorizontalHeaderLabels(["PLOT","CHAN","DIM","PARAM","PANEL","COLOR"])
        emaControlTableHeader = self.emaControlTable.horizontalHeader()
        for i in range(6): emaControlTableHeader.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

        # add functionality to channel button
        self.addChannelToEmaControlTableButton.clicked.connect(self.addChannelToEmaControlTable)
        self.removeChannelFromEmaControlTableButton.clicked.connect(self.removeChannelFromEmaControlTable)

        # add functionalty to landmark control buttons
        self.selectRegionButton.clicked.connect(self.select_region_activation)

        self.region_selection = {
                                "emaPlotWidget1" : None,
                                "emaPlotWidget2" : None,
                                "emaPlotWidget3" : None
                                }

        #for i in range(1,4): self.emaPanelDict[i]["PlotWidget"].scene().installEventFilter(self)

        for i in range(1,4): self.emaPanelDict[i]["PlotWidget"].scene().sigMouseClicked.connect(self.add_landmarks)
        for i in range(1,4): self.emaPanelDict[i]["PlotWidget"].scene().sigMouseClicked.connect(self.rename_landmarks)
        for i in range(1,4): self.emaPanelDict[i]["PlotWidget"].scene().sigMouseClicked.connect(self.remove_landmarks)

        for i in range(1,4): self.emaPanelDict[i]["PlotWidget"].scene().sigItemAdded.connect(self.item_added)

        self.addLandmarkButton.clicked.connect(self.activate_landmark_addition)
        self.renameLandmarkButton.clicked.connect(self.activate_landmark_renaming)
        self.removeLandmarkButton.clicked.connect(self.activate_landmark_removal)

        # linear Region item register
        self.LinearRegionItemRegister = {
                                            "waveformPlotWidget" : None,
                                            "emaPlotWidget1" : None,
                                            "emaPlotWidget2" : None,
                                            "emaPlotWidget3" : None
                                        }
        self.pw_names = ["waveformPlotWidget","spectrogramWidget","emaPlotWidget1","emaPlotWidget2","emaPlotWidget3"]

        # initialize line for mouse cursor location
        self.locationLines = {
                                "waveformPlotWidget": pg.InfiniteLine(pos=0,movable=False,pen=pg.mkPen("white",width=0.5)),
                                "spectrogramWidget" : pg.InfiniteLine(pos=0,movable=False,pen=pg.mkPen("white",width=0.5)),
                                "emaPlotWidget1" : pg.InfiniteLine(pos=0,movable=False,pen=pg.mkPen("white",width=0.5)),
                                "emaPlotWidget2" : pg.InfiniteLine(pos=0,movable=False,pen=pg.mkPen("white",width=0.5)),
                                "emaPlotWidget3" : pg.InfiniteLine(pos=0,movable=False,pen=pg.mkPen("white",width=0.5))
                            }
         
        for pw_name in self.pw_names: 
                if "emaPlotWidget" in pw_name:
                    emaPlotWidget_index = int(list(pw_name)[-1])    
                    self.emaPanelDict[emaPlotWidget_index]["PlotWidget"].addItem(self.locationLines[pw_name])
                    self.emaPanelDict[emaPlotWidget_index]["PlotWidget"].scene().sigMouseMoved.connect(self.mouse_hover)
                elif "waveformPlotWidget" == pw_name:
                    self.waveformPlotWidget.addItem(self.locationLines["waveformPlotWidget"])
                    self.waveformPlotWidget.scene().sigMouseMoved.connect(self.mouse_hover)
                elif "spectrogramWidget" == pw_name:
                    self.spectrogramWidget.addItem(self.locationLines["spectrogramWidget"])
                    self.spectrogramWidget.scene().sigMouseMoved.connect(self.mouse_hover)

        self.scatterItemRegister = {}
        self.scatterLabelRegister = {}

        self.displayLandmarksCheckBoxes = {
                                            1 : self.emaPanel1DisplayLandmarksPushButton,
                                            2 : self.emaPanel2DisplayLandmarksPushButton,
                                            3 : self.emaPanel3DisplayLandmarksPushButton
                                        }
        self.landmarksTierLineEdits = {
                                        1 : self.emaPanel1TierNameLineEdit,
                                        2 : self.emaPanel2TierNameLineEdit,
                                        3 : self.emaPanel3TierNameLineEdit
                                    }

        self.emaLandmarksComboBoxes = { 0 : self.emaAllTiersComboBox,
                                        1 : self.emaPanel1SelectTierComboBox,
                                        2 : self.emaPanel2SelectTierComboBox,
                                        3 : self.emaPanel3SelectTierComboBox
                                    }
        for i in range(1,4): self.emaLandmarksComboBoxes[i].currentTextChanged.connect(self.landmark_cmbbox_value_changed)

        if len(self.tierList) != 0:
            self.landmarkRegister = self.data.annotation[self.data.annotation["tierName"].isin(self.tierList)].reset_index(drop=True)
            for i in range(4):
                for j in range(len(self.tierList)):
                    self.emaLandmarksComboBoxes[i].addItem(self.tierList[j])


        self.removeTierButton.clicked.connect(self.remove_tier)
        for i in range(1,4): self.displayLandmarksCheckBoxes[i].clicked.connect(self.display_landmarks)
        self.storeLandmarksButton.clicked.connect(self.store_landmarks)
        

        #self.test.clicked.connect(self.test_fun)

        self.installEventFilter(self)

        self.PLAY_AUDIO.clicked.connect(self.play_audio)

        self.audioAnnotationComboBox.currentTextChanged.connect(self.change_audio_annotation_tier)

        self.waveformSplitter.splitterMoved.connect(self.movingSplitter)
        self.emaSplitter.splitterMoved.connect(self.movingSplitter)
        self.emaSplitter.setSizes([1000,1])

        self.zoomSelectionButton.clicked.connect(self.zoom_selection)
        self.zoomAllButton.clicked.connect(self.zoom_all)
        self.showSpectrogramButton.click()
        self.showFundamentalFrequencyButton.clicked.connect(self.plot_fundamental_frequency)
        self.showIntensityButton.clicked.connect(self.plot_intensity)
        self.showFundamentalFrequencyButton.setText(" ")
        self.showIntensityButton.setText(" ")
        self.displayAnnotationPushButton.setText(" ")

        #create 2nd spectrogram axis
        self.specgram_2nd_axis = pg.ViewBox()
        self.specgram_2nd_axis.setMouseEnabled(x=False,y=False)
        p1 = self.spectrogramWidget
        #p1.showAxis("right")
        p1.scene().addItem(self.specgram_2nd_axis)
        p1.getAxis("right").linkToView(self.specgram_2nd_axis)
        self.specgram_2nd_axis.setXLink(p1)
        
        def updateViews():
            self.specgram_2nd_axis.setGeometry(p1.getViewBox().sceneBoundingRect())
            self.specgram_2nd_axis.linkedViewChanged(p1.getViewBox(),self.specgram_2nd_axis.XAxis)
        updateViews()
        p1.getViewBox().sigResized.connect(updateViews)

        
        
        
        # assign ema tiers to comboboxes:
        #if self.data.annotation is not None:
        #    if "ema" in list(self.data.annotation.keys()):
        #        ema_tiers = list(self.data.annotation["ema"].keys())
        #        for i in range(len(self.emaLandmarksComboBoxes)):
        #            for tier in ema_tiers:
        #                self.emaLandmarksComboBoxes[i+1].addItem(tier)

    def plot_intensity(self):
        if self.showFundamentalFrequencyButton.isChecked() == False:
            if self.sender().isChecked():
                audio_signal = self.data.audio.signal.values
                time = self.data.audio.time.values
                intensity = sp.calculate_rms(input_signal=audio_signal)
                intensity = 20*np.log10((intensity/np.min(intensity)))
                intensity_curve = pg.PlotCurveItem(pen=pg.mkPen(color="yellow",width=3))
                t = np.linspace(0,time[-1],len(intensity))
                intensity_curve.setData(t,intensity)
                ymin, ymax = np.nanmin(intensity), np.nanmax(intensity)
                self.spectrogramWidget.showAxis("right")
                self.specgram_2nd_axis.addItem(intensity_curve)
                self.specgram_2nd_axis.setRange(yRange=[ymin,ymax])
                self.specgram_2nd_axis.setZValue(1)
                font = QFont("Helvetica",8)
                self.spectrogramWidget.getAxis("right").setLabel(text="rms amplitude",color="yellow")
                self.spectrogramWidget.getAxis("right").label.setFont(font)
                self.sender().setStyleSheet("background-color : green")
                self.sender().setText("✔")
            else:
                self.spectrogramWidget.hideAxis("right")
                #remove f0 plot curve
                item_list = self.specgram_2nd_axis.allChildItems()
                for i in range(len(item_list)):
                    if isinstance(item_list[i],pg.PlotCurveItem):
                        self.specgram_2nd_axis.removeItem(item_list[i])
                self.sender().setStyleSheet("background-color : light gray")
                self.sender().setText(" ")
        else:
            self.sender().setChecked(False)


    def plot_fundamental_frequency(self):
        if self.showIntensityButton.isChecked() == False:
            if self.sender().isChecked():
                #calculate f0
                self.sender().setStyleSheet("background-color : red")
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle("running f0 estimation")
                msgBox.setText("estimate f0 ...\nwait until the red button is green.\nPress Ok to continue.")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
                audio_signal = self.data.audio.signal.values
                time = self.data.audio.time.values
                if self.fundamentalFrequencyComboBox.currentText() == "pYin":
                    f0 = sp.calculate_f0_pyin(input_signal=audio_signal,time=time,fs=self.data.audio.attrs["samplerate"])
                elif self.fundamentalFrequencyComboBox.currentText() == "Yin":
                    f0 = sp.calculate_f0_yin(input_signal=audio_signal,time=time,fs=self.data.audio.attrs["samplerate"])
                ymin, ymax = np.nanmin(f0),np.nanmax(f0)
                f0 = np.nan_to_num(f0)
                #initialize second y axis
                
                t = np.linspace(0,time[-1],len(f0))
                f0_curve = pg.PlotCurveItem(pen=pg.mkPen(color="blue",width=3))
                f0_curve.setData(t,f0)
                self.spectrogramWidget.showAxis("right")
                self.specgram_2nd_axis.addItem(f0_curve)
                self.specgram_2nd_axis.setRange(yRange=[ymin,ymax])
                self.specgram_2nd_axis.setZValue(1)
                font = QFont("Helvetica",8)
                self.spectrogramWidget.getAxis("right").setLabel(text="f0 (Hz)",color="blue")
                self.spectrogramWidget.getAxis("right").label.setFont(font)
                self.sender().setStyleSheet("background-color : green")
                self.sender().setText("✔")
                #self.f0_vb.addItem(f0_curve)
            else:
                self.spectrogramWidget.hideAxis("right")
                #remove f0 plot curve
                item_list = self.specgram_2nd_axis.allChildItems()
                for i in range(len(item_list)):
                    if isinstance(item_list[i],pg.PlotCurveItem):
                        self.specgram_2nd_axis.removeItem(item_list[i])
                self.sender().setStyleSheet("background-color : light gray")
                self.sender().setText(" ")
        else:
            self.sender().setChecked(False)


    def plot_spectrogram(self):
        pg.setConfigOptions(imageAxisOrder='row-major')
        #remove spectrogram
        window_size = int(self.data.audio.attrs["samplerate"]*0.005)
        time_step = int(self.data.audio.attrs["samplerate"]*0.001)
        fs = self.data.audio.attrs["samplerate"]

        win = scp.signal.windows.hamming(window_size,sym=True)
        #win = scp.signal.windows.gaussian(window_size,std=50,sym=True)
        SFT = scp.signal.ShortTimeFFT(win,hop=time_step,fs=1/fs,mfft=2048)
        Sxx = SFT.spectrogram(self.data.audio.signal.values,detr="constant")
        Sxx = 10 * np.log10(Sxx)
        img = pg.ImageItem()
        tr = QTransform()
        tr.scale(self.data.audio.time.values[-1]/np.size(Sxx, axis=1),(fs/2)/np.size(Sxx, axis=0))
        img.setTransform(tr)
        img.setImage(image=Sxx,autoLevels=False)
        img.setLevels([Sxx.max()-70,Sxx.max()])
        img.setColorMap("inferno")
        
        self.spectrogramWidget.getViewBox().addItem(img)
        font = QFont("Helvetica",8)
        self.spectrogramWidget.getAxis("left").setLabel(text="Frequency (Hz)",color="white")
        self.spectrogramWidget.getAxis("left").label.setFont(font)
        self.spectrogramWidget.setLimits(xMin=0, xMax=self.data.audio.time.values[-1], yMin=0, yMax=6500)

    def show_spectrogram(self):
        if self.sender().isChecked():
            self.spectrogramFrame.show()
            self.sender().setStyleSheet("background-color : green")
        else:
            self.spectrogramFrame.hide()
            self.sender().setStyleSheet("background-color : light gray")


    def remove_tier(self):
        if self.emaAllTiersComboBox.count() != 0:
            tier_name = self.emaAllTiersComboBox.currentText()
            self.landmarkRegister = self.landmarkRegister[self.landmarkRegister["tierName"] != tier_name].reset_index(drop=True)
            for i in range(1,4):
                if self.emaLandmarksComboBoxes[i].currentText() == tier_name and self.displayLandmarksCheckBoxes[i].isChecked():
                    self.displayLandmarksCheckBoxes[i].click()
            self.update_landmark_comboboxes()


    def movingSplitter(self,pos,index):
        if self.sender().objectName() == "waveformSplitter":
            self.emaSplitter.moveSplitter(pos,index)
        elif self.sender().objectName() == "emaSplitter":
            self.waveformSplitter.moveSplitter(pos,index)


    def removeChannelFromEmaControlTable(self):
        current_row = self.emaControlTable.currentRow()
        if current_row == -1:
            current_row = self.emaControlTable.rowCount() -1
        plot_checkbox = self.emaControlTable.cellWidget(current_row,0)
        if plot_checkbox.isChecked():
            self.plot_trajectory(button_index=current_row)
        self.emaControlTable.removeRow(current_row)

    def change_audio_annotation_tier(self,evt):
        if self.displayAnnotationPushButton.isChecked():
            self.displayAnnotationPushButton.setChecked(False)
        #if self.audioAnnotationComboBox.currentText() != "Tier":
        #    self.displayAnnotationPushButton.setChecked(True)
        
        


    def play_audio(self):
        if isinstance(self.LinearRegionItemRegister["waveformPlotWidget"],pg.LinearRegionItem):
            x = self.LinearRegionItemRegister["waveformPlotWidget"].getRegion()

        xmin = np.abs(self.data.audio.time.values - x[0]).argmin()
        xmax = np.abs(self.data.audio.time.values - x[1]).argmin()
        sound_snippet = self.data.audio.signal.values[xmin:xmax]
        sr = self.data.audio.attrs["samplerate"]
        sd.play(sound_snippet,sr)


    def displayAudioAnnotations(self):
        if self.sender().isChecked():
            if self.audioAnnotationComboBox.currentText() != "Tiers":
                tier_name = self.audioAnnotationComboBox.currentText()
                segments = self.data.annotation[self.data.annotation["tierName"] == tier_name].reset_index(drop=True)
                for segment_idx in range(len(segments)):
                                acoustic_landmark = pg.InfiniteLine(
                                                                    angle = 90,
                                                                    pos = segments["tmin"][segment_idx],
                                                                    label = segments["label"][segment_idx],
                                                                    labelOpts   = {
                                                                            "position" : 0.95,
                                                                            "anchors"  : (0,0)
                                                                        },
                                                                    movable     = False,
                                                                    pen         = pg.mkPen("green", width = 2)
                                                                    )
                                self.waveformPlotWidget.addItem(acoustic_landmark)
                self.sender().setStyleSheet("background-color : green; color= black")
                self.sender().setText("✔")
            else:
                self.sender().setChecked(False)
        elif self.sender().isChecked() == False:
            item_list = self.waveformPlotWidget.allChildItems()
            for i in range(len(item_list)):
                if isinstance(item_list[i],pg.InfiniteLine) and item_list[i] != self.locationLines["waveformPlotWidget"]:
                    self.waveformPlotWidget.removeItem(item_list[i])
            self.sender().setStyleSheet("background-color : light gray")
            self.sender().setText(" ")
  

    def eventFilter(self,source,evt):
       
        #if source == self and evt.type() == QEvent.Type.HoverMove:
        #    pos = self.mapToParent(evt.pos())
        #    w = qApp.widgetAt(pos)
        #    parent_widget_name = w.parentWidget().objectName()
        #    if parent_widget_name in self.pw_names:
        #        self.locationLines[parent_widget_name].show()
        #    else:
        #        for pw_name in self.pw_names: self.locationLines[pw_name].hide()
        
        if source == self and evt.type() == QEvent.MouseButtonPress:
            pos = self.mapToParent(evt.pos())
            w = qApp.widgetAt(pos)
            parent_widget_name = w.parentWidget().objectName()
            if parent_widget_name == "waveformPlotWidget":
                vb = w.parentWidget().getViewBox()
                position_on_widget = w.parentWidget().mapFromGlobal(pos)
                mouse_point = vb.mapSceneToView(position_on_widget)
                if self.LinearRegionItemRegister[parent_widget_name] == None:
                    self.LinearRegionItemRegister["waveformPlotWidget"] = pg.LinearRegionItem(values=(mouse_point.x(),mouse_point.x()))
                    w.parentWidget().addItem(self.LinearRegionItemRegister["waveformPlotWidget"])
                else:
                    w.parentWidget().removeItem(self.LinearRegionItemRegister["waveformPlotWidget"])
                    self.LinearRegionItemRegister["waveformPlotWidget"] = None
            elif self.selectRegionButton.isChecked() and parent_widget_name in list(self.LinearRegionItemRegister.keys())[1:]:
                vb = w.parentWidget().getViewBox()
                position_on_widget = w.parentWidget().mapFromGlobal(pos)
                mouse_point = vb.mapSceneToView(position_on_widget)
                if self.LinearRegionItemRegister[parent_widget_name] == None:
                    self.LinearRegionItemRegister[parent_widget_name] = pg.LinearRegionItem(values=(mouse_point.x(),mouse_point.x()))
                    w.parentWidget().addItem(self.LinearRegionItemRegister[parent_widget_name])
                else:
                    w.parentWidget().removeItem(self.LinearRegionItemRegister[parent_widget_name])
                    self.LinearRegionItemRegister[parent_widget_name] = None

        return super(inspector_window, self).eventFilter(source,evt)


    def movingMouse(self,evt):
        #print(self.mapFromGlobal(QCursor.pos()).x())
        pass

    def display_landmarks(self):
        name = self.sender().objectName() #replace with more efficient naming
        idx = int(self.sender().text())
        if self.sender().isChecked() and self.emaLandmarksComboBoxes[idx].currentText() != "new":
            current_text = self.emaLandmarksComboBoxes[idx].currentText()
            tmp_landmark_register = self.landmarkRegister[self.landmarkRegister["tierName"] == current_text].reset_index(drop=True)
            plt.add_landmarks_to_pw(self.emaPanelDict[idx]["PlotWidget"],tmp_landmark_register)
            self.sender().setStyleSheet("background-color: green")
        else:
            plt.remove_landmarks_from_pw(self.emaPanelDict[idx]["PlotWidget"])
            self.sender().setChecked(False)
            self.sender().setStyleSheet("background-color: light gray")


    def landmark_cmbbox_value_changed(self):
        name = self.sender().objectName() #replace with more efficient naming
        idx = int(name.replace("emaPanel","").replace("SelectTierComboBox",""))
        current_text = self.sender().currentText()
        if self.displayLandmarksCheckBoxes[idx].isChecked():
            plt.remove_landmarks_from_pw(self.emaPanelDict[idx]["PlotWidget"])
            tmp_landmark_register = self.landmarkRegister[self.landmarkRegister["tierName"] == current_text].reset_index(drop=True)
            plt.add_landmarks_to_pw(self.emaPanelDict[idx]["PlotWidget"],tmp_landmark_register)


    #def test_fun(self):
    #    keys = list(self.landmarkRegister.keys())
    #    for key in keys:
    #        print(key,self.landmarkRegister[key])

    def store_landmarks(self):
        for i in range(1,4):
            if self.displayLandmarksCheckBoxes[i].isChecked():
                if self.landmarksTierLineEdits[i].text() != "" and self.emaLandmarksComboBoxes[i].currentText() == "new":
                    tier_name = self.landmarksTierLineEdits[i].text()
                    self.landmarksTierLineEdits[i].setText("")
                else:
                    tier_name = self.emaLandmarksComboBoxes[i].currentText()

                tmp_lm = icoll.collect_landmarks(self.emaPanelDict[i]["PlotWidget"])
                tmp_landmark_register = pd.DataFrame(columns=["tierName","tmin","tmax","label"])
                for j in range(len(tmp_lm)):
                    landmark = pd.Series(index=tmp_landmark_register.columns)
                    
                    landmark["tierName"] = str(tier_name)
                    landmark["tmin"] = tmp_lm[j]["position"]
                    landmark["tmax"] = tmp_lm[j]["position"]
                    landmark["label"] = tmp_lm[j]["label"]
                    tmp_landmark_register.loc[len(tmp_landmark_register)] = landmark
                self.landmarkRegister = self.landmarkRegister[self.landmarkRegister["tierName"] != tier_name].drop_duplicates().reset_index(drop=True)
                self.landmarkRegister = pd.concat([self.landmarkRegister,tmp_landmark_register]).reset_index(drop=True)


        self.submitLandmarks.emit(self.landmarkRegister)
        self.update_landmark_comboboxes()
        tier_names = self.landmarkRegister["tierName"].unique()
        for j in range(len(tier_names)):
            index = self.emaLandmarksComboBoxes[j+1].findText(tier_names[j],Qt.MatchFixedString)
            self.emaLandmarksComboBoxes[j+1].setCurrentIndex(index)
        self.sender().setStyleSheet("background-color: light gray")
        msgBox_stored = QMessageBox()
        msgBox_stored.setIcon(QMessageBox.Information)
        msgBox_stored.setText("Landmarks stored")
        msgBox_stored.setStandardButtons(QMessageBox.Ok)
        msgBox_stored.exec()


    def update_landmark_comboboxes(self):
        tier_names = self.landmarkRegister["tierName"].unique()
        for i in range(0,4):
            cmbbox = self.emaLandmarksComboBoxes[i]
            cmbbox.clear()
            cmbbox.addItem("new")
            for tier_name in tier_names:
                cmbbox.addItem(tier_name)
                 


            
    def mouse_hover(self,evt):
        #if self.addLandmarkButton.isChecked() or self.renameLandmarkButton.isChecked() or self.removeLandmarkButton.isChecked() or self.selectRegionButton.isChecked():
        oname = self.sender().parent().objectName()
        scene_coords = evt
        vb = self.sender().parent().getViewBox()
        if self.sender().parent().sceneBoundingRect().contains(scene_coords):
            for pw_name in self.pw_names:
                self.locationLines[pw_name].show()
                mouse_loc = vb.mapSceneToView(scene_coords)
                self.locationLines[pw_name].setValue(mouse_loc)

    def item_added(self,item):
        if isinstance(item,pg.InfiniteLine):
            parent_name = self.sender().parent().objectName()
            panel_idx = int(list(parent_name)[-1])
            self.displayLandmarksCheckBoxes[panel_idx].setChecked(True)
            self.displayLandmarksCheckBoxes[panel_idx].setStyleSheet("background-color : green")
            
            #position = item.pos()
            ##label = item.label.format
            #if position not in self.landmarkRegister["tmin"].to_numpy():
            #    #parent_name = self.sender().parent().objectName()
            #    #panel_idx = int(list(parent_name)[-1])
            #    #parent_idx = int(list(parent_name)[-1])
            #    #ready_to_store = True
            #    #if self.emaLandmarksComboBoxes[parent_idx].currentText() != "":
            #    #    tier_name = self.emaLandmarksComboBoxes[parent_idx].currentText()
            #    #    tier_names = self.landmarkRegister["tierName"].unique()
            #    #    positions = [ position[0] == self.landmarkRegister[key][i]["position"] for i in range(len(tier_names))]
            #    #    if all(positions):
            #    #        ready_to_store = False
            #    #if ready_to_store == True:
            #    if self.displayLandmarksCheckBoxes[panel_idx].isChecked() == False:
            #        self.displayLandmarksCheckBoxes[panel_idx].setChecked(True)
            #        self.displayLandmarksCheckBoxes[panel_idx].setStyleSheet("background-color : green")
            #    self.storeLandmarksButton.setStyleSheet("background-color : red")
            

    
    def rename_landmarks(self,evt):
        if self.selectRegionButton.isChecked():
            pass
        elif self.renameLandmarkButton.isChecked():
            item_list = self.sender().itemsNearEvent(evt)
            for i in range(len(item_list)):
                if isinstance(item_list[i],pg.InfiniteLine) and hasattr(item_list[i],"label"):
                    infinite_line_item = item_list[i]
                    xpos = infinite_line_item.getXPos()
                    proceed, landmark_label = self.open_label_editor()
                    if proceed:
                        self.sender().parent().removeItem(infinite_line_item)
                        new_landmark_item = pg.InfiniteLine(
                                                    pos = xpos,
                                                    label = landmark_label,
                                                    movable = True,
                                                    pen = pg.mkPen("green",width=4),
                                                    labelOpts={"position" : 0.95}
                                                    )
                    self.sender().parent().addItem(new_landmark_item)

    def remove_landmarks(self,evt):
        if self.selectRegionButton.isChecked():
            for j in range(len(self.pw_names)):
                if "emaPlotWidget" in self.pw_names[j]:
                    emaPlotWidget_index = int(list(self.pw_names[j])[-1])
                    if self.LinearRegionItemRegister[self.pw_names[j]] != None:
                        boundaries = self.LinearRegionItemRegister[self.pw_names[j]].getRegion()
                        item_list = self.emaPanelDict[emaPlotWidget_index]["PlotWidget"].allChildItems()
                        for i in range(len(item_list)):
                            if isinstance(item_list[i],pg.InfiniteLine) and hasattr(item_list[i],"label"):
                                if item_list[i].value() > boundaries[0] and item_list[i].value() < boundaries[1]:
                                    self.emaPanelDict[emaPlotWidget_index]["PlotWidget"].removeItem(item_list[i])

        elif self.removeLandmarkButton.isChecked():
            item_list = self.sender().itemsNearEvent(evt)
            for i in range(len(item_list)):
                if isinstance(item_list[i],pg.InfiniteLine) and hasattr(item_list[i],"label"):
                    infinite_line_item = item_list[i]
                    self.sender().parent().removeItem(infinite_line_item)


    def activate_landmark_removal(self,evt):
        if self.selectRegionButton.isChecked():
            self.sender().setChecked(False)
            self.remove_landmarks(evt=evt)
        else:
            if self.sender().isChecked():
                self.sender().setStyleSheet("background-color : green")
                if self.addLandmarkButton.isChecked():
                    self.addLandmarkButton.click()
                if self.renameLandmarkButton.isChecked():
                    self.renameLandmarkButton.click()
            else:
                self.sender().setStyleSheet("background-color : light gray")

    def activate_landmark_renaming(self,evt):
        if self.selectRegionButton.isChecked():
            self.sender().setChecked(False)
        else:
            if self.sender().isChecked():
                self.sender().setStyleSheet("background-color : green")
                if self.removeLandmarkButton.isChecked():
                    self.removeLandmarkButton.click()
                if self.addLandmarkButton.isChecked():
                    self.addLandmarkButton.click()
            else:
                self.sender().setStyleSheet("background-color : light gray")

    def open_label_editor(self):
        label, ok  = QInputDialog.getText(self,"Label editor", "enter label:")
        return ok, label

    def add_landmarks(self,evt):
        if self.selectRegionButton.isChecked():
            # make landmark detection
            detection_algorithm = self.selectLandmarkDetectionComboBox.currentText()
            for i in range(len(self.pw_names)):
                if "emaPlotWidget" in self.pw_names[i]:
                    emaPlotWidget_index = int(list(self.pw_names[i])[-1])
                    if self.LinearRegionItemRegister[self.pw_names[i]] != None:
                        tmin, tmax = self.LinearRegionItemRegister[self.pw_names[i]].getRegion()
                        for j in range(self.emaControlTable.rowCount()):
                            panel_name = self.emaControlTable.cellWidget(j,4).currentText()
                            parameter = self.emaControlTable.cellWidget(j,3).currentText()
                            if panel_name == str(emaPlotWidget_index)+"a":
                                plot_checkbox = self.emaControlTable.cellWidget(j,0)
                                if plot_checkbox.isChecked():
                                    channel     = self.emaControlTable.cellWidget(j,1).currentText()
                                    dimension   = self.emaControlTable.cellWidget(j,2).currentText()
                                    parameter   = self.emaControlTable.cellWidget(j,3).currentText()
                                    panel       = self.emaControlTable.cellWidget(j,4).currentText()
                                    color       = self.emaControlTable.cellWidget(j,5).currentText()
                                    if parameter in ["pos","eucl2D","eucl3D"] and detection_algorithm in ["vel20","vel15"]:
                                        

                                        signal, _ = sp.get_signal(
                                                        data = self.data.ema,
                                                        channel_dict = self.channels,
                                                        target_channel = channel,
                                                        target_dimension = dimension,
                                                        target_parameter = parameter,
                                                        )
                                        
                                        velocity = sp.derivation(signal,ema_fs=self.data.ema.attrs["samplerate"],time=self.data.ema.time.values,order=1)
                                        if detection_algorithm == "vel20":
                                            landmarks = ldb.detect_landmarks_vel(time=self.data.ema.time.values,velocity=velocity,tmin=tmin,tmax=tmax,factor=0.2)
                                        elif detection_algorithm == "vel15":
                                            landmarks = ldb.detect_landmarks_vel(time=self.data.ema.time.values,velocity=velocity,tmin=tmin,tmax=tmax,factor=0.15)
                                        landmark_keys = list(landmarks.keys())
                                        for key in landmark_keys:
                                            infinite_line_item = pg.InfiniteLine(
                                                                                    pos = tmin + landmarks[key],
                                                                                    label = key,
                                                                                    movable = True,
                                                                                    pen = pg.mkPen("green",width=5),
                                                                                    labelOpts={"position":0.95}
                                                                                    )
                                            self.emaPanelDict[emaPlotWidget_index]["PlotWidget"].addItem(infinite_line_item)

                                    elif parameter == "pos" and detection_algorithm in ["tvel15_xy","tvel15_xz","tvel20_xy","tvel20_yz"]:
                                        dims = list(detection_algorithm.split("_")[1])
                                        tangential_velocity = sp.get_tangential_velocity(data=self.data.ema,channel_index=self.channels[channel],dims=dims)
                                        if "15" in detection_algorithm:
                                            factor = 0.15
                                        elif "20" in detection_algorithm:
                                            factor = 0.2
                                        landmarks = ldb.detect_landmarks_tvel(time=self.data.ema.time.values,tangential_velocity=tangential_velocity,tmin=tmin,tmax=tmax,factor=0.2)
                                        landmark_keys = list(landmarks.keys())
                                        for key in landmark_keys:
                                            infinite_line_item = pg.InfiniteLine(
                                                                                    pos = landmarks[key],
                                                                                    label = key,
                                                                                    movable = True,
                                                                                    pen = pg.mkPen("green",width=5),
                                                                                    labelOpts={"position":0.95}
                                                                                    )
                                            self.emaPanelDict[emaPlotWidget_index]["PlotWidget"].addItem(infinite_line_item)

        elif self.addLandmarkButton.isChecked():
            vb = self.sender().parent().getViewBox()
            scene_coords = evt.scenePos()
            if self.sender().parent().sceneBoundingRect().contains(scene_coords):
                mouse_point = vb.mapSceneToView(scene_coords)
                proceed, landmark_label = self.open_label_editor()
                if proceed:
                    landmark_item = pg.InfiniteLine(
                                                    pos = mouse_point.x(),
                                                    label = landmark_label,
                                                    movable = True,
                                                    pen = pg.mkPen("green",width=4),
                                                    labelOpts={"position" : 0.95}
                                                    )
                    self.sender().parent().addItem(landmark_item)
            


    def activate_landmark_addition(self,evt):
        if self.selectRegionButton.isChecked():
            self.sender().setChecked(False)
            self.add_landmarks(evt=evt)
        else:
            if self.sender().isChecked():
                self.sender().setStyleSheet("background-color : green")
                if self.removeLandmarkButton.isChecked():
                    self.removeLandmarkButton.click()
                if self.renameLandmarkButton.isChecked():
                    self.renameLandmarkButton.click()


            else:
                self.sender().setStyleSheet("background-color : light gray")

    


    def select_region_activation(self):
        """
            Signals the activation of the linear region items for the ema panels.
            If buttons for adding, removing or renaming landmarks are activated, they will be set to False and background color is  reset to light gray.
            If the select region function is deactivated, LinearRegionItems are removed.
        """
        if self.sender().isChecked():
            self.sender().setStyleSheet("background-color : green")
            if self.removeLandmarkButton.isChecked():
                    self.removeLandmarkButton.setChecked(False)
                    self.removeLandmarkButton.setStyleSheet("background-color : light gray")
            if self.renameLandmarkButton.isChecked():
                    self.renameLandmarkButton.setChecked(False)
                    self.renameLandmarkButton.setStyleSheet("background-color : light gray")
            if self.addLandmarkButton.isChecked():
                    self.addLandmarkButton.setChecked(False)    
                    self.addLandmarkButton.setStyleSheet("background-color : light gray")        
        else:
            self.sender().setStyleSheet("background-color : light gray")
            for i in range(len(self.pw_names)):
                if "emaPlotWidget" in self.pw_names[i]:
                    emaPlotWidget_index = int(list(self.pw_names[i])[-1])
                    if self.LinearRegionItemRegister[self.pw_names[i]] != None:
                        self.emaPanelDict[emaPlotWidget_index]["PlotWidget"].removeItem(self.LinearRegionItemRegister[self.pw_names[i]])
                        self.LinearRegionItemRegister[self.pw_names[i]] = None
        

    def plot_trajectory(self,button_index=None):
        button = qApp.focusWidget()
        index = self.emaControlTable.indexAt(button.pos()).row()
        if button_index != None:
            index = button_index
        is_plotted = False
        panel_to_plot = self.emaControlTable.cellWidget(index,4).currentText()
        
        tmp_panel_array = [self.emaControlTable.cellWidget(i,4).currentText() for i in range(self.emaControlTable.rowCount())]
        
        if button.isChecked() and tmp_panel_array.count(panel_to_plot) == 1:
            channel     = self.emaControlTable.cellWidget(index,1).currentText()
            dimension   = self.emaControlTable.cellWidget(index,2).currentText()
            parameter   = self.emaControlTable.cellWidget(index,3).currentText()
            panel       = self.emaControlTable.cellWidget(index,4).currentText()
            color       = self.emaControlTable.cellWidget(index,5).currentText()
            signal, label = sp.get_signal(
                                                data = self.data.ema,
                                                channel_dict = self.channels,
                                                target_channel = channel,
                                                target_dimension = dimension,
                                                target_parameter = parameter,
                                            )
            is_plotted = plt.plot_ema_trajectory(
                                                data = self.data.ema,
                                                panels = self.emaPanelDict,
                                                signal = signal,
                                                target_panel = panel,
                                                color = color,
                                                label = label
                                                )
            
            #self.emaControlTable.item(index.row(),0).setBackground(QColor(color))
            
            if is_plotted:
                button.setChecked(is_plotted)
                button.setStyleSheet("background-color:"+color)
                button.setText("✔")
        elif tmp_panel_array.count(panel_to_plot) > 1:
            button.setChecked(False)
        else:
            panel       = self.emaControlTable.cellWidget(index,4).currentText()
            plt.remove_ema_trajectory(panels=self.emaPanelDict,target_panel=panel)
            button.setChecked(False)
            button.setStyleSheet("background-color: light gray")
            button.setText(" ")



    def addChannelToEmaControlTable(self):
        number_of_rows = self.emaControlTable.rowCount()
        self.emaControlTable.insertRow(number_of_rows)

        # get channel denominations
        channel_list = list(self.channels.keys())
        channel_list1 = channel_list.copy()
        channel_list2 = channel_list.copy()
        # update channel list
        for i in range(len(channel_list1)):
            for j in range(len(channel_list2)):
                if channel_list[i] != channel_list1[j] and channel_list1[j] + "+" + channel_list2[i] not in channel_list: channel_list.append(channel_list1[i] + "+" + channel_list2[j])

        # channel selection
        channelSelectionComboBox = QComboBox()
        for i in range(len(channel_list)): channelSelectionComboBox.addItem(channel_list[i])
        self.emaControlTable.setCellWidget(number_of_rows,1,channelSelectionComboBox)

        # dimension selection
        dimensionSelectionComboBox = QComboBox()
        dimensions = self.data.ema.dimensions.values[:3].tolist() + ["x+y","x+z","y+z"]
        for i in range(len(dimensions)): dimensionSelectionComboBox.addItem(dimensions[i])
        self.emaControlTable.setCellWidget(number_of_rows,2,dimensionSelectionComboBox)

        # parameter selection
        parameterSelectionComboBox = QComboBox()
        params = ["pos","vel","acc","tanvel","eucl2D","eucl3D","dist"]
        for i in range(len(params)): parameterSelectionComboBox.addItem(params[i])
        self.emaControlTable.setCellWidget(number_of_rows,3,parameterSelectionComboBox)

        # panel selection
        panelSelectionComboBox = QComboBox()
        panels = ["1a","1b","1c","2a","2b","2c","3a","3b","3c"]
        for i in range(len(panels)): panelSelectionComboBox.addItem(panels[i])
        self.emaControlTable.setCellWidget(number_of_rows,4,panelSelectionComboBox)

        # color selection
        colorSelectionComboBox = QComboBox()
        colors = ["lightcoral","red","salmon","lightsalmon","sandybrown","peachpuff","antiquewhite","gold","yellow","greenyellow","palegreen","lime","turquoise","cyan","lightskyblue","lavender","plum","fuchsia","crimson"]
        for i in range(len(colors)): 
            item = QStandardItem(colors[i])
            item.setBackground(QColor(colors[i]))
            item.setForeground(QColor("black"))
            colorSelectionComboBox.model().appendRow(item)
        self.emaControlTable.setCellWidget(number_of_rows,5,colorSelectionComboBox)
        self.emaControlTable.cellWidget(number_of_rows,5).setStyleSheet("background-color: lightcoral; color: black")
        self.emaControlTable.cellWidget(number_of_rows,5).currentTextChanged.connect(self.color_selection)

        plot_button = QPushButton(" ")
        plot_button.setCheckable(True)
        plot_button.clicked.connect(lambda: self.plot_trajectory())
        self.emaControlTable.setCellWidget(number_of_rows,0,plot_button)
        
        
    def color_selection(self):
        self.sender().setStyleSheet("background-color:"+self.sender().currentText()+"; color: black")


    def sliderMovePlot(self):
        #get current xmin
        xmin,xmax = self.waveformPlotWidget.getViewBox().viewRange()[0]
        slider_value = self.sender().value()
        mid = (xmin + xmax)/2
        half = np.abs(mid - xmin)
        max_slider_value = self.sender().maximum()
        new_value = ((slider_value - 0)*(self.data.audio.time.values[-1]))/(max_slider_value)
        self.waveformPlotWidget.getViewBox().setXRange(new_value-half,new_value+half,padding=0.0,update=True)
        self.update_plot()
        if self.sender().objectName() == "waveformSlider":
            self.waveformSlider_2.setValue(slider_value)
        else:
            self.waveformSlider.setValue(slider_value)

    # function for zoom control

    def zoom_all(self):
        time = self.data.audio.time.values
        self.waveformPlotWidget.getViewBox().setXRange(time[0],time[-1],padding=0.0,update=True)
        self.waveformSlider.setMaximum(0)
        self.waveformSlider_2.setMaximum(0)
        self.update_plot()

    def zoom_selection(self):
        if isinstance(self.LinearRegionItemRegister["waveformPlotWidget"],pg.LinearRegionItem):
            audio_range = np.abs(self.data.audio.time.values[0] - self.data.audio.time.values[-1])
            boundaries = self.LinearRegionItemRegister["waveformPlotWidget"].getRegion()
            mid = (boundaries[0] + boundaries[1])/2 
            
            self.waveformPlotWidget.getViewBox().setXRange(boundaries[0],boundaries[1],padding=0.0,update=True)
            xRange, _ = self.waveformPlotWidget.getViewBox().viewRange()
            boundary_range = np.abs(xRange[0] - xRange[1])
            slider_steps = int(audio_range/boundary_range)*100
            
            self.waveformSlider.setMaximum(slider_steps)
            self.waveformSlider_2.setMaximum(slider_steps)
            mid = (xRange[0]+xRange[1])/2
            slider_location = int(((mid - 0)*(slider_steps))/(self.data.audio.time.values[-1]))
            self.waveformSlider.setValue(slider_location)
            self.waveformSlider_2.setValue(slider_location)

    def zoom(self,direction):
        s = 0.9
        audio_range = np.abs(self.data.audio.time.values[0] - self.data.audio.time.values[-1])

        x1, x2 = self.waveformPlotWidget.getViewBox().viewRange()[0]
        mid = (x1+x2)/2
        
        if direction == "in":
            self.waveformPlotWidget.getViewBox().scaleBy(center=mid,x=s)
        elif direction == "out":
            self.waveformPlotWidget.getViewBox().scaleBy(center=mid,x=1/s)
        self.update_plot()
        xRange, _ = self.waveformPlotWidget.getViewBox().viewRange()
        boundary_range = np.abs(xRange[0] - xRange[1])
        slider_steps = int(audio_range/boundary_range)*100
        self.waveformSlider.setMaximum(slider_steps)
        self.waveformSlider_2.setMaximum(slider_steps)
        mid = (xRange[0]+xRange[1])/2
        slider_location = round(((mid - 0)*(slider_steps))/(self.data.audio.time.values[-1]))
        self.waveformSlider.setValue(slider_location)
        self.waveformSlider_2.setValue(slider_location)


    def update_plot(self):
        left_boundary, right_boundary = self.waveformPlotWidget.getViewBox().viewRange()[0]
        left_boundary_index = np.abs(left_boundary - self.data.audio.time.values).argmin()
        right_boundary_index = np.abs(right_boundary - self.data.audio.time.values).argmin()
        items = self.waveformPlotWidget.allChildItems()
        for item in items:
            if isinstance(item,pg.PlotDataItem):
                item.setData(self.data.audio.time.values[left_boundary_index:right_boundary_index],
                             self.data.audio.signal.values[left_boundary_index:right_boundary_index])
        #number_of_rows = self.emaControlTable.rowCount()
        #for i in range(number_of_rows):
        #    if self.emaControlTable.cellWidget(i,0).isChecked():
        #        channel     = self.emaControlTable.cellWidget(i,1).currentText()
        #        dimension   = self.emaControlTable.cellWidget(i,2).currentText()
        #        parameter   = self.emaControlTable.cellWidget(i,3).currentText()
        #        panel       = self.emaControlTable.cellWidget(i,4).currentText()
        #        color       = self.emaControlTable.cellWidget(i,5).currentText()
        #        signal, label = utils.get_signal(
        #                                            data = self.data.ema,
        #                                            channel_dict = self.channels,
        #                                            target_channel = channel,
        #                                            target_dimension = dimension,
        #                                            target_parameter = parameter,
        #                                        )
        #        panel, axis = int(list(target_panel)[0]), list(target_panel)[-1]
        #        items = self.emaPanelDict[panel]["axes"][panel]["viewbox"].allChildItems()
        #        for item in items:
        #            if isinstance(item,pg.PlotDataItem):
        #                item.setData(self.data.ema.time.values[left_boundary_index:right_boundary_index],
        #                            signal[left_boundary_index:right_boundary_index])











    #def update_slider(self):
    #    left_boundary, right_boundary = self.waveformPlotWidget.getViewBox().viewRange()[0]
    #    minrange, maxrange = self.data.audio.time.values[0]-0.1, self.data.audio.time.values[-1]+0.1
    #    data_range = np.abs(minrange - maxrange)
    #    viewbox_range = np.abs(left_boundary - right_boundary)
    #    num_steps = data_range / viewbox_range
    #    num_steps = int(num_steps)
    #    self.waveformSlider.setMaximum(num_steps)
    #    self.waveformSlider_2.setMaximum(num_steps)

    def initialize_ema_axes(self,plotWidget):

        #code from multiple axes exampleswerafderadferdf

        p1 = plotWidget.plotItem
        p1.getViewBox().setXLink(self.waveformPlotWidget)
        p2 = pg.ViewBox()
        p2.setMouseEnabled(x=False,y=False)
        p1.showAxis("right")
        p1.scene().addItem(p2)
        p1.getAxis("right").linkToView(p2)
        p2.setXLink(self.waveformPlotWidget)
        p3 = pg.ViewBox()
        p3.setMouseEnabled(x=False,y=False)
        ax3 = pg.AxisItem("right")
        p1.layout.addItem(ax3,2,3)
        p1.scene().addItem(p3)
        ax3.linkToView(p3)
        p3.setXLink(self.waveformPlotWidget)

        def updateViews():
            p2.setGeometry(p1.vb.sceneBoundingRect())
            p3.setGeometry(p1.vb.sceneBoundingRect())
            p2.linkedViewChanged(p1.vb, p2.XAxis)
            p3.linkedViewChanged(p1.vb, p3.XAxis)
        updateViews()
        p1.vb.sigResized.connect(updateViews)
        axes = {
                "a" : {
                            "viewbox": p1,
                            "axis" : p1.getAxis("left"),
                            "occupied" : False
                        },
                "b" : {
                            "viewbox" : p2,
                            "axis" : p1.getAxis("right"),
                            "occupied" : False
                        },
                "c" : {
                            "viewbox" : p3,
                            "axis" : ax3,
                            "occupied" : False

                        }
            }
        
        return axes

    def show_ema_panel(self):
        panel_number = int(self.sender().objectName().replace("displayEmaPanel","").replace("PushButton",""))
        if self.sender().isChecked():
            self.emaPanelDict[panel_number]["Panel"].show()
            self.sender().setStyleSheet("background-color : green")
        else:
            self.sender().setStyleSheet("background-color : light gray")
            self.emaPanelDict[panel_number]["Panel"].hide()

    def plot_audio_waveform(self):
        self.waveformPlotWidget.plot(
                                        self.data.audio.time.values,
                                        self.data.audio.signal.values
                                    )
        self.waveformPlotWidget.setLimits(
                                            xMin = self.data.audio.time.values[0],
                                            xMax = self.data.audio.time.values[-1]
                                        )
        font = QFont("Helvetica",8)
        self.waveformPlotWidget.getAxis("left").setLabel(text="Amplitude",color="white")
        self.waveformPlotWidget.getAxis("left").label.setFont(font)

"""
### for testing
path = ""
posfile = path + "0005.pos"
wavfile = path + "0005.wav"
tgfile = path + "0005.TextGrid"

dat = data_import.dataContainer()
dat.ema = data_import.read_AG50x(posfile)
dat.audio = data_import.read_wav(wavfile)

dat.annotation = data_import.read_TextGrid(tgfile)
channels = {
    "TBO": 2,
    "TMID": 3,
    "TTIP" : 4,
    "ULIP" : 5,
    "LLIP" : 6
}
tier_list = []
#print(dat.annotation)
app = QApplication(sys.argv)
w = inspector_window(dat,channels,tier_list)
w.show()
sys.exit(app.exec_())
"""