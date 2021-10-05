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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.bacPredictionLabel = QLabel(self.centralwidget)
        self.bacPredictionLabel.setObjectName(u"bacPredictionLabel")
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setItalic(True)
        self.bacPredictionLabel.setFont(font3)
        self.bacPredictionLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.bacPredictionLabel)


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
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelVideo1.sizePolicy().hasHeightForWidth())
        self.labelVideo1.setSizePolicy(sizePolicy2)
        self.labelVideo1.setMinimumSize(QSize(620, 410))
        self.labelVideo1.setMaximumSize(QSize(620, 410))
        self.labelVideo1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelVideo1)

        self.labelVideo2 = QLabel(self.centralwidget)
        self.labelVideo2.setObjectName(u"labelVideo2")
        sizePolicy2.setHeightForWidth(self.labelVideo2.sizePolicy().hasHeightForWidth())
        self.labelVideo2.setSizePolicy(sizePolicy2)
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
        self.label.setText(QCoreApplication.translate("DemoWindow", u"Cat\u00e9gorie de tri : ", None))
        self.bacPredictionLabel.setText(QCoreApplication.translate("DemoWindow", u"En attente...", None))
        self.pushButtonStart.setText(QCoreApplication.translate("DemoWindow", u"DETECTER", None))
        self.labelVideo1.setText("")
        self.labelVideo2.setText("")
    # retranslateUi

