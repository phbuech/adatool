# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_measurements.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MEASUREMENTS(object):
    def setupUi(self, MEASUREMENTS):
        if not MEASUREMENTS.objectName():
            MEASUREMENTS.setObjectName(u"MEASUREMENTS")
        MEASUREMENTS.resize(946, 687)
        self.gridLayout_2 = QGridLayout(MEASUREMENTS)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progressBar = QProgressBar(MEASUREMENTS)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selectionTreeWidget = QTreeWidget(MEASUREMENTS)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.selectionTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.selectionTreeWidget.setObjectName(u"selectionTreeWidget")
        self.selectionTreeWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.selectionTreeWidget.setFrameShape(QFrame.StyledPanel)
        self.selectionTreeWidget.setAutoExpandDelay(0)

        self.verticalLayout.addWidget(self.selectionTreeWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addTargetButton = QPushButton(MEASUREMENTS)
        self.addTargetButton.setObjectName(u"addTargetButton")

        self.horizontalLayout_2.addWidget(self.addTargetButton)

        self.removeTargetButton = QPushButton(MEASUREMENTS)
        self.removeTargetButton.setObjectName(u"removeTargetButton")

        self.horizontalLayout_2.addWidget(self.removeTargetButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addSegmentButton = QPushButton(MEASUREMENTS)
        self.addSegmentButton.setObjectName(u"addSegmentButton")

        self.horizontalLayout.addWidget(self.addSegmentButton)

        self.removeSegmentButton = QPushButton(MEASUREMENTS)
        self.removeSegmentButton.setObjectName(u"removeSegmentButton")

        self.horizontalLayout.addWidget(self.removeSegmentButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.runMeasurementsButton = QPushButton(MEASUREMENTS)
        self.runMeasurementsButton.setObjectName(u"runMeasurementsButton")

        self.gridLayout_2.addWidget(self.runMeasurementsButton, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(MEASUREMENTS)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.line = QFrame(MEASUREMENTS)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.landmarkAllocationComboBox_5 = QComboBox(MEASUREMENTS)
        self.landmarkAllocationComboBox_5.setObjectName(u"landmarkAllocationComboBox_5")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_5, 4, 1, 1, 1)

        self.landmarkLineEdit_4 = QLineEdit(MEASUREMENTS)
        self.landmarkLineEdit_4.setObjectName(u"landmarkLineEdit_4")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_4, 3, 2, 1, 1)

        self.landmarkAllocationComboBox_1 = QComboBox(MEASUREMENTS)
        self.landmarkAllocationComboBox_1.setObjectName(u"landmarkAllocationComboBox_1")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_1, 0, 1, 1, 1)

        self.landmarkCheckBox_2 = QCheckBox(MEASUREMENTS)
        self.landmarkCheckBox_2.setObjectName(u"landmarkCheckBox_2")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_2, 1, 0, 1, 1)

        self.landmarkAllocationComboBox_2 = QComboBox(MEASUREMENTS)
        self.landmarkAllocationComboBox_2.setObjectName(u"landmarkAllocationComboBox_2")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_2, 1, 1, 1, 1)

        self.landmarkCheckBox_1 = QCheckBox(MEASUREMENTS)
        self.landmarkCheckBox_1.setObjectName(u"landmarkCheckBox_1")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_1, 0, 0, 1, 1)

        self.landmarkAllocationComboBox_4 = QComboBox(MEASUREMENTS)
        self.landmarkAllocationComboBox_4.setObjectName(u"landmarkAllocationComboBox_4")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_4, 3, 1, 1, 1)

        self.landmarkLineEdit_3 = QLineEdit(MEASUREMENTS)
        self.landmarkLineEdit_3.setObjectName(u"landmarkLineEdit_3")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_3, 2, 2, 1, 1)

        self.landmarkCheckBox_5 = QCheckBox(MEASUREMENTS)
        self.landmarkCheckBox_5.setObjectName(u"landmarkCheckBox_5")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_5, 4, 0, 1, 1)

        self.landmarkLineEdit_5 = QLineEdit(MEASUREMENTS)
        self.landmarkLineEdit_5.setObjectName(u"landmarkLineEdit_5")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_5, 4, 2, 1, 1)

        self.landmarkAllocationComboBox_6 = QComboBox(MEASUREMENTS)
        self.landmarkAllocationComboBox_6.setObjectName(u"landmarkAllocationComboBox_6")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_6, 5, 1, 1, 1)

        self.landmarkCheckBox_3 = QCheckBox(MEASUREMENTS)
        self.landmarkCheckBox_3.setObjectName(u"landmarkCheckBox_3")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_3, 2, 0, 1, 1)

        self.landmarkLineEdit_2 = QLineEdit(MEASUREMENTS)
        self.landmarkLineEdit_2.setObjectName(u"landmarkLineEdit_2")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_2, 1, 2, 1, 1)

        self.landmarkCheckBox_4 = QCheckBox(MEASUREMENTS)
        self.landmarkCheckBox_4.setObjectName(u"landmarkCheckBox_4")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_4, 3, 0, 1, 1)

        self.landmarkLineEdit_1 = QLineEdit(MEASUREMENTS)
        self.landmarkLineEdit_1.setObjectName(u"landmarkLineEdit_1")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_1, 0, 2, 1, 1)

        self.landmarkCheckBox_6 = QCheckBox(MEASUREMENTS)
        self.landmarkCheckBox_6.setObjectName(u"landmarkCheckBox_6")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_6, 5, 0, 1, 1)

        self.landmarkAllocationComboBox_3 = QComboBox(MEASUREMENTS)
        self.landmarkAllocationComboBox_3.setObjectName(u"landmarkAllocationComboBox_3")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_3, 2, 1, 1, 1)

        self.landmarkLineEdit_6 = QLineEdit(MEASUREMENTS)
        self.landmarkLineEdit_6.setObjectName(u"landmarkLineEdit_6")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_6, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(MEASUREMENTS)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(MEASUREMENTS)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.line_3 = QFrame(MEASUREMENTS)
        self.line_3.setObjectName(u"line_3")
        sizePolicy1.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy1)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.measurementsTableWidget = QTableWidget(MEASUREMENTS)
        self.measurementsTableWidget.setObjectName(u"measurementsTableWidget")

        self.verticalLayout_3.addWidget(self.measurementsTableWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.addMeasurementButton = QPushButton(MEASUREMENTS)
        self.addMeasurementButton.setObjectName(u"addMeasurementButton")

        self.horizontalLayout_5.addWidget(self.addMeasurementButton)

        self.removeMeasurementButton = QPushButton(MEASUREMENTS)
        self.removeMeasurementButton.setObjectName(u"removeMeasurementButton")

        self.horizontalLayout_5.addWidget(self.removeMeasurementButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.massSpringParametersRadioButton = QRadioButton(MEASUREMENTS)
        self.massSpringParametersRadioButton.setObjectName(u"massSpringParametersRadioButton")
        self.massSpringParametersRadioButton.setChecked(True)

        self.gridLayout_4.addWidget(self.massSpringParametersRadioButton, 0, 0, 1, 1)

        self.trajectoriesRadioButton = QRadioButton(MEASUREMENTS)
        self.trajectoriesRadioButton.setObjectName(u"trajectoriesRadioButton")
        self.trajectoriesRadioButton.setChecked(False)

        self.gridLayout_4.addWidget(self.trajectoriesRadioButton, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.storeMeasurementsButton = QPushButton(MEASUREMENTS)
        self.storeMeasurementsButton.setObjectName(u"storeMeasurementsButton")

        self.gridLayout_2.addWidget(self.storeMeasurementsButton, 4, 0, 1, 1)


        self.retranslateUi(MEASUREMENTS)

        QMetaObject.connectSlotsByName(MEASUREMENTS)
    # setupUi

    def retranslateUi(self, MEASUREMENTS):
        MEASUREMENTS.setWindowTitle(QCoreApplication.translate("MEASUREMENTS", u"Form", None))
        self.addTargetButton.setText(QCoreApplication.translate("MEASUREMENTS", u"add target", None))
        self.removeTargetButton.setText(QCoreApplication.translate("MEASUREMENTS", u"remove target", None))
        self.addSegmentButton.setText(QCoreApplication.translate("MEASUREMENTS", u"add segment", None))
        self.removeSegmentButton.setText(QCoreApplication.translate("MEASUREMENTS", u"remove segment", None))
        self.runMeasurementsButton.setText(QCoreApplication.translate("MEASUREMENTS", u"conduct measurements", None))
        self.label.setText(QCoreApplication.translate("MEASUREMENTS", u"LANDMARK NAME SPECIFICATION", None))
        self.landmarkCheckBox_2.setText("")
        self.landmarkCheckBox_1.setText("")
        self.landmarkCheckBox_5.setText("")
        self.landmarkCheckBox_3.setText("")
        self.landmarkCheckBox_4.setText("")
        self.landmarkCheckBox_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MEASUREMENTS", u"MEASUREMENTS", None))
        self.addMeasurementButton.setText(QCoreApplication.translate("MEASUREMENTS", u"add measurement", None))
        self.removeMeasurementButton.setText(QCoreApplication.translate("MEASUREMENTS", u"remove measurement", None))
        self.massSpringParametersRadioButton.setText(QCoreApplication.translate("MEASUREMENTS", u"mass-spring parameters", None))
        self.trajectoriesRadioButton.setText(QCoreApplication.translate("MEASUREMENTS", u"trajectories", None))
        self.storeMeasurementsButton.setText(QCoreApplication.translate("MEASUREMENTS", u"store measurements", None))
    # retranslateUi

