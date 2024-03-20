# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1497, 1058)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionimport_corpus = QAction(MainWindow)
        self.actionimport_corpus.setObjectName(u"actionimport_corpus")
        self.actionas = QAction(MainWindow)
        self.actionas.setObjectName(u"actionas")
        self.actionexport_EMA_to_netcdf = QAction(MainWindow)
        self.actionexport_EMA_to_netcdf.setObjectName(u"actionexport_EMA_to_netcdf")
        self.actionexport_EMA_to_csv = QAction(MainWindow)
        self.actionexport_EMA_to_csv.setObjectName(u"actionexport_EMA_to_csv")
        self.actionexport_landmarks_to_TextGrid = QAction(MainWindow)
        self.actionexport_landmarks_to_TextGrid.setObjectName(u"actionexport_landmarks_to_TextGrid")
        self.actionexport_landmarks_to_csv = QAction(MainWindow)
        self.actionexport_landmarks_to_csv.setObjectName(u"actionexport_landmarks_to_csv")
        self.actionexport_landmarks_to_JSON = QAction(MainWindow)
        self.actionexport_landmarks_to_JSON.setObjectName(u"actionexport_landmarks_to_JSON")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dataList = QListWidget(self.centralwidget)
        self.dataList.setObjectName(u"dataList")
        self.dataList.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout.addWidget(self.dataList)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addFilesToDataListButton = QPushButton(self.centralwidget)
        self.addFilesToDataListButton.setObjectName(u"addFilesToDataListButton")

        self.horizontalLayout_2.addWidget(self.addFilesToDataListButton)

        self.removeFilesFromDataListButton = QPushButton(self.centralwidget)
        self.removeFilesFromDataListButton.setObjectName(u"removeFilesFromDataListButton")

        self.horizontalLayout_2.addWidget(self.removeFilesFromDataListButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_6)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy2)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_9)


        self.verticalLayout_14.addLayout(self.horizontalLayout)

        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_14.addWidget(self.comboBox_4)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_8.addWidget(self.comboBox_3, 1, 2, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_8.addWidget(self.comboBox, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_8.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 0, 2, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_8)


        self.verticalLayout.addLayout(self.verticalLayout_14)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 0, 3, 1, 1)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.label)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.emaChannelInfoLabel = QLabel(self.centralwidget)
        self.emaChannelInfoLabel.setObjectName(u"emaChannelInfoLabel")

        self.gridLayout_3.addWidget(self.emaChannelInfoLabel, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.emaDeviceInfoLabel = QLabel(self.centralwidget)
        self.emaDeviceInfoLabel.setObjectName(u"emaDeviceInfoLabel")

        self.gridLayout_3.addWidget(self.emaDeviceInfoLabel, 0, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.emaSamplerateInfoLabel = QLabel(self.centralwidget)
        self.emaSamplerateInfoLabel.setObjectName(u"emaSamplerateInfoLabel")

        self.gridLayout_3.addWidget(self.emaSamplerateInfoLabel, 1, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.emaDurationInfoLabel = QLabel(self.centralwidget)
        self.emaDurationInfoLabel.setObjectName(u"emaDurationInfoLabel")

        self.gridLayout_3.addWidget(self.emaDurationInfoLabel, 3, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        sizePolicy2.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.audioSamplerateInfoLabel = QLabel(self.centralwidget)
        self.audioSamplerateInfoLabel.setObjectName(u"audioSamplerateInfoLabel")

        self.gridLayout_4.addWidget(self.audioSamplerateInfoLabel, 0, 1, 1, 1)

        self.audioDurationInfoLabel = QLabel(self.centralwidget)
        self.audioDurationInfoLabel.setObjectName(u"audioDurationInfoLabel")

        self.gridLayout_4.addWidget(self.audioDurationInfoLabel, 1, 1, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        sizePolicy2.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy2)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.annotationTierNumberInfoLabel = QLabel(self.centralwidget)
        self.annotationTierNumberInfoLabel.setObjectName(u"annotationTierNumberInfoLabel")
        self.annotationTierNumberInfoLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.annotationTierNumberInfoLabel, 0, 1, 1, 1)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_5)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tierList = QTableWidget(self.centralwidget)
        self.tierList.setObjectName(u"tierList")

        self.verticalLayout_15.addWidget(self.tierList)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.addTierNameToTierListButton = QPushButton(self.centralwidget)
        self.addTierNameToTierListButton.setObjectName(u"addTierNameToTierListButton")
        self.addTierNameToTierListButton.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.addTierNameToTierListButton)

        self.removeTierNameFromTierListButton = QPushButton(self.centralwidget)
        self.removeTierNameFromTierListButton.setObjectName(u"removeTierNameFromTierListButton")
        self.removeTierNameFromTierListButton.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.removeTierNameFromTierListButton)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addLayout(self.verticalLayout_15)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.openInspectorWindowButton = QPushButton(self.centralwidget)
        self.openInspectorWindowButton.setObjectName(u"openInspectorWindowButton")

        self.verticalLayout_6.addWidget(self.openInspectorWindowButton)

        self.open2DInspectorWindowButton = QPushButton(self.centralwidget)
        self.open2DInspectorWindowButton.setObjectName(u"open2DInspectorWindowButton")

        self.verticalLayout_6.addWidget(self.open2DInspectorWindowButton)

        self.open3DInspectorWindowButton = QPushButton(self.centralwidget)
        self.open3DInspectorWindowButton.setObjectName(u"open3DInspectorWindowButton")
        self.open3DInspectorWindowButton.setEnabled(False)

        self.verticalLayout_6.addWidget(self.open3DInspectorWindowButton)

        self.landmarkDetectionButton = QPushButton(self.centralwidget)
        self.landmarkDetectionButton.setObjectName(u"landmarkDetectionButton")

        self.verticalLayout_6.addWidget(self.landmarkDetectionButton)

        self.measurementsButton = QPushButton(self.centralwidget)
        self.measurementsButton.setObjectName(u"measurementsButton")

        self.verticalLayout_6.addWidget(self.measurementsButton)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_18)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        sizePolicy2.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy2)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.channelTable = QTableWidget(self.centralwidget)
        self.channelTable.setObjectName(u"channelTable")

        self.verticalLayout_9.addWidget(self.channelTable)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addChannelToChannelTableButton = QPushButton(self.centralwidget)
        self.addChannelToChannelTableButton.setObjectName(u"addChannelToChannelTableButton")

        self.horizontalLayout_7.addWidget(self.addChannelToChannelTableButton)

        self.removeChannelFromChannelTableButton = QPushButton(self.centralwidget)
        self.removeChannelFromChannelTableButton.setObjectName(u"removeChannelFromChannelTableButton")

        self.horizontalLayout_7.addWidget(self.removeChannelFromChannelTableButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.label_19)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        sizePolicy2.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy2)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.headCorrectionList = QTableWidget(self.centralwidget)
        self.headCorrectionList.setObjectName(u"headCorrectionList")

        self.verticalLayout_11.addWidget(self.headCorrectionList)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.addChannelToHeadCorrectionListButton = QPushButton(self.centralwidget)
        self.addChannelToHeadCorrectionListButton.setObjectName(u"addChannelToHeadCorrectionListButton")
        self.addChannelToHeadCorrectionListButton.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.addChannelToHeadCorrectionListButton)

        self.removeChannelFromHeadCorrectionListButton = QPushButton(self.centralwidget)
        self.removeChannelFromHeadCorrectionListButton.setObjectName(u"removeChannelFromHeadCorrectionListButton")
        self.removeChannelFromHeadCorrectionListButton.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.removeChannelFromHeadCorrectionListButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_10.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)

        self.gridLayout_6.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(False)

        self.gridLayout_6.addWidget(self.radioButton_2, 0, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_6)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)

        self.verticalLayout_12.addWidget(self.checkBox)


        self.verticalLayout_10.addLayout(self.verticalLayout_12)


        self.verticalLayout_7.addLayout(self.verticalLayout_10)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.label_20)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        sizePolicy2.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy2)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_6)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.filterRadioButtonMovingAverage = QRadioButton(self.centralwidget)
        self.filterRadioButtonMovingAverage.setObjectName(u"filterRadioButtonMovingAverage")

        self.gridLayout_7.addWidget(self.filterRadioButtonMovingAverage, 1, 0, 1, 1)

        self.filterRadioButtonBWLP = QRadioButton(self.centralwidget)
        self.filterRadioButtonBWLP.setObjectName(u"filterRadioButtonBWLP")

        self.gridLayout_7.addWidget(self.filterRadioButtonBWLP, 2, 0, 1, 1)

        self.filterRadioButtonNone = QRadioButton(self.centralwidget)
        self.filterRadioButtonNone.setObjectName(u"filterRadioButtonNone")
        self.filterRadioButtonNone.setChecked(True)

        self.gridLayout_7.addWidget(self.filterRadioButtonNone, 0, 0, 1, 1)

        self.movingAverageInput = QLineEdit(self.centralwidget)
        self.movingAverageInput.setObjectName(u"movingAverageInput")

        self.gridLayout_7.addWidget(self.movingAverageInput, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.bwLowPassCutoffInput = QLineEdit(self.centralwidget)
        self.bwLowPassCutoffInput.setObjectName(u"bwLowPassCutoffInput")

        self.horizontalLayout_11.addWidget(self.bwLowPassCutoffInput)

        self.bwLowPassOrderInput = QLineEdit(self.centralwidget)
        self.bwLowPassOrderInput.setObjectName(u"bwLowPassOrderInput")

        self.horizontalLayout_11.addWidget(self.bwLowPassOrderInput)


        self.gridLayout_7.addLayout(self.horizontalLayout_11, 2, 1, 1, 1)


        self.verticalLayout_13.addLayout(self.gridLayout_7)


        self.verticalLayout_8.addLayout(self.verticalLayout_13)

        self.testButton = QPushButton(self.centralwidget)
        self.testButton.setObjectName(u"testButton")

        self.verticalLayout_8.addWidget(self.testButton)


        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1497, 28))
        self.menuFiles = QMenu(self.menubar)
        self.menuFiles.setObjectName(u"menuFiles")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuexport = QMenu(self.menubar)
        self.menuexport.setObjectName(u"menuexport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuexport.menuAction())
        self.menuFiles.addAction(self.actionimport_corpus)
        self.menuSettings.addAction(self.actionas)
        self.menuexport.addAction(self.actionexport_EMA_to_netcdf)
        self.menuexport.addAction(self.actionexport_EMA_to_csv)
        self.menuexport.addAction(self.actionexport_landmarks_to_JSON)
        self.menuexport.addAction(self.actionexport_landmarks_to_TextGrid)
        self.menuexport.addAction(self.actionexport_landmarks_to_csv)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionimport_corpus.setText(QCoreApplication.translate("MainWindow", u"import corpus", None))
        self.actionas.setText(QCoreApplication.translate("MainWindow", u"change settings", None))
        self.actionexport_EMA_to_netcdf.setText(QCoreApplication.translate("MainWindow", u"export EMA to netcdf", None))
        self.actionexport_EMA_to_csv.setText(QCoreApplication.translate("MainWindow", u"export EMA to csv", None))
        self.actionexport_landmarks_to_TextGrid.setText(QCoreApplication.translate("MainWindow", u"export landmarks to TextGrid", None))
        self.actionexport_landmarks_to_csv.setText(QCoreApplication.translate("MainWindow", u"export landmarks to csv", None))
        self.actionexport_landmarks_to_JSON.setText(QCoreApplication.translate("MainWindow", u"export landmarks to JSON", None))
        self.addFilesToDataListButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.removeFilesFromDataListButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"INPUT FORMATS", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"EMA", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"TextGrid", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"pos (Carstens)", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"wav", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"EMA", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"AUDIO", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ANNOTATION", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EMA", None))
        self.emaChannelInfoLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sample rate:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Channels:", None))
        self.emaDeviceInfoLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Articulograph:", None))
        self.emaSamplerateInfoLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.emaDurationInfoLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AUDIO", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Sample rate:", None))
        self.audioSamplerateInfoLabel.setText("")
        self.audioDurationInfoLabel.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ANNOTATION", None))
        self.annotationTierNumberInfoLabel.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Number of Tiers:", None))
        self.addTierNameToTierListButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.removeTierNameFromTierListButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.openInspectorWindowButton.setText(QCoreApplication.translate("MainWindow", u"Inspector", None))
        self.open2DInspectorWindowButton.setText(QCoreApplication.translate("MainWindow", u"2D Inspector", None))
        self.open3DInspectorWindowButton.setText(QCoreApplication.translate("MainWindow", u"3D Inspector", None))
        self.landmarkDetectionButton.setText(QCoreApplication.translate("MainWindow", u"Landmark detection", None))
        self.measurementsButton.setText(QCoreApplication.translate("MainWindow", u"Measurements", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"CHANNELS", None))
        self.addChannelToChannelTableButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.removeChannelFromChannelTableButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"HEAD CORRECTION", None))
        self.addChannelToHeadCorrectionListButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.removeChannelFromHeadCorrectionListButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"option 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"option 2", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"apply head correction", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"FILTER", None))
        self.filterRadioButtonMovingAverage.setText(QCoreApplication.translate("MainWindow", u"moving average", None))
        self.filterRadioButtonBWLP.setText(QCoreApplication.translate("MainWindow", u"butterworth lowpass", None))
        self.filterRadioButtonNone.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.movingAverageInput.setText(QCoreApplication.translate("MainWindow", u"window size", None))
        self.bwLowPassCutoffInput.setText(QCoreApplication.translate("MainWindow", u"cutoff", None))
        self.bwLowPassOrderInput.setText(QCoreApplication.translate("MainWindow", u"order", None))
        self.testButton.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuexport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

