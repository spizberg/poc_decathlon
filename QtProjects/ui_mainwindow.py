# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'idshoes_poc_decathlonykUzkb.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import idshoes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1280, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 700))
        MainWindow.setMaximumSize(QSize(1280, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(20, 130, 194, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(190, 190, 190, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.labelTitle.setPalette(palette)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setLineWidth(1)
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelImageCETI = QLabel(self.centralwidget)
        self.labelImageCETI.setObjectName(u"labelImageCETI")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelImageCETI.sizePolicy().hasHeightForWidth())
        self.labelImageCETI.setSizePolicy(sizePolicy3)
        self.labelImageCETI.setMinimumSize(QSize(327, 200))
        self.labelImageCETI.setMaximumSize(QSize(200, 200))
        font1 = QFont()
        font1.setPointSize(10)
        self.labelImageCETI.setFont(font1)
        self.labelImageCETI.setPixmap(QPixmap(u":/imageModele/logo-ceti.jpeg"))
        self.labelImageCETI.setScaledContents(True)
        self.labelImageCETI.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelImageCETI)

        self.labelImageESTIA = QLabel(self.centralwidget)
        self.labelImageESTIA.setObjectName(u"labelImageESTIA")
        self.labelImageESTIA.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelImageESTIA.sizePolicy().hasHeightForWidth())
        self.labelImageESTIA.setSizePolicy(sizePolicy4)
        self.labelImageESTIA.setMinimumSize(QSize(400, 200))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(20)
        self.labelImageESTIA.setFont(font2)
        self.labelImageESTIA.setPixmap(QPixmap(u":/imageModele/logo-estia.png"))
        self.labelImageESTIA.setScaledContents(False)
        self.labelImageESTIA.setAlignment(Qt.AlignCenter)
        self.labelImageESTIA.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.labelImageESTIA)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.pushButtonDemo = QPushButton(self.centralwidget)
        self.pushButtonDemo.setObjectName(u"pushButtonDemo")
        self.pushButtonDemo.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.pushButtonDemo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>IDSHOES </p><p>- </p><p>CELLULE DE PRISE DE PHOTOS AUTOMATISE</p></body></html>", None))
        self.labelImageCETI.setText("")
        self.labelImageESTIA.setText("")
        self.pushButtonDemo.setText(QCoreApplication.translate("MainWindow", u"D\u00e9marrer", None))
    # retranslateUi

