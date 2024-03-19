# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_landmark_detection.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QProgressBar, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_LM_DETECT(object):
    def setupUi(self, LM_DETECT):
        if not LM_DETECT.objectName():
            LM_DETECT.setObjectName(u"LM_DETECT")
        LM_DETECT.resize(1474, 768)
        self.gridLayout_2 = QGridLayout(LM_DETECT)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progressBar = QProgressBar(LM_DETECT)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.selectionTreeWidget = QTreeWidget(LM_DETECT)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.selectionTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.selectionTreeWidget.setObjectName(u"selectionTreeWidget")
        self.selectionTreeWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.selectionTreeWidget.setFrameShape(QFrame.StyledPanel)
        self.selectionTreeWidget.setAutoExpandDelay(0)

        self.verticalLayout.addWidget(self.selectionTreeWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addTargetButton = QPushButton(LM_DETECT)
        self.addTargetButton.setObjectName(u"addTargetButton")

        self.horizontalLayout.addWidget(self.addTargetButton)

        self.removeTargetButton = QPushButton(LM_DETECT)
        self.removeTargetButton.setObjectName(u"removeTargetButton")

        self.horizontalLayout.addWidget(self.removeTargetButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addSegmentButton = QPushButton(LM_DETECT)
        self.addSegmentButton.setObjectName(u"addSegmentButton")

        self.horizontalLayout_2.addWidget(self.addSegmentButton)

        self.removeSegmentButton = QPushButton(LM_DETECT)
        self.removeSegmentButton.setObjectName(u"removeSegmentButton")

        self.horizontalLayout_2.addWidget(self.removeSegmentButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.runLandmarkDetectionButton = QPushButton(LM_DETECT)
        self.runLandmarkDetectionButton.setObjectName(u"runLandmarkDetectionButton")

        self.verticalLayout.addWidget(self.runLandmarkDetectionButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.storeLandmarksButton = QPushButton(LM_DETECT)
        self.storeLandmarksButton.setObjectName(u"storeLandmarksButton")
        self.storeLandmarksButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.storeLandmarksButton, 2, 0, 1, 1)


        self.retranslateUi(LM_DETECT)

        QMetaObject.connectSlotsByName(LM_DETECT)
    # setupUi

    def retranslateUi(self, LM_DETECT):
        LM_DETECT.setWindowTitle(QCoreApplication.translate("LM_DETECT", u"Form", None))
        self.addTargetButton.setText(QCoreApplication.translate("LM_DETECT", u"add target", None))
        self.removeTargetButton.setText(QCoreApplication.translate("LM_DETECT", u"remove target", None))
        self.addSegmentButton.setText(QCoreApplication.translate("LM_DETECT", u"add segment", None))
        self.removeSegmentButton.setText(QCoreApplication.translate("LM_DETECT", u"remove segment", None))
        self.runLandmarkDetectionButton.setText(QCoreApplication.translate("LM_DETECT", u"detect landmarks", None))
        self.storeLandmarksButton.setText(QCoreApplication.translate("LM_DETECT", u"store landmarks", None))
    # retranslateUi

