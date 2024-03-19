# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_measurements.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(946, 687)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selectionTreeWidget = QTreeWidget(Form)
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
        self.addTargetButton = QPushButton(Form)
        self.addTargetButton.setObjectName(u"addTargetButton")

        self.horizontalLayout_2.addWidget(self.addTargetButton)

        self.removeTargetButton = QPushButton(Form)
        self.removeTargetButton.setObjectName(u"removeTargetButton")

        self.horizontalLayout_2.addWidget(self.removeTargetButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addSegmentButton = QPushButton(Form)
        self.addSegmentButton.setObjectName(u"addSegmentButton")

        self.horizontalLayout.addWidget(self.addSegmentButton)

        self.removeSegmentButton = QPushButton(Form)
        self.removeSegmentButton.setObjectName(u"removeSegmentButton")

        self.horizontalLayout.addWidget(self.removeSegmentButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.runMeasurementsButton = QPushButton(Form)
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
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
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
        self.landmarkAllocationComboBox_5 = QComboBox(Form)
        self.landmarkAllocationComboBox_5.setObjectName(u"landmarkAllocationComboBox_5")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_5, 4, 1, 1, 1)

        self.landmarkLineEdit_4 = QLineEdit(Form)
        self.landmarkLineEdit_4.setObjectName(u"landmarkLineEdit_4")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_4, 3, 2, 1, 1)

        self.landmarkAllocationComboBox_1 = QComboBox(Form)
        self.landmarkAllocationComboBox_1.setObjectName(u"landmarkAllocationComboBox_1")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_1, 0, 1, 1, 1)

        self.landmarkCheckBox_2 = QCheckBox(Form)
        self.landmarkCheckBox_2.setObjectName(u"landmarkCheckBox_2")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_2, 1, 0, 1, 1)

        self.landmarkAllocationComboBox_2 = QComboBox(Form)
        self.landmarkAllocationComboBox_2.setObjectName(u"landmarkAllocationComboBox_2")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_2, 1, 1, 1, 1)

        self.landmarkCheckBox_1 = QCheckBox(Form)
        self.landmarkCheckBox_1.setObjectName(u"landmarkCheckBox_1")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_1, 0, 0, 1, 1)

        self.landmarkAllocationComboBox_4 = QComboBox(Form)
        self.landmarkAllocationComboBox_4.setObjectName(u"landmarkAllocationComboBox_4")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_4, 3, 1, 1, 1)

        self.landmarkLineEdit_3 = QLineEdit(Form)
        self.landmarkLineEdit_3.setObjectName(u"landmarkLineEdit_3")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_3, 2, 2, 1, 1)

        self.landmarkCheckBox_5 = QCheckBox(Form)
        self.landmarkCheckBox_5.setObjectName(u"landmarkCheckBox_5")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_5, 4, 0, 1, 1)

        self.landmarkLineEdit_5 = QLineEdit(Form)
        self.landmarkLineEdit_5.setObjectName(u"landmarkLineEdit_5")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_5, 4, 2, 1, 1)

        self.landmarkAllocationComboBox_6 = QComboBox(Form)
        self.landmarkAllocationComboBox_6.setObjectName(u"landmarkAllocationComboBox_6")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_6, 5, 1, 1, 1)

        self.landmarkCheckbox_3 = QCheckBox(Form)
        self.landmarkCheckbox_3.setObjectName(u"landmarkCheckbox_3")

        self.gridLayout_3.addWidget(self.landmarkCheckbox_3, 2, 0, 1, 1)

        self.landmarkLineEdit_2 = QLineEdit(Form)
        self.landmarkLineEdit_2.setObjectName(u"landmarkLineEdit_2")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_2, 1, 2, 1, 1)

        self.landmarkCheckBox_4 = QCheckBox(Form)
        self.landmarkCheckBox_4.setObjectName(u"landmarkCheckBox_4")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_4, 3, 0, 1, 1)

        self.landmarkLineEdit_1 = QLineEdit(Form)
        self.landmarkLineEdit_1.setObjectName(u"landmarkLineEdit_1")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_1, 0, 2, 1, 1)

        self.landmarkCheckBox_6 = QCheckBox(Form)
        self.landmarkCheckBox_6.setObjectName(u"landmarkCheckBox_6")

        self.gridLayout_3.addWidget(self.landmarkCheckBox_6, 5, 0, 1, 1)

        self.landmarkAllocationComboBox_3 = QComboBox(Form)
        self.landmarkAllocationComboBox_3.setObjectName(u"landmarkAllocationComboBox_3")

        self.gridLayout_3.addWidget(self.landmarkAllocationComboBox_3, 2, 1, 1, 1)

        self.landmarkLineEdit_6 = QLineEdit(Form)
        self.landmarkLineEdit_6.setObjectName(u"landmarkLineEdit_6")

        self.gridLayout_3.addWidget(self.landmarkLineEdit_6, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 6, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        sizePolicy1.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy1)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.addMeasurementButton = QPushButton(Form)
        self.addMeasurementButton.setObjectName(u"addMeasurementButton")

        self.horizontalLayout_5.addWidget(self.addMeasurementButton)

        self.removeMeasurementButton = QPushButton(Form)
        self.removeMeasurementButton.setObjectName(u"removeMeasurementButton")

        self.horizontalLayout_5.addWidget(self.removeMeasurementButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.massSpringParametersRadioButton = QRadioButton(Form)
        self.massSpringParametersRadioButton.setObjectName(u"massSpringParametersRadioButton")
        self.massSpringParametersRadioButton.setChecked(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.massSpringParametersRadioButton)

        self.trajectoriesRadioButton = QRadioButton(Form)
        self.trajectoriesRadioButton.setObjectName(u"trajectoriesRadioButton")
        self.trajectoriesRadioButton.setChecked(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.trajectoriesRadioButton)


        self.verticalLayout_3.addLayout(self.formLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.storeMeasurementsButton = QPushButton(Form)
        self.storeMeasurementsButton.setObjectName(u"storeMeasurementsButton")

        self.gridLayout_2.addWidget(self.storeMeasurementsButton, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.addTargetButton.setText(QCoreApplication.translate("Form", u"add target", None))
        self.removeTargetButton.setText(QCoreApplication.translate("Form", u"remove target", None))
        self.addSegmentButton.setText(QCoreApplication.translate("Form", u"add segment", None))
        self.removeSegmentButton.setText(QCoreApplication.translate("Form", u"remove segment", None))
        self.runMeasurementsButton.setText(QCoreApplication.translate("Form", u"conduct measurements", None))
        self.label.setText(QCoreApplication.translate("Form", u"LANDMARK ALLOCATION", None))
        self.landmarkCheckBox_2.setText("")
        self.landmarkCheckBox_1.setText("")
        self.landmarkCheckBox_5.setText("")
        self.landmarkCheckbox_3.setText("")
        self.landmarkCheckBox_4.setText("")
        self.landmarkCheckBox_6.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"MEASUREMENTS", None))
        self.addMeasurementButton.setText(QCoreApplication.translate("Form", u"add meaurement", None))
        self.removeMeasurementButton.setText(QCoreApplication.translate("Form", u"remove measurement", None))
        self.massSpringParametersRadioButton.setText(QCoreApplication.translate("Form", u"mass-spring parameters", None))
        self.trajectoriesRadioButton.setText(QCoreApplication.translate("Form", u"trajectories", None))
        self.storeMeasurementsButton.setText(QCoreApplication.translate("Form", u"store measurements", None))
    # retranslateUi

