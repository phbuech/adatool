import os
import sys
import io
import numpy as np
import pandas as pd

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

from ui_inspector2D import Ui_INSPECTOR2D
#import inspector_plotting as iplt



import pyqtgraph as pg
import scipy as scp

#load internal modules
import data_import
import plotting as plt
import information_collection as icoll
import signal_processing as sp
import landmark_detection_backend as ldb

import sounddevice as sd
from scipy.interpolate import CubicSpline

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

class inspector2D_window(QMainWindow, Ui_INSPECTOR2D):

    def __init__(self, transmittedData,transmittedChannelAllocation,transmittedTierList):
        super().__init__()
        self.setupUi(self)

        
        self.data = transmittedData
        self.channels = transmittedChannelAllocation
        self.tierList = transmittedTierList

        self.plot_audio_waveform()
        self.waveformPlotWidget.setMouseEnabled(x=False,y=False)

        self.waveformSplitter.splitterMoved.connect(self.movingSplitter)
        self.emaSplitter.splitterMoved.connect(self.movingSplitter)

        self.emaPlotWidget1.disableAutoRange()
        self.emaPlotWidget1.setMouseEnabled(x=False,y=False)


        self.spectrogramFrame.hide()
        self.showSpectrogramButton.clicked.connect(self.show_spectrogram)
        self.spectrogramWidget.setMouseEnabled(x=False,y=False)
        self.plot_spectrogram()
        self.spectrogramWidget.setXLink(self.waveformPlotWidget)


        


        try:
            if self.data.annotation is not None:
                tiers = self.data.annotation["tierName"].unique()
                for i in range(len(tiers)): 
                    if tiers[i] not in self.tierList:
                        self.audioAnnotationComboBox.addItem(tiers[i])
        except:
            pass
        self.displayAnnotationPushButton.clicked.connect(self.displayAudioAnnotations)

        for i in range(len(self.data.ema.dimensions.values)): self.selectDimensionComboBox1.addItem(self.data.ema.dimensions.values[i])
        for i in range(len(self.data.ema.dimensions.values)): self.selectDimensionComboBox2.addItem(self.data.ema.dimensions.values[i])

        self.emaControlTable.setColumnCount(4)
        self.emaControlTable.setHorizontalHeaderLabels(["PLOT","CHAN","COLOR","TONGUE"])
        emaControlTableHeader = self.emaControlTable.horizontalHeader()
        for i in range(4): emaControlTableHeader.setSectionResizeMode(i,QHeaderView.ResizeMode.Stretch)

        self.addChannelToEmaControlTableButton.clicked.connect(self.addChannelToEmaControlTable)
        self.removeChannelFromEmaControlTableButton.clicked.connect(self.removeChannelFromEmaControlTable)

        self.scatterPlotItemRegister = {}
        self.locationLine = pg.InfiniteLine(pos=0,pen=pg.mkPen("white",width=2),movable=False)
        self.waveformPlotWidget.addItem(self.locationLine)
        self.locationLine.setPos(0)
        #self.locationLine.sigPositionChanged(self.lineLocationChanged)
        self.installEventFilter(self)
        self.dataRegister = {}
        self.LinearRegionItem = None

        self.zoomInButton.clicked.connect(lambda: self.zoom("in"))
        self.zoomOutButton.clicked.connect(lambda: self.zoom("out"))

        self.PLAY_AUDIO.clicked.connect(self.play_audio)

        self.addLabelsPushButton.clicked.connect(self.displayLabels)

        self.scatterLabelRegister = {}

        self.selectDimensionComboBox1.currentTextChanged.connect(self.updateRange)
        self.selectDimensionComboBox2.currentTextChanged.connect(self.updateRange)

        self.tongueSensorRegister = {}
        self.curveItemRegister = {}
        self.tongueShapeCurve = None
        self.plotTongueShapePushButton.clicked.connect(self.plot_tongue_shape)
        self.waveformSlider.setMaximum(0)
        self.waveformSlider.valueChanged.connect(self.sliderMovePlot)

        self.plotTracePushButton.clicked.connect(self.activate_button)
        self.plotTongueShapePushButton.clicked.connect(self.activate_button)
        self.sizeSlider.valueChanged.connect(self.on_size_change)

        self.zoomSelectionButton.clicked.connect(self.zoom_selection)
        self.zoomAllButton.clicked.connect(self.zoom_all)

        self.showFundamentalFrequencyButton.clicked.connect(self.plot_fundamental_frequency)
        self.showIntensityButton.clicked.connect(self.plot_intensity)
        self.showFundamentalFrequencyButton.setText(" ")
        self.showIntensityButton.setText(" ")
        self.displayAnnotationPushButton.setText(" ")
        self.showSpectrogramButton.click()

        #create 2nd spectrogram axis
        self.specgram_2nd_axis = pg.ViewBox()
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

    def on_size_change(self):
        #change sensor position size
        size = self.sender().value()
        number_of_rows = self.emaControlTable.rowCount()
        for row_idx in range(number_of_rows):
            channel_name = self.emaControlTable.cellWidget(row_idx,1).currentText()
            color_name = self.emaControlTable.cellWidget(row_idx,2).currentText()
            if self.emaControlTable.cellWidget(row_idx,0).isChecked():
                #self.scatterLabelRegister[channel_name].setScale(size)
                self.scatterPlotItemRegister[channel_name].setPen(color=color_name,width=size/4)
            if self.addLabelsPushButton.isChecked():
                fn = QFont()
                fn.setBold(True)
                fn.setPointSize(size/2)
                self.scatterLabelRegister[channel_name].setFont(fn)


    def activate_button(self):
        if self.sender().isChecked():
            self.sender().setStyleSheet("background-color : green")
        else:
            self.sender().setStyleSheet("background-color : light gray")
        
    def plot_tongue_shape(self):
        #collect tongue shape
        number_of_rows = self.emaControlTable.rowCount()
        for i in range(number_of_rows):
            item = self.emaControlTable.cellWidget(i,3)
            if item.isChecked():
                channel_name = self.emaControlTable.cellWidget(i,1).currentText()
                self.tongueSensorRegister[channel_name] = True
        if self.plotTongueShapePushButton.isChecked():
                self.tongueShapeCurve = pg.PlotCurveItem(pen=pg.mkPen("white",width=2, style=Qt.DashLine))
                self.tongueShapeCurve.hide()
                self.emaPlotWidget1.addItem(self.tongueShapeCurve)

    def updateRange(self):
        
        dim1_name = self.selectDimensionComboBox1.currentText()
        dim2_name = self.selectDimensionComboBox2.currentText()
        tmp_min_dim1 = []
        tmp_max_dim1 = []
        tmp_min_dim2 = []
        tmp_max_dim2 = []
        channel_values = list(self.channels.values())
        for key in channel_values:
            tmp_min_dim1.append(self.data.ema.sel(channels=key).sel(dimensions=dim1_name).ema.values.min())
            tmp_max_dim1.append(self.data.ema.sel(channels=key).sel(dimensions=dim1_name).ema.values.max())
            tmp_min_dim2.append(self.data.ema.sel(channels=key).sel(dimensions=dim2_name).ema.values.min())
            tmp_max_dim2.append(self.data.ema.sel(channels=key).sel(dimensions=dim2_name).ema.values.max())
        dim1_minimum = np.min(tmp_min_dim1)
        dim1_maximum = np.max(tmp_max_dim1)
        dim2_minimum = np.min(tmp_min_dim2)
        dim2_maximum = np.max(tmp_max_dim2)
        dim1_cent = np.abs(dim1_minimum-dim1_maximum)*0.1
        dim2_cent = np.abs(dim2_minimum-dim2_maximum)*0.1
        self.emaPlotWidget1.setRange(
                        xRange = (dim2_maximum+dim1_cent,dim1_minimum-dim1_cent),
                        yRange = (dim2_minimum-dim2_cent,dim2_maximum+dim2_cent)
                    )


    def displayLabels(self):
        
        number_of_rows = self.emaControlTable.rowCount()
        if self.sender().isChecked():
            self.sender().setStyleSheet("background-color : green")
        else:
            self.sender().setStyleSheet("background-color : light gray")
        for row_idx in range(number_of_rows):
            channel_name = self.emaControlTable.cellWidget(row_idx,1).currentText()
            color_name = self.emaControlTable.cellWidget(row_idx,2).currentText()
            if self.sender().isChecked():
                if self.emaControlTable.cellWidget(row_idx,0).isChecked():
                    scatterKeys = list(self.scatterLabelRegister.keys())
                    if channel_name not in scatterKeys:
                        self.scatterLabelRegister[channel_name] = pg.TextItem(
                                                                                text=channel_name,
                                                                                anchor=(0,0)
                                                                                )
                        self.scatterLabelRegister[channel_name].setColor(color_name)
                        dim1, dim2 = self.scatterPlotItemRegister[channel_name].getData()[0],self.scatterPlotItemRegister[channel_name].getData()[1]
                        fn = QFont()
                        fn.setBold(True)
                        fn.setPointSize(int(self.sizeSlider.value()))

                        self.scatterLabelRegister[channel_name].setFont(fn)
                        self.scatterLabelRegister[channel_name].setPos(
                                                                        dim1,
                                                                        dim2
                                                                    )
                        self.emaPlotWidget1.addItem(self.scatterLabelRegister[channel_name])
            else:
                if self.emaControlTable.cellWidget(row_idx,0).isChecked():
                    scatterKeys = list(self.scatterLabelRegister.keys())
                    if channel_name in scatterKeys:
                        self.emaPlotWidget1.removeItem(self.scatterLabelRegister[channel_name])
                        self.scatterLabelRegister.pop(channel_name)


    def play_audio(self):
        if isinstance(self.LinearRegionItem,pg.LinearRegionItem):
            x = self.LinearRegionItem.getRegion()
            xmin = np.abs(self.data.audio.time.values-x[0]).argmin()
            xmax = np.abs(self.data.audio.time.values-x[1]).argmin()
            snippet = self.data.audio.signal.values[xmin:xmax]
            sr = self.data.audio.attrs["samplerate"]
            sd.play(snippet,sr)
            




    def eventFilter(self,source,evt):
       
        if source == self and evt.type() == QEvent.Type.HoverMove:
            pos = self.mapToParent(evt.pos())
            w = qApp.widgetAt(pos)
            parent_widget_name = w.parentWidget().objectName()
            if parent_widget_name == "waveformPlotWidget":
                vb = w.parentWidget().getViewBox()
                position_on_widget = w.parentWidget().mapFromGlobal(pos)
                mouse_point = vb.mapSceneToView(position_on_widget)
                self.locationLine.setValue(mouse_point.x())
                self.lineLocationChanged(mouse_point.x())
                
        if source == self and evt.type() == QEvent.MouseButtonPress:
            pos = self.mapToParent(evt.pos())
            w = qApp.widgetAt(pos)
            parent_widget_name = w.parentWidget().objectName()
            if parent_widget_name == "waveformPlotWidget":
                vb = w.parentWidget().getViewBox()
                position_on_widget = w.parentWidget().mapFromGlobal(pos)
                mouse_point = vb.mapSceneToView(position_on_widget)
                if self.LinearRegionItem == None:
                    self.LinearRegionItem = pg.LinearRegionItem(values=(mouse_point.x(),mouse_point.x()))
                    self.waveformPlotWidget.addItem(self.LinearRegionItem)
                else:
                    self.waveformPlotWidget.removeItem(self.LinearRegionItem)
                    self.LinearRegionItem = None
        
        return super(inspector2D_window, self).eventFilter(source,evt)


    def lineLocationChanged(self,coord):
        tmp_tongueShape = []
        if len(self.scatterPlotItemRegister) != 0:
            keys = list(self.scatterPlotItemRegister.keys())
            for key in keys:
                new_coord_index = np.abs(coord - self.dataRegister[key]["time"]).argmin()
                dim1_new = self.dataRegister[key]["dim1"][new_coord_index]
                dim2_new = self.dataRegister[key]["dim2"][new_coord_index]
                self.scatterPlotItemRegister[key].setData(
                                                            x = [dim1_new],
                                                            y = [dim2_new]
                                                        )
                if key in list(self.scatterLabelRegister.keys()):
                    self.scatterLabelRegister[key].setPos(
                                                                dim1_new,
                                                                dim2_new
                                                            )
                if self.LinearRegionItem is not None:
                    if self.plotTracePushButton.isChecked():
                        xmin, xmax = self.LinearRegionItem.getRegion()
                        if coord > xmin and coord < xmax:
                            xmin_idx = np.abs(xmin - self.data.ema.time.values).argmin()
                            dim1_curve = self.dataRegister[key]["dim1"][xmin_idx:new_coord_index]
                            dim2_curve = self.dataRegister[key]["dim2"][xmin_idx:new_coord_index]
                            self.curveItemRegister[key].setData(x=dim1_curve,y=dim2_curve)
                            self.curveItemRegister[key].show()
                        else:
                            self.curveItemRegister[key].hide()
                    else:
                        self.curveItemRegister[key].hide()
                else:
                        self.curveItemRegister[key].hide()
                if self.plotTongueShapePushButton.isChecked():
                    if key in list(self.tongueSensorRegister.keys()):
                        tmp_tongueShape.append(np.array([dim1_new,dim2_new]))
            if self.plotTongueShapePushButton.isChecked():
                tmp_tongueShape = np.array(tmp_tongueShape)
                sorted_ts = tmp_tongueShape[tmp_tongueShape[:,0].argsort()]
                cs = CubicSpline(sorted_ts[:,0],sorted_ts[:,1])
                xmin, xmax = sorted_ts[:,0].min(), sorted_ts[:,0].max()
                xnew = np.linspace(xmin,xmax,20)
                self.tongueShapeCurve.setData(x=xnew,y=cs(xnew))
                self.tongueShapeCurve.show()
            else:
                self.tongueShapeCurve.hide()


                
                    


    def plotChannel(self,button_index=None):
        button = qApp.focusWidget()
        index = self.emaControlTable.indexAt(button.pos()).row()
        if button_index != None:
            index = button_index
        channel_name = self.emaControlTable.cellWidget(index,1).currentText()
        if button.isChecked():
            
            position = self.locationLine.value()
            position_index = np.abs(position - self.data.ema.time.values).argmin()
            color_name = self.emaControlTable.cellWidget(index,2).currentText()
            channel_index = self.channels[channel_name]
            dim1_name = self.selectDimensionComboBox1.currentText()
            dim2_name = self.selectDimensionComboBox2.currentText()
            dim1 = self.data.ema.sel(channels=channel_index).sel(dimensions=dim1_name).ema.values
            dim2 = self.data.ema.sel(channels=channel_index).sel(dimensions=dim2_name).ema.values
            self.dataRegister[channel_name] = {
                                                "dim1" : dim1,
                                                "dim2" : dim2,
                                                "time" : self.data.ema.time.values
                                            }
            size = int(self.sizeSlider.value())
            self.scatterPlotItemRegister[channel_name] = pg.ScatterPlotItem(size=size/4,pen=pg.mkPen(color_name),brush=pg.mkBrush(color_name))
            self.scatterPlotItemRegister[channel_name].setData(
                                                                x = [self.dataRegister[channel_name]["dim1"][position_index]],
                                                                y = [self.dataRegister[channel_name]["dim2"][position_index]]  
                                                            )
            self.curveItemRegister[channel_name] = pg.PlotCurveItem(pen=pg.mkPen(color_name,width=size/4))
            #self.curveItemRegister[channel_name].hide()
            self.emaPlotWidget1.addItem(self.curveItemRegister[channel_name])
            self.emaPlotWidget1.addItem(self.scatterPlotItemRegister[channel_name])
            
            button.setStyleSheet("background-color:"+color_name)
            button.setText("✔")
            
        else:
            self.emaPlotWidget1.removeItem(self.scatterPlotItemRegister[channel_name])
            self.emaPlotWidget1.removeItem(self.curveItemRegister[channel_name])
            self.emaPlotWidget1.removeItem(self.tongueShapeCurve)
            if self.addLabelsPushButton.isChecked():
                self.emaPlotWidget1.removeItem(self.scatterLabelRegister[channel_name])
            if self.plotTongueShapePushButton.isChecked() == False:
                self.emaPlotWidget1.removeItem(self.tongueShapeCurve)
                self.tongueShapeCurve = None
            self.scatterPlotItemRegister.pop(channel_name)
            self.dataRegister.pop(channel_name)
            button.setStyleSheet("background-color: light gray")
            button.setText("")


        

    def addChannelToEmaControlTable(self):
        number_of_rows = self.emaControlTable.rowCount()
        self.emaControlTable.insertRow(number_of_rows)
        channel_list = list(self.channels.keys())

        #add plot button
        plot_button = QPushButton(self.emaControlTable)
        plot_button.setCheckable(True)
        plot_button.clicked.connect(lambda: self.plotChannel())
        self.emaControlTable.setCellWidget(number_of_rows,0, plot_button)


        # channel selection
        channelSelectionComboBox = QComboBox()
        for i in range(len(channel_list)): channelSelectionComboBox.addItem(channel_list[i])
        self.emaControlTable.setCellWidget(number_of_rows,1,channelSelectionComboBox)

        # color selection
        colorSelectionComboBox = QComboBox()
        colors = ["lightcoral","red","salmon","lightsalmon","sandybrown","peachpuff","antiquewhite","gold","yellow","greenyellow","palegreen","lime","turquoise","cyan","lightskyblue","lavender","plum","fuchsia","crimson"]
        for i in range(len(colors)): 
            item = QStandardItem(colors[i])
            item.setBackground(QColor(colors[i]))
            item.setForeground(QColor("black"))
            colorSelectionComboBox.model().appendRow(item)
        self.emaControlTable.setCellWidget(number_of_rows,2,colorSelectionComboBox)
        self.emaControlTable.cellWidget(number_of_rows,2).setStyleSheet("background-color: lightcoral; color: black")
        self.emaControlTable.cellWidget(number_of_rows,2).currentTextChanged.connect(self.color_selection)

        #plot item
        # https://stackoverflow.com/questions/56102229/how-to-remove-label-from-dynamically-generated-check-box-in-pyqt5
        
        tongue_button = QPushButton(self.emaControlTable)
        tongue_button.setCheckable(True)
        tongue_button.clicked.connect(self.activate_istongue)
        self.emaControlTable.setCellWidget(number_of_rows,3,tongue_button)

    def activate_istongue(self):
        if self.sender().isChecked():
            self.sender().setText("✔")
            self.sender().setStyleSheet("background-color : green")
        else:
            self.sender().setText("")
            self.sender().setStyleSheet("background-color : light gray")

    def color_selection(self):
        self.sender().setStyleSheet("background-color:"+self.sender().currentText()+"; color: black")

    def removeChannelFromEmaControlTable(self):
        current_row = self.emaControlTable.currentRow()
        if current_row == -1:
            current_row = self.emaControlTable.rowCount() -1
        plot_checkbox = self.emaControlTable.cellWidget(current_row,0)
        if plot_checkbox.isChecked():
            plot_checkbox.click(button_index=current_row)
        self.emaControlTable.removeRow(current_row)

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
                self.sender().setText("✔")
                self.sender().setStyleSheet("background-color : green")
        elif self.sender().isChecked() == False:
            item_list = self.waveformPlotWidget.allChildItems()
            for i in range(len(item_list)):
                if isinstance(item_list[i],pg.InfiniteLine):
                    self.waveformPlotWidget.removeItem(item_list[i])
            self.sender().setStyleSheet("background-color : light gray")
            self.sender().setText(" ")

    def movingSplitter(self,pos,index):
        if self.sender().objectName() == "waveformSplitter":
            self.emaSplitter.moveSplitter(pos,index)
        elif self.sender().objectName() == "emaSplitter":
            self.waveformSplitter.moveSplitter(pos,index)

    def plot_audio_waveform(self):
        self.waveformPlotWidget.plot(
                                        self.data.audio.time,
                                        self.data.audio.signal
                                    )
        self.waveformPlotWidget.setLimits(
                                            xMin = self.data.audio.time[0],
                                            xMax = self.data.audio.time[-1]
                                        )


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
        self.waveformSlider.setValue(slider_value)

    # function for zoom control
    def zoom_all(self):
        time = self.data.audio.time.values
        self.waveformPlotWidget.getViewBox().setXRange(time[0],time[-1],padding=0.0,update=True)
        self.waveformSlider.setMaximum(0)
        self.update_plot()

    def zoom_selection(self):
        
        if isinstance(self.LinearRegionItem,pg.LinearRegionItem):
            audio_range = np.abs(self.data.audio.time.values[0] - self.data.audio.time.values[-1])
            boundaries = self.LinearRegionItem.getRegion()
            mid = (boundaries[0] + boundaries[1])/2 
            
            self.waveformPlotWidget.getViewBox().setXRange(boundaries[0],boundaries[1],padding=0.0,update=True)
            xRange, _ = self.waveformPlotWidget.getViewBox().viewRange()
            boundary_range = np.abs(xRange[0] - xRange[1])
            slider_steps = int(audio_range/boundary_range)*100
            
            self.waveformSlider.setMaximum(slider_steps)
            mid = (xRange[0]+xRange[1])/2
            slider_location = int(((mid - 0)*(slider_steps))/(self.data.audio.time.values[-1]))
            self.waveformSlider.setValue(slider_location)


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
        
        mid = (xRange[0]+xRange[1])/2
        slider_location = round(((mid - 0)*(slider_steps))/(self.data.audio.time.values[-1]))
        self.waveformSlider.setValue(slider_location)
            


    def update_plot(self):
        left_boundary, right_boundary = self.waveformPlotWidget.getViewBox().viewRange()[0]
        left_boundary_index = np.abs(left_boundary - self.data.audio.time.values).argmin()
        right_boundary_index = np.abs(right_boundary - self.data.audio.time.values).argmin()
        items = self.waveformPlotWidget.allChildItems()
        for item in items:
            if isinstance(item,pg.PlotDataItem):
                item.setData(self.data.audio.time.values[left_boundary_index:right_boundary_index],
                             self.data.audio.signal.values[left_boundary_index:right_boundary_index])
"""
### for testing
posfile = "/home/philipp/test/0005.pos"
wavfile = "/home/philipp/test/0005.wav"
tgfile = "/home/philipp/test/0005.TextGrid"

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
w = inspector2D_window(dat,channels,tier_list)
w.show()
sys.exit(app.exec_())
"""