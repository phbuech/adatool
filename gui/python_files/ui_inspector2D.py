# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_inspector2D.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTableWidget, QTableWidgetItem, QToolBox, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_INSPECTOR2D(object):
    def setupUi(self, INSPECTOR2D):
        if not INSPECTOR2D.objectName():
            INSPECTOR2D.setObjectName(u"INSPECTOR2D")
        INSPECTOR2D.resize(1310, 890)
        self.centralwidget = QWidget(INSPECTOR2D)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSplitter = QSplitter(self.centralwidget)
        self.verticalSplitter.setObjectName(u"verticalSplitter")
        self.verticalSplitter.setOrientation(Qt.Vertical)
        self.verticalSplitter.setOpaqueResize(False)
        self.verticalSplitter.setHandleWidth(20)
        self.verticalSplitter.setChildrenCollapsible(False)
        self.verticalLayoutWidget_4 = QWidget(self.verticalSplitter)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.line = QFrame(self.verticalLayoutWidget_4)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.waveformSplitter = QSplitter(self.verticalLayoutWidget_4)
        self.waveformSplitter.setObjectName(u"waveformSplitter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.waveformSplitter.sizePolicy().hasHeightForWidth())
        self.waveformSplitter.setSizePolicy(sizePolicy2)
        self.waveformSplitter.setMinimumSize(QSize(10, 0))
        self.waveformSplitter.setFrameShadow(QFrame.Raised)
        self.waveformSplitter.setLineWidth(10)
        self.waveformSplitter.setMidLineWidth(5)
        self.waveformSplitter.setOrientation(Qt.Horizontal)
        self.waveformSplitter.setOpaqueResize(False)
        self.waveformSplitter.setHandleWidth(20)
        self.waveformSplitter.setChildrenCollapsible(False)
        self.layoutWidget_3 = QWidget(self.waveformSplitter)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.waveformPlotWidget = PlotWidget(self.layoutWidget_3)
        self.waveformPlotWidget.setObjectName(u"waveformPlotWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.waveformPlotWidget.sizePolicy().hasHeightForWidth())
        self.waveformPlotWidget.setSizePolicy(sizePolicy3)
        self.waveformPlotWidget.setMinimumSize(QSize(0, 100))
        self.waveformPlotWidget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.waveformPlotWidget)

        self.spectrogramFrame = QFrame(self.layoutWidget_3)
        self.spectrogramFrame.setObjectName(u"spectrogramFrame")
        self.spectrogramFrame.setFrameShape(QFrame.StyledPanel)
        self.spectrogramFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.spectrogramFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.spectrogramWidget = PlotWidget(self.spectrogramFrame)
        self.spectrogramWidget.setObjectName(u"spectrogramWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.spectrogramWidget.sizePolicy().hasHeightForWidth())
        self.spectrogramWidget.setSizePolicy(sizePolicy4)
        self.spectrogramWidget.setMinimumSize(QSize(0, 0))
        self.spectrogramWidget.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_12.addWidget(self.spectrogramWidget)


        self.verticalLayout_3.addWidget(self.spectrogramFrame)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.waveformSlider = QScrollBar(self.layoutWidget_3)
        self.waveformSlider.setObjectName(u"waveformSlider")
        self.waveformSlider.setMinimumSize(QSize(0, 15))
        self.waveformSlider.setMaximum(200)
        self.waveformSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.waveformSlider)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.zoomAllButton = QPushButton(self.layoutWidget_3)
        self.zoomAllButton.setObjectName(u"zoomAllButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.zoomAllButton.sizePolicy().hasHeightForWidth())
        self.zoomAllButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.zoomAllButton)

        self.zoomOutButton = QPushButton(self.layoutWidget_3)
        self.zoomOutButton.setObjectName(u"zoomOutButton")
        sizePolicy.setHeightForWidth(self.zoomOutButton.sizePolicy().hasHeightForWidth())
        self.zoomOutButton.setSizePolicy(sizePolicy)
        self.zoomOutButton.setMinimumSize(QSize(0, 19))
        self.zoomOutButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.zoomOutButton)

        self.zoomInButton = QPushButton(self.layoutWidget_3)
        self.zoomInButton.setObjectName(u"zoomInButton")
        self.zoomInButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.zoomInButton)

        self.zoomSelectionButton = QPushButton(self.layoutWidget_3)
        self.zoomSelectionButton.setObjectName(u"zoomSelectionButton")

        self.horizontalLayout_4.addWidget(self.zoomSelectionButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.PLAY_AUDIO = QPushButton(self.layoutWidget_3)
        self.PLAY_AUDIO.setObjectName(u"PLAY_AUDIO")
        self.PLAY_AUDIO.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.PLAY_AUDIO)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.waveformSplitter.addWidget(self.layoutWidget_3)
        self.verticalLayoutWidget = QWidget(self.waveformSplitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.displayAnnotationPushButton = QPushButton(self.verticalLayoutWidget)
        self.displayAnnotationPushButton.setObjectName(u"displayAnnotationPushButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.displayAnnotationPushButton.sizePolicy().hasHeightForWidth())
        self.displayAnnotationPushButton.setSizePolicy(sizePolicy7)
        self.displayAnnotationPushButton.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.displayAnnotationPushButton)

        self.audioAnnotationComboBox = QComboBox(self.verticalLayoutWidget)
        self.audioAnnotationComboBox.addItem("")
        self.audioAnnotationComboBox.setObjectName(u"audioAnnotationComboBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.audioAnnotationComboBox.sizePolicy().hasHeightForWidth())
        self.audioAnnotationComboBox.setSizePolicy(sizePolicy8)

        self.horizontalLayout_5.addWidget(self.audioAnnotationComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.line_4 = QFrame(self.verticalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_4)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.showSpectrogramButton = QPushButton(self.verticalLayoutWidget)
        self.showSpectrogramButton.setObjectName(u"showSpectrogramButton")
        self.showSpectrogramButton.setCheckable(True)

        self.verticalLayout.addWidget(self.showSpectrogramButton)

        self.toolBox = QToolBox(self.verticalLayoutWidget)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy5.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy5)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.toolBox.setFont(font)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(True)
        self.toolBox.setFrameShadow(QFrame.Plain)
        self.toolBox.setLineWidth(1)
        self.toolBox.setMidLineWidth(0)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 525, 69))
        self.horizontalLayout_20 = QHBoxLayout(self.page_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setSizeConstraint(QLayout.SetMinimumSize)
        self.showFundamentalFrequencyButton = QPushButton(self.page_5)
        self.showFundamentalFrequencyButton.setObjectName(u"showFundamentalFrequencyButton")
        sizePolicy7.setHeightForWidth(self.showFundamentalFrequencyButton.sizePolicy().hasHeightForWidth())
        self.showFundamentalFrequencyButton.setSizePolicy(sizePolicy7)
        self.showFundamentalFrequencyButton.setMinimumSize(QSize(75, 0))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.showFundamentalFrequencyButton.setFont(font1)
        self.showFundamentalFrequencyButton.setCheckable(True)

        self.horizontalLayout_21.addWidget(self.showFundamentalFrequencyButton)

        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)
        self.label_9.setMinimumSize(QSize(50, 0))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_9)

        self.fundamentalFrequencyComboBox = QComboBox(self.page_5)
        self.fundamentalFrequencyComboBox.addItem("")
        self.fundamentalFrequencyComboBox.addItem("")
        self.fundamentalFrequencyComboBox.setObjectName(u"fundamentalFrequencyComboBox")
        sizePolicy5.setHeightForWidth(self.fundamentalFrequencyComboBox.sizePolicy().hasHeightForWidth())
        self.fundamentalFrequencyComboBox.setSizePolicy(sizePolicy5)
        self.fundamentalFrequencyComboBox.setFont(font1)

        self.horizontalLayout_21.addWidget(self.fundamentalFrequencyComboBox)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)

        self.toolBox.addItem(self.page_5, u"FUNDAMENTAL FREQUENCY")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 525, 69))
        self.horizontalLayout_22 = QHBoxLayout(self.page_6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.showIntensityButton = QPushButton(self.page_6)
        self.showIntensityButton.setObjectName(u"showIntensityButton")
        sizePolicy7.setHeightForWidth(self.showIntensityButton.sizePolicy().hasHeightForWidth())
        self.showIntensityButton.setSizePolicy(sizePolicy7)
        self.showIntensityButton.setMinimumSize(QSize(75, 0))
        self.showIntensityButton.setFont(font1)
        self.showIntensityButton.setCheckable(True)

        self.horizontalLayout_23.addWidget(self.showIntensityButton)

        self.label_19 = QLabel(self.page_6)
        self.label_19.setObjectName(u"label_19")
        sizePolicy6.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy6)
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_19)

        self.intensityComboBox = QComboBox(self.page_6)
        self.intensityComboBox.addItem("")
        self.intensityComboBox.setObjectName(u"intensityComboBox")
        sizePolicy5.setHeightForWidth(self.intensityComboBox.sizePolicy().hasHeightForWidth())
        self.intensityComboBox.setSizePolicy(sizePolicy5)
        self.intensityComboBox.setFont(font1)

        self.horizontalLayout_23.addWidget(self.intensityComboBox)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_23)

        self.toolBox.addItem(self.page_6, u"INTENSITY")

        self.verticalLayout.addWidget(self.toolBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.waveformSplitter.addWidget(self.verticalLayoutWidget)

        self.verticalLayout_6.addWidget(self.waveformSplitter)

        self.verticalSplitter.addWidget(self.verticalLayoutWidget_4)
        self.verticalLayoutWidget_3 = QWidget(self.verticalSplitter)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.line_5 = QFrame(self.verticalLayoutWidget_3)
        self.line_5.setObjectName(u"line_5")
        sizePolicy1.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy1)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.emaSplitter = QSplitter(self.verticalLayoutWidget_3)
        self.emaSplitter.setObjectName(u"emaSplitter")
        sizePolicy2.setHeightForWidth(self.emaSplitter.sizePolicy().hasHeightForWidth())
        self.emaSplitter.setSizePolicy(sizePolicy2)
        self.emaSplitter.setMinimumSize(QSize(10, 0))
        self.emaSplitter.setFrameShadow(QFrame.Raised)
        self.emaSplitter.setLineWidth(10)
        self.emaSplitter.setMidLineWidth(5)
        self.emaSplitter.setOrientation(Qt.Horizontal)
        self.emaSplitter.setOpaqueResize(False)
        self.emaSplitter.setHandleWidth(20)
        self.emaSplitter.setChildrenCollapsible(False)
        self.verticalLayoutWidget_2 = QWidget(self.emaSplitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.emaPanel1 = QFrame(self.verticalLayoutWidget_2)
        self.emaPanel1.setObjectName(u"emaPanel1")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.emaPanel1.sizePolicy().hasHeightForWidth())
        self.emaPanel1.setSizePolicy(sizePolicy9)
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
        self.emaPlotWidget1 = PlotWidget(self.emaPanel1)
        self.emaPlotWidget1.setObjectName(u"emaPlotWidget1")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.emaPlotWidget1.sizePolicy().hasHeightForWidth())
        self.emaPlotWidget1.setSizePolicy(sizePolicy10)

        self.verticalLayout_16.addWidget(self.emaPlotWidget1)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.verticalLayout_2.addWidget(self.emaPanel1)

        self.emaSplitter.addWidget(self.verticalLayoutWidget_2)
        self.layoutWidget_2 = QWidget(self.emaSplitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.line_3 = QFrame(self.layoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.selectDimensionComboBox1 = QComboBox(self.layoutWidget_2)
        self.selectDimensionComboBox1.setObjectName(u"selectDimensionComboBox1")

        self.horizontalLayout.addWidget(self.selectDimensionComboBox1)

        self.selectDimensionComboBox2 = QComboBox(self.layoutWidget_2)
        self.selectDimensionComboBox2.setObjectName(u"selectDimensionComboBox2")

        self.horizontalLayout.addWidget(self.selectDimensionComboBox2)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.emaControlTable = QTableWidget(self.layoutWidget_2)
        self.emaControlTable.setObjectName(u"emaControlTable")
        sizePolicy3.setHeightForWidth(self.emaControlTable.sizePolicy().hasHeightForWidth())
        self.emaControlTable.setSizePolicy(sizePolicy3)

        self.verticalLayout_10.addWidget(self.emaControlTable)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.addChannelToEmaControlTableButton = QPushButton(self.layoutWidget_2)
        self.addChannelToEmaControlTableButton.setObjectName(u"addChannelToEmaControlTableButton")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.addChannelToEmaControlTableButton.sizePolicy().hasHeightForWidth())
        self.addChannelToEmaControlTableButton.setSizePolicy(sizePolicy11)
        self.addChannelToEmaControlTableButton.setMinimumSize(QSize(0, 20))
        self.addChannelToEmaControlTableButton.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_9.addWidget(self.addChannelToEmaControlTableButton)

        self.removeChannelFromEmaControlTableButton = QPushButton(self.layoutWidget_2)
        self.removeChannelFromEmaControlTableButton.setObjectName(u"removeChannelFromEmaControlTableButton")
        sizePolicy11.setHeightForWidth(self.removeChannelFromEmaControlTableButton.sizePolicy().hasHeightForWidth())
        self.removeChannelFromEmaControlTableButton.setSizePolicy(sizePolicy11)
        self.removeChannelFromEmaControlTableButton.setMinimumSize(QSize(0, 20))
        self.removeChannelFromEmaControlTableButton.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_9.addWidget(self.removeChannelFromEmaControlTableButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.sizeSlider = QScrollBar(self.layoutWidget_2)
        self.sizeSlider.setObjectName(u"sizeSlider")
        self.sizeSlider.setMinimumSize(QSize(0, 15))
        self.sizeSlider.setMinimum(10)
        self.sizeSlider.setMaximum(50)
        self.sizeSlider.setPageStep(1)
        self.sizeSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.sizeSlider, 1, 1, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.plotTracePushButton = QPushButton(self.layoutWidget_2)
        self.plotTracePushButton.setObjectName(u"plotTracePushButton")
        self.plotTracePushButton.setCheckable(True)

        self.verticalLayout_7.addWidget(self.plotTracePushButton)

        self.addLabelsPushButton = QPushButton(self.layoutWidget_2)
        self.addLabelsPushButton.setObjectName(u"addLabelsPushButton")
        self.addLabelsPushButton.setCheckable(True)

        self.verticalLayout_7.addWidget(self.addLabelsPushButton)

        self.plotTongueShapePushButton = QPushButton(self.layoutWidget_2)
        self.plotTongueShapePushButton.setObjectName(u"plotTongueShapePushButton")
        self.plotTongueShapePushButton.setCheckable(True)

        self.verticalLayout_7.addWidget(self.plotTongueShapePushButton)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.emaSplitter.addWidget(self.layoutWidget_2)

        self.verticalLayout_4.addWidget(self.emaSplitter)

        self.verticalSplitter.addWidget(self.verticalLayoutWidget_3)

        self.gridLayout.addWidget(self.verticalSplitter, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        INSPECTOR2D.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(INSPECTOR2D)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1310, 28))
        INSPECTOR2D.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(INSPECTOR2D)
        self.statusbar.setObjectName(u"statusbar")
        INSPECTOR2D.setStatusBar(self.statusbar)

        self.retranslateUi(INSPECTOR2D)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(1)


        QMetaObject.connectSlotsByName(INSPECTOR2D)
    # setupUi

    def retranslateUi(self, INSPECTOR2D):
        INSPECTOR2D.setWindowTitle(QCoreApplication.translate("INSPECTOR2D", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("INSPECTOR2D", u"WAVEFORM", None))
        self.zoomAllButton.setText(QCoreApplication.translate("INSPECTOR2D", u"all", None))
        self.zoomOutButton.setText(QCoreApplication.translate("INSPECTOR2D", u"zoom out", None))
        self.zoomInButton.setText(QCoreApplication.translate("INSPECTOR2D", u"zoom in", None))
        self.zoomSelectionButton.setText(QCoreApplication.translate("INSPECTOR2D", u"selection", None))
        self.PLAY_AUDIO.setText(QCoreApplication.translate("INSPECTOR2D", u"play", None))
        self.label_2.setText(QCoreApplication.translate("INSPECTOR2D", u"WAVEFORM CONTROLS", None))
        self.displayAnnotationPushButton.setText("")
        self.audioAnnotationComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR2D", u"Tiers", None))

        self.label_8.setText(QCoreApplication.translate("INSPECTOR2D", u"SPECTROGRAM CONTROLS", None))
        self.showSpectrogramButton.setText(QCoreApplication.translate("INSPECTOR2D", u"spectrogram", None))
        self.showFundamentalFrequencyButton.setText("")
        self.label_9.setText(QCoreApplication.translate("INSPECTOR2D", u" estimation:", None))
        self.fundamentalFrequencyComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR2D", u"pYin", None))
        self.fundamentalFrequencyComboBox.setItemText(1, QCoreApplication.translate("INSPECTOR2D", u"Yin", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("INSPECTOR2D", u"FUNDAMENTAL FREQUENCY", None))
        self.showIntensityButton.setText("")
        self.label_19.setText(QCoreApplication.translate("INSPECTOR2D", u"estimation:", None))
        self.intensityComboBox.setItemText(0, QCoreApplication.translate("INSPECTOR2D", u"rms", None))

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("INSPECTOR2D", u"INTENSITY", None))
        self.label_6.setText(QCoreApplication.translate("INSPECTOR2D", u"EMA", None))
        self.label_4.setText(QCoreApplication.translate("INSPECTOR2D", u"PLOTTING CONTROLS", None))
        self.label_5.setText(QCoreApplication.translate("INSPECTOR2D", u"dimensions:", None))
        self.addChannelToEmaControlTableButton.setText(QCoreApplication.translate("INSPECTOR2D", u"+", None))
        self.removeChannelFromEmaControlTableButton.setText(QCoreApplication.translate("INSPECTOR2D", u"-", None))
        self.label_7.setText(QCoreApplication.translate("INSPECTOR2D", u"point size", None))
        self.plotTracePushButton.setText(QCoreApplication.translate("INSPECTOR2D", u"plot trace", None))
        self.addLabelsPushButton.setText(QCoreApplication.translate("INSPECTOR2D", u"add labels", None))
        self.plotTongueShapePushButton.setText(QCoreApplication.translate("INSPECTOR2D", u"plot tongue shape", None))
    # retranslateUi

