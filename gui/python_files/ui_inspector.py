# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_inspector.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_INSPECTOR(object):
    def setupUi(self, INSPECTOR):
        if not INSPECTOR.objectName():
            INSPECTOR.setObjectName(u"INSPECTOR")
        INSPECTOR.resize(914, 1126)
        INSPECTOR.setMouseTracking(True)
        self.centralwidget = QWidget(INSPECTOR)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(20)
        self.waveformSplitter = QSplitter(self.splitter)
        self.waveformSplitter.setObjectName(u"waveformSplitter")
        self.waveformSplitter.setOrientation(Qt.Horizontal)
        self.waveformSplitter.setHandleWidth(20)
        self.layoutWidget = QWidget(self.waveformSplitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.waveformPlotWidget = PlotWidget(self.layoutWidget)
        self.waveformPlotWidget.setObjectName(u"waveformPlotWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.waveformPlotWidget.sizePolicy().hasHeightForWidth())
        self.waveformPlotWidget.setSizePolicy(sizePolicy2)
        self.waveformPlotWidget.setMinimumSize(QSize(0, 100))
        self.waveformPlotWidget.setMaximumSize(QSize(16777215, 250))

        self.verticalLayout_3.addWidget(self.waveformPlotWidget)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.waveformSlider = QScrollBar(self.layoutWidget)
        self.waveformSlider.setObjectName(u"waveformSlider")
        self.waveformSlider.setMinimumSize(QSize(0, 15))
        self.waveformSlider.setMaximum(200)
        self.waveformSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.waveformSlider)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.zoomInButton = QPushButton(self.layoutWidget)
        self.zoomInButton.setObjectName(u"zoomInButton")
        self.zoomInButton.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.zoomInButton)

        self.zoomOutButton = QPushButton(self.layoutWidget)
        self.zoomOutButton.setObjectName(u"zoomOutButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.zoomOutButton.sizePolicy().hasHeightForWidth())
        self.zoomOutButton.setSizePolicy(sizePolicy3)
        self.zoomOutButton.setMinimumSize(QSize(0, 25))
        self.zoomOutButton.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.zoomOutButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.PLAY_AUDIO = QPushButton(self.layoutWidget)
        self.PLAY_AUDIO.setObjectName(u"PLAY_AUDIO")
        self.PLAY_AUDIO.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_5.addWidget(self.PLAY_AUDIO)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.waveformSplitter.addWidget(self.layoutWidget)
        self.layoutWidget_2 = QWidget(self.waveformSplitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_2 = QFrame(self.layoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        sizePolicy3.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy3)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_6.addLayout(self.verticalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.displayAnnotationCheckBox = QCheckBox(self.layoutWidget_2)
        self.displayAnnotationCheckBox.setObjectName(u"displayAnnotationCheckBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.displayAnnotationCheckBox.sizePolicy().hasHeightForWidth())
        self.displayAnnotationCheckBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.displayAnnotationCheckBox)

        self.audioAnnotationComboBox = QComboBox(self.layoutWidget_2)
        self.audioAnnotationComboBox.addItem("")
        self.audioAnnotationComboBox.setObjectName(u"audioAnnotationComboBox")
        sizePolicy3.setHeightForWidth(self.audioAnnotationComboBox.sizePolicy().hasHeightForWidth())
        self.audioAnnotationComboBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.audioAnnotationComboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(500, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_2)

        self.waveformSplitter.addWidget(self.layoutWidget_2)
        self.splitter.addWidget(self.waveformSplitter)
        self.emaSplitter = QSplitter(self.splitter)
        self.emaSplitter.setObjectName(u"emaSplitter")
        self.emaSplitter.setOrientation(Qt.Horizontal)
        self.emaSplitter.setHandleWidth(20)
        self.layoutWidget_3 = QWidget(self.emaSplitter)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.EMA_PANEL_LAYOUT = QVBoxLayout(self.layoutWidget_3)
        self.EMA_PANEL_LAYOUT.setObjectName(u"EMA_PANEL_LAYOUT")
        self.EMA_PANEL_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.emaPanel1 = QFrame(self.layoutWidget_3)
        self.emaPanel1.setObjectName(u"emaPanel1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.emaPanel1.sizePolicy().hasHeightForWidth())
        self.emaPanel1.setSizePolicy(sizePolicy6)
        self.emaPanel1.setMinimumSize(QSize(0, 50))
        self.emaPanel1.setFrameShape(QFrame.StyledPanel)
        self.emaPanel1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.emaPanel1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.emaPanel1)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)
        self.label_11.setMinimumSize(QSize(0, 10))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_11)

        self.line_16 = QFrame(self.emaPanel1)
        self.line_16.setObjectName(u"line_16")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.line_16.sizePolicy().hasHeightForWidth())
        self.line_16.setSizePolicy(sizePolicy8)
        self.line_16.setMinimumSize(QSize(0, 10))
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_16)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.emaPlotWidget1 = PlotWidget(self.emaPanel1)
        self.emaPlotWidget1.setObjectName(u"emaPlotWidget1")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.emaPlotWidget1.sizePolicy().hasHeightForWidth())
        self.emaPlotWidget1.setSizePolicy(sizePolicy9)

        self.verticalLayout_16.addWidget(self.emaPlotWidget1)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.EMA_PANEL_LAYOUT.addWidget(self.emaPanel1)

        self.emaPanel2 = QFrame(self.layoutWidget_3)
        self.emaPanel2.setObjectName(u"emaPanel2")
        sizePolicy6.setHeightForWidth(self.emaPanel2.sizePolicy().hasHeightForWidth())
        self.emaPanel2.setSizePolicy(sizePolicy6)
        self.emaPanel2.setMinimumSize(QSize(0, 50))
        self.emaPanel2.setFrameShape(QFrame.StyledPanel)
        self.emaPanel2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.emaPanel2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.emaPanel2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        self.label_12.setMinimumSize(QSize(0, 10))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_12)

        self.line_17 = QFrame(self.emaPanel2)
        self.line_17.setObjectName(u"line_17")
        sizePolicy8.setHeightForWidth(self.line_17.sizePolicy().hasHeightForWidth())
        self.line_17.setSizePolicy(sizePolicy8)
        self.line_17.setMinimumSize(QSize(0, 10))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_17)


        self.verticalLayout_18.addLayout(self.horizontalLayout_17)

        self.emaPlotWidget2 = PlotWidget(self.emaPanel2)
        self.emaPlotWidget2.setObjectName(u"emaPlotWidget2")
        sizePolicy9.setHeightForWidth(self.emaPlotWidget2.sizePolicy().hasHeightForWidth())
        self.emaPlotWidget2.setSizePolicy(sizePolicy9)

        self.verticalLayout_18.addWidget(self.emaPlotWidget2)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.EMA_PANEL_LAYOUT.addWidget(self.emaPanel2)

        self.emaPanel3 = QFrame(self.layoutWidget_3)
        self.emaPanel3.setObjectName(u"emaPanel3")
        sizePolicy6.setHeightForWidth(self.emaPanel3.sizePolicy().hasHeightForWidth())
        self.emaPanel3.setSizePolicy(sizePolicy6)
        self.emaPanel3.setMinimumSize(QSize(0, 50))
        self.emaPanel3.setFrameShape(QFrame.StyledPanel)
        self.emaPanel3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.emaPanel3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.emaPanel3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy7.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy7)
        self.label_13.setMinimumSize(QSize(0, 10))
        self.label_13.setTextFormat(Qt.AutoText)
        self.label_13.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_13)

        self.line_18 = QFrame(self.emaPanel3)
        self.line_18.setObjectName(u"line_18")
        sizePolicy8.setHeightForWidth(self.line_18.sizePolicy().hasHeightForWidth())
        self.line_18.setSizePolicy(sizePolicy8)
        self.line_18.setMinimumSize(QSize(0, 10))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_18)


        self.verticalLayout_20.addLayout(self.horizontalLayout_18)

        self.emaPlotWidget3 = PlotWidget(self.emaPanel3)
        self.emaPlotWidget3.setObjectName(u"emaPlotWidget3")
        sizePolicy9.setHeightForWidth(self.emaPlotWidget3.sizePolicy().hasHeightForWidth())
        self.emaPlotWidget3.setSizePolicy(sizePolicy9)

        self.verticalLayout_20.addWidget(self.emaPlotWidget3)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)


        self.EMA_PANEL_LAYOUT.addWidget(self.emaPanel3)

        self.waveformSlider_2 = QScrollBar(self.layoutWidget_3)
        self.waveformSlider_2.setObjectName(u"waveformSlider_2")
        self.waveformSlider_2.setMinimumSize(QSize(0, 15))
        self.waveformSlider_2.setMaximum(200)
        self.waveformSlider_2.setSingleStep(1)
        self.waveformSlider_2.setOrientation(Qt.Horizontal)

        self.EMA_PANEL_LAYOUT.addWidget(self.waveformSlider_2)

        self.emaSplitter.addWidget(self.layoutWidget_3)
        self.layoutWidget_4 = QWidget(self.emaSplitter)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.EMA_CONTROL_LAYOUT = QVBoxLayout(self.layoutWidget_4)
        self.EMA_CONTROL_LAYOUT.setObjectName(u"EMA_CONTROL_LAYOUT")
        self.EMA_CONTROL_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.layoutWidget_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy10)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.line_6 = QFrame(self.layoutWidget_4)
        self.line_6.setObjectName(u"line_6")
        sizePolicy1.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy1)
        self.line_6.setMaximumSize(QSize(16777215, 16777215))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)


        self.EMA_CONTROL_LAYOUT.addLayout(self.horizontalLayout_8)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.displayEmaPanel1CheckBox = QCheckBox(self.layoutWidget_4)
        self.displayEmaPanel1CheckBox.setObjectName(u"displayEmaPanel1CheckBox")
        self.displayEmaPanel1CheckBox.setChecked(True)

        self.verticalLayout_11.addWidget(self.displayEmaPanel1CheckBox)

        self.displayEmaPanel2CheckBox = QCheckBox(self.layoutWidget_4)
        self.displayEmaPanel2CheckBox.setObjectName(u"displayEmaPanel2CheckBox")

        self.verticalLayout_11.addWidget(self.displayEmaPanel2CheckBox)

        self.displayEmaPanel3CheckBox = QCheckBox(self.layoutWidget_4)
        self.displayEmaPanel3CheckBox.setObjectName(u"displayEmaPanel3CheckBox")

        self.verticalLayout_11.addWidget(self.displayEmaPanel3CheckBox)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.emaControlTable = QTableWidget(self.layoutWidget_4)
        self.emaControlTable.setObjectName(u"emaControlTable")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.emaControlTable.sizePolicy().hasHeightForWidth())
        self.emaControlTable.setSizePolicy(sizePolicy11)

        self.verticalLayout_10.addWidget(self.emaControlTable)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.addChannelToEmaControlTableButton = QPushButton(self.layoutWidget_4)
        self.addChannelToEmaControlTableButton.setObjectName(u"addChannelToEmaControlTableButton")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.addChannelToEmaControlTableButton.sizePolicy().hasHeightForWidth())
        self.addChannelToEmaControlTableButton.setSizePolicy(sizePolicy12)
        self.addChannelToEmaControlTableButton.setMinimumSize(QSize(0, 20))
        self.addChannelToEmaControlTableButton.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_9.addWidget(self.addChannelToEmaControlTableButton)

        self.removeChannelFromEmaControlTableButton = QPushButton(self.layoutWidget_4)
        self.removeChannelFromEmaControlTableButton.setObjectName(u"removeChannelFromEmaControlTableButton")
        sizePolicy12.setHeightForWidth(self.removeChannelFromEmaControlTableButton.sizePolicy().hasHeightForWidth())
        self.removeChannelFromEmaControlTableButton.setSizePolicy(sizePolicy12)
        self.removeChannelFromEmaControlTableButton.setMinimumSize(QSize(0, 20))
        self.removeChannelFromEmaControlTableButton.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_9.addWidget(self.removeChannelFromEmaControlTableButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)


        self.EMA_CONTROL_LAYOUT.addLayout(self.verticalLayout_10)

        self.line_8 = QFrame(self.layoutWidget_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.EMA_CONTROL_LAYOUT.addWidget(self.line_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.layoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.label_5)

        self.line_9 = QFrame(self.layoutWidget_4)
        self.line_9.setObjectName(u"line_9")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy13)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_9)


        self.EMA_CONTROL_LAYOUT.addLayout(self.horizontalLayout_10)

        self.addLandmarkButton = QPushButton(self.layoutWidget_4)
        self.addLandmarkButton.setObjectName(u"addLandmarkButton")
        sizePolicy12.setHeightForWidth(self.addLandmarkButton.sizePolicy().hasHeightForWidth())
        self.addLandmarkButton.setSizePolicy(sizePolicy12)
        self.addLandmarkButton.setCheckable(True)

        self.EMA_CONTROL_LAYOUT.addWidget(self.addLandmarkButton)

        self.removeLandmarkButton = QPushButton(self.layoutWidget_4)
        self.removeLandmarkButton.setObjectName(u"removeLandmarkButton")
        sizePolicy13.setHeightForWidth(self.removeLandmarkButton.sizePolicy().hasHeightForWidth())
        self.removeLandmarkButton.setSizePolicy(sizePolicy13)
        self.removeLandmarkButton.setCheckable(True)

        self.EMA_CONTROL_LAYOUT.addWidget(self.removeLandmarkButton)

        self.renameLandmarkButton = QPushButton(self.layoutWidget_4)
        self.renameLandmarkButton.setObjectName(u"renameLandmarkButton")
        sizePolicy13.setHeightForWidth(self.renameLandmarkButton.sizePolicy().hasHeightForWidth())
        self.renameLandmarkButton.setSizePolicy(sizePolicy13)
        self.renameLandmarkButton.setCheckable(True)

        self.EMA_CONTROL_LAYOUT.addWidget(self.renameLandmarkButton)

        self.selectRegionButton = QPushButton(self.layoutWidget_4)
        self.selectRegionButton.setObjectName(u"selectRegionButton")
        sizePolicy13.setHeightForWidth(self.selectRegionButton.sizePolicy().hasHeightForWidth())
        self.selectRegionButton.setSizePolicy(sizePolicy13)
        self.selectRegionButton.setCheckable(True)

        self.EMA_CONTROL_LAYOUT.addWidget(self.selectRegionButton)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.selectLandmarkDetectionComboBox = QComboBox(self.layoutWidget_4)
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.setObjectName(u"selectLandmarkDetectionComboBox")

        self.gridLayout_2.addWidget(self.selectLandmarkDetectionComboBox, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)


        self.EMA_CONTROL_LAYOUT.addLayout(self.gridLayout_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.layoutWidget_4)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.line_11 = QFrame(self.layoutWidget_4)
        self.line_11.setObjectName(u"line_11")
        sizePolicy13.setHeightForWidth(self.line_11.sizePolicy().hasHeightForWidth())
        self.line_11.setSizePolicy(sizePolicy13)
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_11)


        self.EMA_CONTROL_LAYOUT.addLayout(self.horizontalLayout_12)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.emaPanel1TierNameLineEdit = QLineEdit(self.layoutWidget_4)
        self.emaPanel1TierNameLineEdit.setObjectName(u"emaPanel1TierNameLineEdit")
        sizePolicy3.setHeightForWidth(self.emaPanel1TierNameLineEdit.sizePolicy().hasHeightForWidth())
        self.emaPanel1TierNameLineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.emaPanel1TierNameLineEdit, 1, 2, 1, 1)

        self.emaPanel2DisplayLandmarksCheckBox = QCheckBox(self.layoutWidget_4)
        self.emaPanel2DisplayLandmarksCheckBox.setObjectName(u"emaPanel2DisplayLandmarksCheckBox")

        self.gridLayout_3.addWidget(self.emaPanel2DisplayLandmarksCheckBox, 2, 0, 1, 1)

        self.emaPanel3SelectTierComboBox = QComboBox(self.layoutWidget_4)
        self.emaPanel3SelectTierComboBox.setObjectName(u"emaPanel3SelectTierComboBox")
        sizePolicy3.setHeightForWidth(self.emaPanel3SelectTierComboBox.sizePolicy().hasHeightForWidth())
        self.emaPanel3SelectTierComboBox.setSizePolicy(sizePolicy3)
        self.emaPanel3SelectTierComboBox.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.emaPanel3SelectTierComboBox, 3, 1, 1, 1)

        self.emaPanel2SelectTierComboBox = QComboBox(self.layoutWidget_4)
        self.emaPanel2SelectTierComboBox.setObjectName(u"emaPanel2SelectTierComboBox")
        sizePolicy5.setHeightForWidth(self.emaPanel2SelectTierComboBox.sizePolicy().hasHeightForWidth())
        self.emaPanel2SelectTierComboBox.setSizePolicy(sizePolicy5)
        self.emaPanel2SelectTierComboBox.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.emaPanel2SelectTierComboBox, 2, 1, 1, 1)

        self.emaPanel3DisplayLandmarksCheckBox = QCheckBox(self.layoutWidget_4)
        self.emaPanel3DisplayLandmarksCheckBox.setObjectName(u"emaPanel3DisplayLandmarksCheckBox")

        self.gridLayout_3.addWidget(self.emaPanel3DisplayLandmarksCheckBox, 3, 0, 1, 1)

        self.label_10 = QLabel(self.layoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.emaPanel1SelectTierComboBox = QComboBox(self.layoutWidget_4)
        self.emaPanel1SelectTierComboBox.setObjectName(u"emaPanel1SelectTierComboBox")
        sizePolicy3.setHeightForWidth(self.emaPanel1SelectTierComboBox.sizePolicy().hasHeightForWidth())
        self.emaPanel1SelectTierComboBox.setSizePolicy(sizePolicy3)
        self.emaPanel1SelectTierComboBox.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.emaPanel1SelectTierComboBox, 1, 1, 1, 1)

        self.emaPanel1DisplayLandmarksCheckBox = QCheckBox(self.layoutWidget_4)
        self.emaPanel1DisplayLandmarksCheckBox.setObjectName(u"emaPanel1DisplayLandmarksCheckBox")
        sizePolicy5.setHeightForWidth(self.emaPanel1DisplayLandmarksCheckBox.sizePolicy().hasHeightForWidth())
        self.emaPanel1DisplayLandmarksCheckBox.setSizePolicy(sizePolicy5)
        self.emaPanel1DisplayLandmarksCheckBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.emaPanel1DisplayLandmarksCheckBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.emaPanel1DisplayLandmarksCheckBox, 1, 0, 1, 1)

        self.label_15 = QLabel(self.layoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)

        self.emaPanel2TierNameLineEdit = QLineEdit(self.layoutWidget_4)
        self.emaPanel2TierNameLineEdit.setObjectName(u"emaPanel2TierNameLineEdit")
        sizePolicy3.setHeightForWidth(self.emaPanel2TierNameLineEdit.sizePolicy().hasHeightForWidth())
        self.emaPanel2TierNameLineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.emaPanel2TierNameLineEdit, 2, 2, 1, 1)

        self.label_14 = QLabel(self.layoutWidget_4)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)

        self.emaPanel3TierNameLineEdit = QLineEdit(self.layoutWidget_4)
        self.emaPanel3TierNameLineEdit.setObjectName(u"emaPanel3TierNameLineEdit")
        sizePolicy3.setHeightForWidth(self.emaPanel3TierNameLineEdit.sizePolicy().hasHeightForWidth())
        self.emaPanel3TierNameLineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.emaPanel3TierNameLineEdit, 3, 2, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget_4)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 4, 2, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget_4)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 4, 1, 1, 1)


        self.EMA_CONTROL_LAYOUT.addLayout(self.gridLayout_3)

        self.storeLandmarksButton = QPushButton(self.layoutWidget_4)
        self.storeLandmarksButton.setObjectName(u"storeLandmarksButton")

        self.EMA_CONTROL_LAYOUT.addWidget(self.storeLandmarksButton)

        self.horizontalSpacer = QSpacerItem(500, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.EMA_CONTROL_LAYOUT.addItem(self.horizontalSpacer)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.EMA_CONTROL_LAYOUT.addItem(self.verticalSpacer_3)

        self.emaSplitter.addWidget(self.layoutWidget_4)
        self.splitter.addWidget(self.emaSplitter)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        INSPECTOR.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(INSPECTOR)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 914, 34))
        INSPECTOR.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(INSPECTOR)
        self.statusbar.setObjectName(u"statusbar")
        INSPECTOR.setStatusBar(self.statusbar)

        self.retranslateUi(INSPECTOR)

        QMetaObject.connectSlotsByName(INSPECTOR)
    # setupUi

    def retranslateUi(self, INSPECTOR):
        INSPECTOR.setWindowTitle(QCoreApplication.translate("INSPECTOR", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("INSPECTOR", u"WAVEFORM", None))
        self.zoomInButton.setText(QCoreApplication.translate("INSPECTOR", u"zoom in", None))
        self.zoomOutButton.setText(QCoreApplication.translate("INSPECTOR", u"zoom out", None))
        self.PLAY_AUDIO.setText(QCoreApplication.translate("INSPECTOR", u"play", None))
        self.label_2.setText(QCoreApplication.translate("INSPECTOR", u"CONTROLS", None))
        self.displayAnnotationCheckBox.setText(QCoreApplication.translate("INSPECTOR", u"show", None))
        self.audioAnnotationComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"Tiers", None))

        self.label_11.setText(QCoreApplication.translate("INSPECTOR", u"PANEL 1", None))
        self.label_12.setText(QCoreApplication.translate("INSPECTOR", u"PANEL 2", None))
        self.label_13.setText(QCoreApplication.translate("INSPECTOR", u"PANEL 3", None))
        self.label_4.setText(QCoreApplication.translate("INSPECTOR", u"PLOTTING CONTROLS", None))
        self.displayEmaPanel1CheckBox.setText(QCoreApplication.translate("INSPECTOR", u"show panel 1", None))
        self.displayEmaPanel2CheckBox.setText(QCoreApplication.translate("INSPECTOR", u"show panel 2", None))
        self.displayEmaPanel3CheckBox.setText(QCoreApplication.translate("INSPECTOR", u"show panel 3", None))
        self.addChannelToEmaControlTableButton.setText(QCoreApplication.translate("INSPECTOR", u"+", None))
        self.removeChannelFromEmaControlTableButton.setText(QCoreApplication.translate("INSPECTOR", u"-", None))
        self.label_5.setText(QCoreApplication.translate("INSPECTOR", u"LANDMARK CONTROLS", None))
        self.addLandmarkButton.setText(QCoreApplication.translate("INSPECTOR", u"add", None))
        self.removeLandmarkButton.setText(QCoreApplication.translate("INSPECTOR", u"remove", None))
        self.renameLandmarkButton.setText(QCoreApplication.translate("INSPECTOR", u"rename", None))
        self.selectRegionButton.setText(QCoreApplication.translate("INSPECTOR", u"select region", None))
        self.selectLandmarkDetectionComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"vel20", None))
        self.selectLandmarkDetectionComboBox.setItemText(1, QCoreApplication.translate("INSPECTOR", u"tvel20", None))
        self.selectLandmarkDetectionComboBox.setItemText(2, QCoreApplication.translate("INSPECTOR", u"acc", None))

        self.label_6.setText(QCoreApplication.translate("INSPECTOR", u"detection algorithm:", None))
        self.label_17.setText(QCoreApplication.translate("INSPECTOR", u"LANDMARK TIER CONTROLS", None))
        self.emaPanel2DisplayLandmarksCheckBox.setText("")
        self.emaPanel3DisplayLandmarksCheckBox.setText("")
        self.label_10.setText(QCoreApplication.translate("INSPECTOR", u"show", None))
        self.emaPanel1DisplayLandmarksCheckBox.setText("")
        self.label_15.setText(QCoreApplication.translate("INSPECTOR", u"edit tier name", None))
        self.label_14.setText(QCoreApplication.translate("INSPECTOR", u"tier", None))
        self.pushButton.setText(QCoreApplication.translate("INSPECTOR", u"remove", None))
        self.storeLandmarksButton.setText(QCoreApplication.translate("INSPECTOR", u"store", None))
    # retranslateUi

