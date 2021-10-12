# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'idshoes_poc_decathlon_demo_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import idshoes_rc

class Ui_DemoWindow(object):
    def setupUi(self, DemoWindow):
        if not DemoWindow.objectName():
            DemoWindow.setObjectName(u"DemoWindow")
        DemoWindow.setWindowModality(Qt.NonModal)
        DemoWindow.setEnabled(True)
        DemoWindow.resize(1280, 700)
        DemoWindow.setMinimumSize(QSize(1280, 600))
        DemoWindow.setMaximumSize(QSize(1280, 700))
        self.centralwidget = QWidget(DemoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/imageModele/Decathlon_Logo.svg"))

        self.horizontalLayout.addWidget(self.label_3)

        self.labelDecathlon = QLabel(self.centralwidget)
        self.labelDecathlon.setObjectName(u"labelDecathlon")
        self.labelDecathlon.setTextFormat(Qt.AutoText)
        self.labelDecathlon.setPixmap(QPixmap(u":/imageModele/ESTIA.png"))
        self.labelDecathlon.setScaledContents(False)

        self.horizontalLayout.addWidget(self.labelDecathlon)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelDemoTitle = QLabel(self.centralwidget)
        self.labelDemoTitle.setObjectName(u"labelDemoTitle")
        palette = QPalette()
        brush = QBrush(QColor(20, 130, 194, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(190, 190, 190, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.labelDemoTitle.setPalette(palette)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.labelDemoTitle.setFont(font)
        self.labelDemoTitle.setCursor(QCursor(Qt.ArrowCursor))
        self.labelDemoTitle.setProperty("Color", QColor(173, 127, 168))

        self.horizontalLayout.addWidget(self.labelDemoTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonBack = QPushButton(self.centralwidget)
        self.pushButtonBack.setObjectName(u"pushButtonBack")
        font1 = QFont()
        self.pushButtonBack.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButtonBack)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(75, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.ipstLabel = QLabel(self.centralwidget)
        self.ipstLabel.setObjectName(u"ipstLabel")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipstLabel.sizePolicy().hasHeightForWidth())
        self.ipstLabel.setSizePolicy(sizePolicy)
        self.ipstLabel.setMinimumSize(QSize(150, 0))
        self.ipstLabel.setMaximumSize(QSize(16777215, 16777215))
        self.ipstLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.ipstLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.itspLabel = QLabel(self.centralwidget)
        self.itspLabel.setObjectName(u"itspLabel")
        sizePolicy.setHeightForWidth(self.itspLabel.sizePolicy().hasHeightForWidth())
        self.itspLabel.setSizePolicy(sizePolicy)
        self.itspLabel.setMinimumSize(QSize(150, 0))
        self.itspLabel.setMaximumSize(QSize(16777215, 16777215))
        self.itspLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.itspLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.fipLabel = QLabel(self.centralwidget)
        self.fipLabel.setObjectName(u"fipLabel")
        sizePolicy.setHeightForWidth(self.fipLabel.sizePolicy().hasHeightForWidth())
        self.fipLabel.setSizePolicy(sizePolicy)
        self.fipLabel.setMinimumSize(QSize(150, 0))
        self.fipLabel.setMaximumSize(QSize(16777215, 16777215))
        self.fipLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.fipLabel)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.btLabel = QLabel(self.centralwidget)
        self.btLabel.setObjectName(u"btLabel")
        sizePolicy.setHeightForWidth(self.btLabel.sizePolicy().hasHeightForWidth())
        self.btLabel.setSizePolicy(sizePolicy)
        self.btLabel.setMinimumSize(QSize(150, 0))
        self.btLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.btLabel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.autreLabel = QLabel(self.centralwidget)
        self.autreLabel.setObjectName(u"autreLabel")
        sizePolicy.setHeightForWidth(self.autreLabel.sizePolicy().hasHeightForWidth())
        self.autreLabel.setSizePolicy(sizePolicy)
        self.autreLabel.setMinimumSize(QSize(150, 0))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.autreLabel.setFont(font2)
        self.autreLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.autreLabel)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.noneLabel = QLabel(self.centralwidget)
        self.noneLabel.setObjectName(u"noneLabel")
        sizePolicy.setHeightForWidth(self.noneLabel.sizePolicy().hasHeightForWidth())
        self.noneLabel.setSizePolicy(sizePolicy)
        self.noneLabel.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setBold(False)
        self.noneLabel.setFont(font3)
        self.noneLabel.setFrameShadow(QFrame.Plain)
        self.noneLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.noneLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(0, 5, -1, 5)
        self.pushButtonStart = QPushButton(self.centralwidget)
        self.pushButtonStart.setObjectName(u"pushButtonStart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonStart.sizePolicy().hasHeightForWidth())
        self.pushButtonStart.setSizePolicy(sizePolicy1)
        self.pushButtonStart.setMaximumSize(QSize(16777215, 16777198))
        self.pushButtonStart.setIconSize(QSize(16, 20))

        self.horizontalLayout_3.addWidget(self.pushButtonStart)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.labelVideo1 = QLabel(self.centralwidget)
        self.labelVideo1.setObjectName(u"labelVideo1")
        sizePolicy.setHeightForWidth(self.labelVideo1.sizePolicy().hasHeightForWidth())
        self.labelVideo1.setSizePolicy(sizePolicy)
        self.labelVideo1.setMinimumSize(QSize(620, 410))
        self.labelVideo1.setMaximumSize(QSize(620, 410))
        self.labelVideo1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelVideo1)

        self.labelVideo2 = QLabel(self.centralwidget)
        self.labelVideo2.setObjectName(u"labelVideo2")
        sizePolicy.setHeightForWidth(self.labelVideo2.sizePolicy().hasHeightForWidth())
        self.labelVideo2.setSizePolicy(sizePolicy)
        self.labelVideo2.setMinimumSize(QSize(620, 410))
        self.labelVideo2.setMaximumSize(QSize(620, 410))
        self.labelVideo2.setScaledContents(False)
        self.labelVideo2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelVideo2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        DemoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DemoWindow)

        QMetaObject.connectSlotsByName(DemoWindow)
    # setupUi

    def retranslateUi(self, DemoWindow):
        DemoWindow.setWindowTitle(QCoreApplication.translate("DemoWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.labelDecathlon.setText("")
        self.labelDemoTitle.setText(QCoreApplication.translate("DemoWindow", u"IDSHOES - CELLULE D'IDENTIFICATION DE MODELE DE CHAUSSURE", None))
        self.pushButtonBack.setText(QCoreApplication.translate("DemoWindow", u"Retour", None))
        self.ipstLabel.setText(QCoreApplication.translate("DemoWindow", u"INJECTE PVC SUR TIGE", None))
        self.itspLabel.setText(QCoreApplication.translate("DemoWindow", u"INJECTE TPR SUR TIGE", None))
        self.fipLabel.setText(QCoreApplication.translate("DemoWindow", u"FULL INJECTE PVC", None))
        self.btLabel.setText(QCoreApplication.translate("DemoWindow", u"BOTTE TPE", None))
        self.autreLabel.setText(QCoreApplication.translate("DemoWindow", u"NON DEFINI", None))
        self.noneLabel.setText(QCoreApplication.translate("DemoWindow", u"VEUILLEZ REESSAYER", None))
        self.pushButtonStart.setText(QCoreApplication.translate("DemoWindow", u"DETECTER", None))
        self.labelVideo1.setText("")
        self.labelVideo2.setText("")
    # retranslateUi

