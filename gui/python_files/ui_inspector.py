# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_inspector.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.waveformSplitter.setAcceptDrops(False)
        self.waveformSplitter.setAutoFillBackground(False)
        self.waveformSplitter.setFrameShape(QFrame.NoFrame)
        self.waveformSplitter.setFrameShadow(QFrame.Raised)
        self.waveformSplitter.setLineWidth(10)
        self.waveformSplitter.setMidLineWidth(5)
        self.waveformSplitter.setOrientation(Qt.Horizontal)
        self.waveformSplitter.setOpaqueResize(False)
        self.waveformSplitter.setHandleWidth(20)
        self.waveformSplitter.setChildrenCollapsible(False)
        self.layoutWidget = QWidget(self.waveformSplitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.waveformPlotWidget.sizePolicy().hasHeightForWidth())
        self.waveformPlotWidget.setSizePolicy(sizePolicy2)
        self.waveformPlotWidget.setMinimumSize(QSize(0, 0))
        self.waveformPlotWidget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.waveformPlotWidget)

        self.spectrogramFrame = QFrame(self.layoutWidget)
        self.spectrogramFrame.setObjectName(u"spectrogramFrame")
        self.spectrogramFrame.setFrameShape(QFrame.StyledPanel)
        self.spectrogramFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.spectrogramFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.spectrogramWidget = PlotWidget(self.spectrogramFrame)
        self.spectrogramWidget.setObjectName(u"spectrogramWidget")
        sizePolicy2.setHeightForWidth(self.spectrogramWidget.sizePolicy().hasHeightForWidth())
        self.spectrogramWidget.setSizePolicy(sizePolicy2)
        self.spectrogramWidget.setMinimumSize(QSize(0, 0))
        self.spectrogramWidget.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.spectrogramWidget)


        self.verticalLayout_3.addWidget(self.spectrogramFrame)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.waveformSlider = QScrollBar(self.layoutWidget)
        self.waveformSlider.setObjectName(u"waveformSlider")
        self.waveformSlider.setMinimumSize(QSize(0, 15))
        self.waveformSlider.setMaximum(1)
        self.waveformSlider.setSliderPosition(1)
        self.waveformSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.waveformSlider)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.zoomAllButton = QPushButton(self.layoutWidget)
        self.zoomAllButton.setObjectName(u"zoomAllButton")

        self.horizontalLayout_3.addWidget(self.zoomAllButton)

        self.zoomOutButton = QPushButton(self.layoutWidget)
        self.zoomOutButton.setObjectName(u"zoomOutButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.zoomOutButton.sizePolicy().hasHeightForWidth())
        self.zoomOutButton.setSizePolicy(sizePolicy3)
        self.zoomOutButton.setMinimumSize(QSize(0, 0))
        self.zoomOutButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.zoomOutButton)

        self.zoomInButton = QPushButton(self.layoutWidget)
        self.zoomInButton.setObjectName(u"zoomInButton")
        self.zoomInButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.zoomInButton)

        self.zoomSelectionButton = QPushButton(self.layoutWidget)
        self.zoomSelectionButton.setObjectName(u"zoomSelectionButton")

        self.horizontalLayout_3.addWidget(self.zoomSelectionButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.PLAY_AUDIO = QPushButton(self.layoutWidget)
        self.PLAY_AUDIO.setObjectName(u"PLAY_AUDIO")
        self.PLAY_AUDIO.setMaximumSize(QSize(16777215, 16777215))

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
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
        self.displayAnnotationPushButton = QPushButton(self.layoutWidget_2)
        self.displayAnnotationPushButton.setObjectName(u"displayAnnotationPushButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.displayAnnotationPushButton.sizePolicy().hasHeightForWidth())
        self.displayAnnotationPushButton.setSizePolicy(sizePolicy5)
        self.displayAnnotationPushButton.setMinimumSize(QSize(75, 0))
        self.displayAnnotationPushButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.displayAnnotationPushButton)

        self.audioAnnotationComboBox = QComboBox(self.layoutWidget_2)
        self.audioAnnotationComboBox.addItem("")
        self.audioAnnotationComboBox.setObjectName(u"audioAnnotationComboBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.audioAnnotationComboBox.sizePolicy().hasHeightForWidth())
        self.audioAnnotationComboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_5.addWidget(self.audioAnnotationComboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.line_3 = QFrame(self.layoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        sizePolicy3.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy3)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.showSpectrogramButton = QPushButton(self.layoutWidget_2)
        self.showSpectrogramButton.setObjectName(u"showSpectrogramButton")
        self.showSpectrogramButton.setCheckable(True)

        self.verticalLayout_6.addWidget(self.showSpectrogramButton)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.line_4 = QFrame(self.layoutWidget_2)
        self.line_4.setObjectName(u"line_4")
        sizePolicy6.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy6)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_4)

        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.line_5 = QFrame(self.layoutWidget_2)
        self.line_5.setObjectName(u"line_5")
        sizePolicy6.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy6)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.showFundamentalFrequencyButton = QPushButton(self.layoutWidget_2)
        self.showFundamentalFrequencyButton.setObjectName(u"showFundamentalFrequencyButton")
        sizePolicy5.setHeightForWidth(self.showFundamentalFrequencyButton.sizePolicy().hasHeightForWidth())
        self.showFundamentalFrequencyButton.setSizePolicy(sizePolicy5)
        self.showFundamentalFrequencyButton.setMinimumSize(QSize(75, 0))
        self.showFundamentalFrequencyButton.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.showFundamentalFrequencyButton)

        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(50, 0))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.fundamentalFrequencyComboBox = QComboBox(self.layoutWidget_2)
        self.fundamentalFrequencyComboBox.addItem("")
        self.fundamentalFrequencyComboBox.addItem("")
        self.fundamentalFrequencyComboBox.setObjectName(u"fundamentalFrequencyComboBox")
        sizePolicy6.setHeightForWidth(self.fundamentalFrequencyComboBox.sizePolicy().hasHeightForWidth())
        self.fundamentalFrequencyComboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.fundamentalFrequencyComboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.line_7 = QFrame(self.layoutWidget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_7)

        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setFont(font)
        self.label_9.setFrameShadow(QFrame.Plain)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setMargin(0)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.line_8 = QFrame(self.layoutWidget_2)
        self.line_8.setObjectName(u"line_8")
        sizePolicy6.setHeightForWidth(self.line_8.sizePolicy().hasHeightForWidth())
        self.line_8.setSizePolicy(sizePolicy6)
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.showIntensityButton = QPushButton(self.layoutWidget_2)
        self.showIntensityButton.setObjectName(u"showIntensityButton")
        sizePolicy5.setHeightForWidth(self.showIntensityButton.sizePolicy().hasHeightForWidth())
        self.showIntensityButton.setSizePolicy(sizePolicy5)
        self.showIntensityButton.setMinimumSize(QSize(75, 0))
        self.showIntensityButton.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.showIntensityButton)

        self.label_16 = QLabel(self.layoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMinimumSize(QSize(50, 0))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_16)

        self.intensityComboBox = QComboBox(self.layoutWidget_2)
        self.intensityComboBox.addItem("")
        self.intensityComboBox.setObjectName(u"intensityComboBox")
        sizePolicy6.setHeightForWidth(self.intensityComboBox.sizePolicy().hasHeightForWidth())
        self.intensityComboBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_14.addWidget(self.intensityComboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.waveformSplitter.addWidget(self.layoutWidget_2)
        self.splitter.addWidget(self.waveformSplitter)
        self.emaSplitter = QSplitter(self.splitter)
        self.emaSplitter.setObjectName(u"emaSplitter")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.emaSplitter.sizePolicy().hasHeightForWidth())
        self.emaSplitter.setSizePolicy(sizePolicy7)
        self.emaSplitter.setFrameShadow(QFrame.Raised)
        self.emaSplitter.setLineWidth(10)
        self.emaSplitter.setMidLineWidth(5)
        self.emaSplitter.setOrientation(Qt.Horizontal)
        self.emaSplitter.setOpaqueResize(False)
        self.emaSplitter.setHandleWidth(20)
        self.emaSplitter.setChildrenCollapsible(False)
        self.layoutWidget_3 = QWidget(self.emaSplitter)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.EMA_PANEL_LAYOUT = QVBoxLayout(self.layoutWidget_3)
        self.EMA_PANEL_LAYOUT.setSpacing(1)
        self.EMA_PANEL_LAYOUT.setObjectName(u"EMA_PANEL_LAYOUT")
        self.EMA_PANEL_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.emaPanel1 = QFrame(self.layoutWidget_3)
        self.emaPanel1.setObjectName(u"emaPanel1")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.emaPanel1.sizePolicy().hasHeightForWidth())
        self.emaPanel1.setSizePolicy(sizePolicy8)
        self.emaPanel1.setMinimumSize(QSize(0, 50))
        self.emaPanel1.setFrameShape(QFrame.StyledPanel)
        self.emaPanel1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.emaPanel1)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_11 = QLabel(self.emaPanel1)
        self.label_11.setObjectName(u"label_11")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy9)
        self.label_11.setMinimumSize(QSize(0, 10))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_11)

        self.line_16 = QFrame(self.emaPanel1)
        self.line_16.setObjectName(u"line_16")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.line_16.sizePolicy().hasHeightForWidth())
        self.line_16.setSizePolicy(sizePolicy10)
        self.line_16.setMinimumSize(QSize(0, 10))
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_16)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.emaPlotWidget1 = PlotWidget(self.emaPanel1)
        self.emaPlotWidget1.setObjectName(u"emaPlotWidget1")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.emaPlotWidget1.sizePolicy().hasHeightForWidth())
        self.emaPlotWidget1.setSizePolicy(sizePolicy11)

        self.verticalLayout_16.addWidget(self.emaPlotWidget1)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.EMA_PANEL_LAYOUT.addWidget(self.emaPanel1)

        self.emaPanel2 = QFrame(self.layoutWidget_3)
        self.emaPanel2.setObjectName(u"emaPanel2")
        sizePolicy8.setHeightForWidth(self.emaPanel2.sizePolicy().hasHeightForWidth())
        self.emaPanel2.setSizePolicy(sizePolicy8)
        self.emaPanel2.setMinimumSize(QSize(0, 50))
        self.emaPanel2.setFrameShape(QFrame.StyledPanel)
        self.emaPanel2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.emaPanel2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_12 = QLabel(self.emaPanel2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy9.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy9)
        self.label_12.setMinimumSize(QSize(0, 10))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_12)

        self.line_17 = QFrame(self.emaPanel2)
        self.line_17.setObjectName(u"line_17")
        sizePolicy10.setHeightForWidth(self.line_17.sizePolicy().hasHeightForWidth())
        self.line_17.setSizePolicy(sizePolicy10)
        self.line_17.setMinimumSize(QSize(0, 10))
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_17)


        self.verticalLayout_18.addLayout(self.horizontalLayout_17)

        self.emaPlotWidget2 = PlotWidget(self.emaPanel2)
        self.emaPlotWidget2.setObjectName(u"emaPlotWidget2")
        sizePolicy11.setHeightForWidth(self.emaPlotWidget2.sizePolicy().hasHeightForWidth())
        self.emaPlotWidget2.setSizePolicy(sizePolicy11)

        self.verticalLayout_18.addWidget(self.emaPlotWidget2)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.EMA_PANEL_LAYOUT.addWidget(self.emaPanel2)

        self.emaPanel3 = QFrame(self.layoutWidget_3)
        self.emaPanel3.setObjectName(u"emaPanel3")
        sizePolicy8.setHeightForWidth(self.emaPanel3.sizePolicy().hasHeightForWidth())
        self.emaPanel3.setSizePolicy(sizePolicy8)
        self.emaPanel3.setMinimumSize(QSize(0, 50))
        self.emaPanel3.setFrameShape(QFrame.StyledPanel)
        self.emaPanel3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.emaPanel3)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_13 = QLabel(self.emaPanel3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy9.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy9)
        self.label_13.setMinimumSize(QSize(0, 10))
        self.label_13.setTextFormat(Qt.AutoText)
        self.label_13.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_13)

        self.line_18 = QFrame(self.emaPanel3)
        self.line_18.setObjectName(u"line_18")
        sizePolicy10.setHeightForWidth(self.line_18.sizePolicy().hasHeightForWidth())
        self.line_18.setSizePolicy(sizePolicy10)
        self.line_18.setMinimumSize(QSize(0, 10))
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_18.addWidget(self.line_18)


        self.verticalLayout_20.addLayout(self.horizontalLayout_18)

        self.emaPlotWidget3 = PlotWidget(self.emaPanel3)
        self.emaPlotWidget3.setObjectName(u"emaPlotWidget3")
        sizePolicy11.setHeightForWidth(self.emaPlotWidget3.sizePolicy().hasHeightForWidth())
        self.emaPlotWidget3.setSizePolicy(sizePolicy11)

        self.verticalLayout_20.addWidget(self.emaPlotWidget3)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)


        self.EMA_PANEL_LAYOUT.addWidget(self.emaPanel3)

        self.waveformSlider_2 = QScrollBar(self.layoutWidget_3)
        self.waveformSlider_2.setObjectName(u"waveformSlider_2")
        self.waveformSlider_2.setMinimumSize(QSize(0, 15))
        self.waveformSlider_2.setMaximum(1)
        self.waveformSlider_2.setSingleStep(1)
        self.waveformSlider_2.setOrientation(Qt.Horizontal)

        self.EMA_PANEL_LAYOUT.addWidget(self.waveformSlider_2)

        self.emaSplitter.addWidget(self.layoutWidget_3)
        self.splitter_2 = QSplitter(self.emaSplitter)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setFrameShadow(QFrame.Raised)
        self.splitter_2.setLineWidth(50)
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(10)
        self.verticalLayoutWidget = QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy12)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.line_6 = QFrame(self.verticalLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        sizePolicy1.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy1)
        self.line_6.setMaximumSize(QSize(16777215, 16777215))
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.displayEmaPanel1PushButton = QPushButton(self.verticalLayoutWidget)
        self.displayEmaPanel1PushButton.setObjectName(u"displayEmaPanel1PushButton")
        self.displayEmaPanel1PushButton.setStyleSheet(u"")
        self.displayEmaPanel1PushButton.setCheckable(True)
        self.displayEmaPanel1PushButton.setChecked(True)

        self.verticalLayout_11.addWidget(self.displayEmaPanel1PushButton)

        self.displayEmaPanel2PushButton = QPushButton(self.verticalLayoutWidget)
        self.displayEmaPanel2PushButton.setObjectName(u"displayEmaPanel2PushButton")
        self.displayEmaPanel2PushButton.setCheckable(True)

        self.verticalLayout_11.addWidget(self.displayEmaPanel2PushButton)

        self.displayEmaPanel3PushButton = QPushButton(self.verticalLayoutWidget)
        self.displayEmaPanel3PushButton.setObjectName(u"displayEmaPanel3PushButton")
        self.displayEmaPanel3PushButton.setCheckable(True)

        self.verticalLayout_11.addWidget(self.displayEmaPanel3PushButton)

        self.emaControlTable = QTableWidget(self.verticalLayoutWidget)
        self.emaControlTable.setObjectName(u"emaControlTable")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.emaControlTable.sizePolicy().hasHeightForWidth())
        self.emaControlTable.setSizePolicy(sizePolicy13)
        self.emaControlTable.setMinimumSize(QSize(100, 0))

        self.verticalLayout_11.addWidget(self.emaControlTable)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.addChannelToEmaControlTableButton = QPushButton(self.verticalLayoutWidget)
        self.addChannelToEmaControlTableButton.setObjectName(u"addChannelToEmaControlTableButton")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.addChannelToEmaControlTableButton.sizePolicy().hasHeightForWidth())
        self.addChannelToEmaControlTableButton.setSizePolicy(sizePolicy14)
        self.addChannelToEmaControlTableButton.setMinimumSize(QSize(0, 20))
        self.addChannelToEmaControlTableButton.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_9.addWidget(self.addChannelToEmaControlTableButton)

        self.removeChannelFromEmaControlTableButton = QPushButton(self.verticalLayoutWidget)
        self.removeChannelFromEmaControlTableButton.setObjectName(u"removeChannelFromEmaControlTableButton")
        sizePolicy14.setHeightForWidth(self.removeChannelFromEmaControlTableButton.sizePolicy().hasHeightForWidth())
        self.removeChannelFromEmaControlTableButton.setSizePolicy(sizePolicy14)
        self.removeChannelFromEmaControlTableButton.setMinimumSize(QSize(0, 20))
        self.removeChannelFromEmaControlTableButton.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_9.addWidget(self.removeChannelFromEmaControlTableButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addLayout(self.verticalLayout_11)

        self.splitter_2.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy5.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy5)

        self.horizontalLayout_10.addWidget(self.label_5)

        self.line_9 = QFrame(self.verticalLayoutWidget_2)
        self.line_9.setObjectName(u"line_9")
        sizePolicy6.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy6)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_9)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.addLandmarkButton = QPushButton(self.verticalLayoutWidget_2)
        self.addLandmarkButton.setObjectName(u"addLandmarkButton")
        sizePolicy14.setHeightForWidth(self.addLandmarkButton.sizePolicy().hasHeightForWidth())
        self.addLandmarkButton.setSizePolicy(sizePolicy14)
        self.addLandmarkButton.setCheckable(True)

        self.verticalLayout_4.addWidget(self.addLandmarkButton)

        self.removeLandmarkButton = QPushButton(self.verticalLayoutWidget_2)
        self.removeLandmarkButton.setObjectName(u"removeLandmarkButton")
        sizePolicy6.setHeightForWidth(self.removeLandmarkButton.sizePolicy().hasHeightForWidth())
        self.removeLandmarkButton.setSizePolicy(sizePolicy6)
        self.removeLandmarkButton.setCheckable(True)

        self.verticalLayout_4.addWidget(self.removeLandmarkButton)

        self.renameLandmarkButton = QPushButton(self.verticalLayoutWidget_2)
        self.renameLandmarkButton.setObjectName(u"renameLandmarkButton")
        sizePolicy6.setHeightForWidth(self.renameLandmarkButton.sizePolicy().hasHeightForWidth())
        self.renameLandmarkButton.setSizePolicy(sizePolicy6)
        self.renameLandmarkButton.setCheckable(True)

        self.verticalLayout_4.addWidget(self.renameLandmarkButton)

        self.selectRegionButton = QPushButton(self.verticalLayoutWidget_2)
        self.selectRegionButton.setObjectName(u"selectRegionButton")
        sizePolicy6.setHeightForWidth(self.selectRegionButton.sizePolicy().hasHeightForWidth())
        self.selectRegionButton.setSizePolicy(sizePolicy6)
        self.selectRegionButton.setCheckable(True)

        self.verticalLayout_4.addWidget(self.selectRegionButton)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.selectLandmarkDetectionComboBox = QComboBox(self.verticalLayoutWidget_2)
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.addItem("")
        self.selectLandmarkDetectionComboBox.setObjectName(u"selectLandmarkDetectionComboBox")

        self.gridLayout_2.addWidget(self.selectLandmarkDetectionComboBox, 0, 1, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.splitter_2.addWidget(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget_3 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.verticalLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy5.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy5)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.line_11 = QFrame(self.verticalLayoutWidget_3)
        self.line_11.setObjectName(u"line_11")
        sizePolicy6.setHeightForWidth(self.line_11.sizePolicy().hasHeightForWidth())
        self.line_11.setSizePolicy(sizePolicy6)
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.emaPanel1TierNameLineEdit = QLineEdit(self.verticalLayoutWidget_3)
        self.emaPanel1TierNameLineEdit.setObjectName(u"emaPanel1TierNameLineEdit")
        sizePolicy3.setHeightForWidth(self.emaPanel1TierNameLineEdit.sizePolicy().hasHeightForWidth())
        self.emaPanel1TierNameLineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.emaPanel1TierNameLineEdit, 1, 2, 1, 1)

        self.emaPanel3SelectTierComboBox = QComboBox(self.verticalLayoutWidget_3)
        self.emaPanel3SelectTierComboBox.addItem("")
        self.emaPanel3SelectTierComboBox.setObjectName(u"emaPanel3SelectTierComboBox")
        sizePolicy3.setHeightForWidth(self.emaPanel3SelectTierComboBox.sizePolicy().hasHeightForWidth())
        self.emaPanel3SelectTierComboBox.setSizePolicy(sizePolicy3)
        self.emaPanel3SelectTierComboBox.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.emaPanel3SelectTierComboBox, 3, 1, 1, 1)

        self.emaPanel2SelectTierComboBox = QComboBox(self.verticalLayoutWidget_3)
        self.emaPanel2SelectTierComboBox.addItem("")
        self.emaPanel2SelectTierComboBox.setObjectName(u"emaPanel2SelectTierComboBox")
        sizePolicy5.setHeightForWidth(self.emaPanel2SelectTierComboBox.sizePolicy().hasHeightForWidth())
        self.emaPanel2SelectTierComboBox.setSizePolicy(sizePolicy5)
        self.emaPanel2SelectTierComboBox.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.emaPanel2SelectTierComboBox, 2, 1, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.emaPanel1SelectTierComboBox = QComboBox(self.verticalLayoutWidget_3)
        self.emaPanel1SelectTierComboBox.addItem("")
        self.emaPanel1SelectTierComboBox.setObjectName(u"emaPanel1SelectTierComboBox")
        sizePolicy3.setHeightForWidth(self.emaPanel1SelectTierComboBox.sizePolicy().hasHeightForWidth())
        self.emaPanel1SelectTierComboBox.setSizePolicy(sizePolicy3)
        self.emaPanel1SelectTierComboBox.setMinimumSize(QSize(150, 0))

        self.gridLayout_3.addWidget(self.emaPanel1SelectTierComboBox, 1, 1, 1, 1)

        self.label_15 = QLabel(self.verticalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.label_15, 0, 2, 1, 1)

        self.emaPanel2TierNameLineEdit = QLineEdit(self.verticalLayoutWidget_3)
        self.emaPanel2TierNameLineEdit.setObjectName(u"emaPanel2TierNameLineEdit")
        sizePolicy3.setHeightForWidth(self.emaPanel2TierNameLineEdit.sizePolicy().hasHeightForWidth())
        self.emaPanel2TierNameLineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.emaPanel2TierNameLineEdit, 2, 2, 1, 1)

        self.label_14 = QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)

        self.emaPanel3TierNameLineEdit = QLineEdit(self.verticalLayoutWidget_3)
        self.emaPanel3TierNameLineEdit.setObjectName(u"emaPanel3TierNameLineEdit")
        sizePolicy3.setHeightForWidth(self.emaPanel3TierNameLineEdit.sizePolicy().hasHeightForWidth())
        self.emaPanel3TierNameLineEdit.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.emaPanel3TierNameLineEdit, 3, 2, 1, 1)

        self.removeTierButton = QPushButton(self.verticalLayoutWidget_3)
        self.removeTierButton.setObjectName(u"removeTierButton")

        self.gridLayout_3.addWidget(self.removeTierButton, 4, 2, 1, 1)

        self.emaAllTiersComboBox = QComboBox(self.verticalLayoutWidget_3)
        self.emaAllTiersComboBox.setObjectName(u"emaAllTiersComboBox")

        self.gridLayout_3.addWidget(self.emaAllTiersComboBox, 4, 1, 1, 1)

        self.emaPanel1DisplayLandmarksPushButton = QPushButton(self.verticalLayoutWidget_3)
        self.emaPanel1DisplayLandmarksPushButton.setObjectName(u"emaPanel1DisplayLandmarksPushButton")
        sizePolicy5.setHeightForWidth(self.emaPanel1DisplayLandmarksPushButton.sizePolicy().hasHeightForWidth())
        self.emaPanel1DisplayLandmarksPushButton.setSizePolicy(sizePolicy5)
        self.emaPanel1DisplayLandmarksPushButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.emaPanel1DisplayLandmarksPushButton.setLayoutDirection(Qt.LeftToRight)
        self.emaPanel1DisplayLandmarksPushButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.emaPanel1DisplayLandmarksPushButton, 1, 0, 1, 1)

        self.emaPanel2DisplayLandmarksPushButton = QPushButton(self.verticalLayoutWidget_3)
        self.emaPanel2DisplayLandmarksPushButton.setObjectName(u"emaPanel2DisplayLandmarksPushButton")
        self.emaPanel2DisplayLandmarksPushButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.emaPanel2DisplayLandmarksPushButton, 2, 0, 1, 1)

        self.emaPanel3DisplayLandmarksPushButton = QPushButton(self.verticalLayoutWidget_3)
        self.emaPanel3DisplayLandmarksPushButton.setObjectName(u"emaPanel3DisplayLandmarksPushButton")
        self.emaPanel3DisplayLandmarksPushButton.setCheckable(True)

        self.gridLayout_3.addWidget(self.emaPanel3DisplayLandmarksPushButton, 3, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_3)

        self.storeLandmarksButton = QPushButton(self.verticalLayoutWidget_3)
        self.storeLandmarksButton.setObjectName(u"storeLandmarksButton")

        self.verticalLayout_7.addWidget(self.storeLandmarksButton)

        self.splitter_2.addWidget(self.verticalLayoutWidget_3)
        self.emaSplitter.addWidget(self.splitter_2)
        self.splitter.addWidget(self.emaSplitter)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        INSPECTOR.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(INSPECTOR)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 914, 28))
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
        self.zoomAllButton.setText(QCoreApplication.translate("INSPECTOR", u"all", None))
        self.zoomOutButton.setText(QCoreApplication.translate("INSPECTOR", u"zoom out", None))
        self.zoomInButton.setText(QCoreApplication.translate("INSPECTOR", u"zoom in", None))
        self.zoomSelectionButton.setText(QCoreApplication.translate("INSPECTOR", u"selection", None))
        self.PLAY_AUDIO.setText(QCoreApplication.translate("INSPECTOR", u"play", None))
        self.label_2.setText(QCoreApplication.translate("INSPECTOR", u"WAVEFORM CONTROLS", None))
        self.displayAnnotationPushButton.setText("")
        self.audioAnnotationComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"Tiers", None))

        self.label_7.setText(QCoreApplication.translate("INSPECTOR", u"SPECTROGRAM CONTROLS", None))
        self.showSpectrogramButton.setText(QCoreApplication.translate("INSPECTOR", u"spectrogram", None))
        self.label_8.setText(QCoreApplication.translate("INSPECTOR", u"FUNDAMENTAL FREQUENCY", None))
        self.showFundamentalFrequencyButton.setText("")
        self.label_3.setText(QCoreApplication.translate("INSPECTOR", u"estimation:", None))
        self.fundamentalFrequencyComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"pYin", None))
        self.fundamentalFrequencyComboBox.setItemText(1, QCoreApplication.translate("INSPECTOR", u"Yin", None))

        self.label_9.setText(QCoreApplication.translate("INSPECTOR", u"INTENSITY", None))
        self.showIntensityButton.setText("")
        self.label_16.setText(QCoreApplication.translate("INSPECTOR", u"estimation:", None))
        self.intensityComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"rms", None))

        self.label_11.setText(QCoreApplication.translate("INSPECTOR", u"PANEL 1", None))
        self.label_12.setText(QCoreApplication.translate("INSPECTOR", u"PANEL 2", None))
        self.label_13.setText(QCoreApplication.translate("INSPECTOR", u"PANEL 3", None))
        self.label_4.setText(QCoreApplication.translate("INSPECTOR", u"EMA CONTROLS", None))
        self.displayEmaPanel1PushButton.setText(QCoreApplication.translate("INSPECTOR", u"show panel 1", None))
        self.displayEmaPanel2PushButton.setText(QCoreApplication.translate("INSPECTOR", u"show panel 2", None))
        self.displayEmaPanel3PushButton.setText(QCoreApplication.translate("INSPECTOR", u"show panel 3", None))
        self.addChannelToEmaControlTableButton.setText(QCoreApplication.translate("INSPECTOR", u"+", None))
        self.removeChannelFromEmaControlTableButton.setText(QCoreApplication.translate("INSPECTOR", u"-", None))
        self.label_5.setText(QCoreApplication.translate("INSPECTOR", u"LANDMARK CONTROLS", None))
        self.addLandmarkButton.setText(QCoreApplication.translate("INSPECTOR", u"add", None))
        self.removeLandmarkButton.setText(QCoreApplication.translate("INSPECTOR", u"remove", None))
        self.renameLandmarkButton.setText(QCoreApplication.translate("INSPECTOR", u"rename", None))
        self.selectRegionButton.setText(QCoreApplication.translate("INSPECTOR", u"select region", None))
        self.selectLandmarkDetectionComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"vel20", None))
        self.selectLandmarkDetectionComboBox.setItemText(1, QCoreApplication.translate("INSPECTOR", u"vel15", None))
        self.selectLandmarkDetectionComboBox.setItemText(2, QCoreApplication.translate("INSPECTOR", u"tvel20_xy", None))
        self.selectLandmarkDetectionComboBox.setItemText(3, QCoreApplication.translate("INSPECTOR", u"tvel20_xz", None))
        self.selectLandmarkDetectionComboBox.setItemText(4, QCoreApplication.translate("INSPECTOR", u"tvel15_xy", None))
        self.selectLandmarkDetectionComboBox.setItemText(5, QCoreApplication.translate("INSPECTOR", u"tvel15_xz", None))
        self.selectLandmarkDetectionComboBox.setItemText(6, QCoreApplication.translate("INSPECTOR", u"acc", None))

        self.label_6.setText(QCoreApplication.translate("INSPECTOR", u"detection algorithm:", None))
        self.label_17.setText(QCoreApplication.translate("INSPECTOR", u"LANDMARK TIER CONTROLS", None))
        self.emaPanel3SelectTierComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"new", None))

        self.emaPanel2SelectTierComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"new", None))

        self.label_10.setText(QCoreApplication.translate("INSPECTOR", u"show", None))
        self.emaPanel1SelectTierComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR", u"new", None))

        self.label_15.setText(QCoreApplication.translate("INSPECTOR", u"edit tier name", None))
        self.label_14.setText(QCoreApplication.translate("INSPECTOR", u"tier", None))
        self.removeTierButton.setText(QCoreApplication.translate("INSPECTOR", u"remove", None))
        self.emaPanel1DisplayLandmarksPushButton.setText(QCoreApplication.translate("INSPECTOR", u"1", None))
        self.emaPanel2DisplayLandmarksPushButton.setText(QCoreApplication.translate("INSPECTOR", u"2", None))
        self.emaPanel3DisplayLandmarksPushButton.setText(QCoreApplication.translate("INSPECTOR", u"3", None))
        self.storeLandmarksButton.setText(QCoreApplication.translate("INSPECTOR", u"store", None))
    # retranslateUi

