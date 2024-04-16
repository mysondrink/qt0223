# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'curve.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 450)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 450))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnReturn = QPushButton(self.frame)
        self.btnReturn.setObjectName(u"btnReturn")
        self.btnReturn.setGeometry(QRect(540, 360, 255, 80))
        self.btnReturn.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnDump = QPushButton(self.frame)
        self.btnDump.setObjectName(u"btnDump")
        self.btnDump.setGeometry(QRect(10, 360, 255, 80))
        self.btnDump.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 171, 70))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.modeBox_1 = QComboBox(self.frame)
        self.modeBox_1.setObjectName(u"modeBox_1")
        self.modeBox_1.setGeometry(QRect(490, 25, 129, 31))
        self.modeBox_1.setStyleSheet(u"QComboBox::drop-down{\n"
"width:56px;  height:56px;\n"
"}\n"
"\n"
"QComboBox{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(0, 0, 0);/*\u80cc\u666f\u989c\u8272*/\n"
"    padding: 1px 2px 1px 2px;  /*\u9488\u5bf9\u4e8e\u7ec4\u5408\u6846\u4e2d\u7684\u6587\u672c\u5185\u5bb9*/\n"
"	color: rgb(255,255,255)\n"
"}")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(401, 28, 81, 31))
        self.label_4.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(275, 360, 255, 80))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 60, 771, 291))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 781, 291))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.layoutWidget)
        self.label_31.setObjectName(u"label_31")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(100, 0))
        self.label_31.setMaximumSize(QSize(100, 16777215))
        self.label_31.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(100, 0))
        self.label_17.setMaximumSize(QSize(100, 16777215))
        self.label_17.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_17, 0, 1, 1, 1)

        self.paraLine_11 = QLineEdit(self.layoutWidget)
        self.paraLine_11.setObjectName(u"paraLine_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.paraLine_11.sizePolicy().hasHeightForWidth())
        self.paraLine_11.setSizePolicy(sizePolicy1)
        self.paraLine_11.setMinimumSize(QSize(150, 0))
        self.paraLine_11.setMaximumSize(QSize(150, 16777215))
        self.paraLine_11.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_11.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_11, 0, 2, 1, 1)

        self.label_32 = QLabel(self.layoutWidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 0))
        self.label_32.setMaximumSize(QSize(100, 16777215))
        self.label_32.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_32, 0, 3, 1, 1)

        self.paraLine_12 = QLineEdit(self.layoutWidget)
        self.paraLine_12.setObjectName(u"paraLine_12")
        sizePolicy1.setHeightForWidth(self.paraLine_12.sizePolicy().hasHeightForWidth())
        self.paraLine_12.setSizePolicy(sizePolicy1)
        self.paraLine_12.setMinimumSize(QSize(150, 0))
        self.paraLine_12.setMaximumSize(QSize(150, 16777215))
        self.paraLine_12.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_12.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_12, 0, 4, 1, 1)

        self.label_33 = QLabel(self.layoutWidget)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QSize(100, 0))
        self.label_33.setMaximumSize(QSize(100, 16777215))
        self.label_33.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_33, 1, 0, 1, 1)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(100, 0))
        self.label_18.setMaximumSize(QSize(100, 16777215))
        self.label_18.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_18, 1, 1, 1, 1)

        self.paraLine_13 = QLineEdit(self.layoutWidget)
        self.paraLine_13.setObjectName(u"paraLine_13")
        sizePolicy1.setHeightForWidth(self.paraLine_13.sizePolicy().hasHeightForWidth())
        self.paraLine_13.setSizePolicy(sizePolicy1)
        self.paraLine_13.setMinimumSize(QSize(150, 0))
        self.paraLine_13.setMaximumSize(QSize(150, 16777215))
        self.paraLine_13.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_13.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_13, 1, 2, 1, 1)

        self.label_34 = QLabel(self.layoutWidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(100, 0))
        self.label_34.setMaximumSize(QSize(100, 16777215))
        self.label_34.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_34, 1, 3, 1, 1)

        self.paraLine_14 = QLineEdit(self.layoutWidget)
        self.paraLine_14.setObjectName(u"paraLine_14")
        sizePolicy1.setHeightForWidth(self.paraLine_14.sizePolicy().hasHeightForWidth())
        self.paraLine_14.setSizePolicy(sizePolicy1)
        self.paraLine_14.setMinimumSize(QSize(150, 0))
        self.paraLine_14.setMaximumSize(QSize(150, 16777215))
        self.paraLine_14.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_14.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_14, 1, 4, 1, 1)

        self.label_35 = QLabel(self.layoutWidget)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QSize(100, 0))
        self.label_35.setMaximumSize(QSize(100, 16777215))
        self.label_35.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_35, 2, 0, 1, 1)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(100, 0))
        self.label_19.setMaximumSize(QSize(100, 16777215))
        self.label_19.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_19, 2, 1, 1, 1)

        self.paraLine_15 = QLineEdit(self.layoutWidget)
        self.paraLine_15.setObjectName(u"paraLine_15")
        sizePolicy1.setHeightForWidth(self.paraLine_15.sizePolicy().hasHeightForWidth())
        self.paraLine_15.setSizePolicy(sizePolicy1)
        self.paraLine_15.setMinimumSize(QSize(150, 0))
        self.paraLine_15.setMaximumSize(QSize(150, 16777215))
        self.paraLine_15.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_15.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_15, 2, 2, 1, 1)

        self.label_36 = QLabel(self.layoutWidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(100, 0))
        self.label_36.setMaximumSize(QSize(100, 16777215))
        self.label_36.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_36, 2, 3, 1, 1)

        self.paraLine_16 = QLineEdit(self.layoutWidget)
        self.paraLine_16.setObjectName(u"paraLine_16")
        sizePolicy1.setHeightForWidth(self.paraLine_16.sizePolicy().hasHeightForWidth())
        self.paraLine_16.setSizePolicy(sizePolicy1)
        self.paraLine_16.setMinimumSize(QSize(150, 0))
        self.paraLine_16.setMaximumSize(QSize(150, 16777215))
        self.paraLine_16.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_16.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_16, 2, 4, 1, 1)

        self.label_37 = QLabel(self.layoutWidget)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QSize(100, 0))
        self.label_37.setMaximumSize(QSize(100, 16777215))
        self.label_37.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_37, 3, 0, 1, 1)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(100, 0))
        self.label_20.setMaximumSize(QSize(100, 16777215))
        self.label_20.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_20, 3, 1, 1, 1)

        self.paraLine_17 = QLineEdit(self.layoutWidget)
        self.paraLine_17.setObjectName(u"paraLine_17")
        sizePolicy1.setHeightForWidth(self.paraLine_17.sizePolicy().hasHeightForWidth())
        self.paraLine_17.setSizePolicy(sizePolicy1)
        self.paraLine_17.setMinimumSize(QSize(150, 0))
        self.paraLine_17.setMaximumSize(QSize(150, 16777215))
        self.paraLine_17.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_17.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_17, 3, 2, 1, 1)

        self.label_38 = QLabel(self.layoutWidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(100, 0))
        self.label_38.setMaximumSize(QSize(100, 16777215))
        self.label_38.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_38, 3, 3, 1, 1)

        self.paraLine_18 = QLineEdit(self.layoutWidget)
        self.paraLine_18.setObjectName(u"paraLine_18")
        sizePolicy1.setHeightForWidth(self.paraLine_18.sizePolicy().hasHeightForWidth())
        self.paraLine_18.setSizePolicy(sizePolicy1)
        self.paraLine_18.setMinimumSize(QSize(150, 0))
        self.paraLine_18.setMaximumSize(QSize(150, 16777215))
        self.paraLine_18.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_18.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_18, 3, 4, 1, 1)

        self.label_39 = QLabel(self.layoutWidget)
        self.label_39.setObjectName(u"label_39")
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setMinimumSize(QSize(100, 0))
        self.label_39.setMaximumSize(QSize(100, 16777215))
        self.label_39.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_39, 4, 0, 1, 1)

        self.label_40 = QLabel(self.layoutWidget)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(100, 0))
        self.label_40.setMaximumSize(QSize(100, 16777215))
        self.label_40.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_40, 4, 1, 1, 1)

        self.paraLine_19 = QLineEdit(self.layoutWidget)
        self.paraLine_19.setObjectName(u"paraLine_19")
        sizePolicy1.setHeightForWidth(self.paraLine_19.sizePolicy().hasHeightForWidth())
        self.paraLine_19.setSizePolicy(sizePolicy1)
        self.paraLine_19.setMinimumSize(QSize(150, 0))
        self.paraLine_19.setMaximumSize(QSize(150, 16777215))
        self.paraLine_19.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_19.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_19, 4, 2, 1, 1)

        self.label_41 = QLabel(self.layoutWidget)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(100, 0))
        self.label_41.setMaximumSize(QSize(100, 16777215))
        self.label_41.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_2.addWidget(self.label_41, 4, 3, 1, 1)

        self.paraLine_20 = QLineEdit(self.layoutWidget)
        self.paraLine_20.setObjectName(u"paraLine_20")
        sizePolicy1.setHeightForWidth(self.paraLine_20.sizePolicy().hasHeightForWidth())
        self.paraLine_20.setSizePolicy(sizePolicy1)
        self.paraLine_20.setMinimumSize(QSize(150, 0))
        self.paraLine_20.setMaximumSize(QSize(150, 16777215))
        self.paraLine_20.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_20.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_2.addWidget(self.paraLine_20, 4, 4, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.layoutWidget_2 = QWidget(self.page_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 781, 291))
        self.gridLayout_3 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.layoutWidget_2)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QSize(100, 0))
        self.label_42.setMaximumSize(QSize(100, 16777215))
        self.label_42.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_42, 0, 0, 1, 1)

        self.label_21 = QLabel(self.layoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(100, 0))
        self.label_21.setMaximumSize(QSize(100, 16777215))
        self.label_21.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_21, 0, 1, 1, 1)

        self.paraLine_21 = QLineEdit(self.layoutWidget_2)
        self.paraLine_21.setObjectName(u"paraLine_21")
        sizePolicy1.setHeightForWidth(self.paraLine_21.sizePolicy().hasHeightForWidth())
        self.paraLine_21.setSizePolicy(sizePolicy1)
        self.paraLine_21.setMinimumSize(QSize(150, 0))
        self.paraLine_21.setMaximumSize(QSize(150, 16777215))
        self.paraLine_21.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_21.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_21, 0, 2, 1, 1)

        self.label_43 = QLabel(self.layoutWidget_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(100, 0))
        self.label_43.setMaximumSize(QSize(100, 16777215))
        self.label_43.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_43, 0, 3, 1, 1)

        self.paraLine_22 = QLineEdit(self.layoutWidget_2)
        self.paraLine_22.setObjectName(u"paraLine_22")
        sizePolicy1.setHeightForWidth(self.paraLine_22.sizePolicy().hasHeightForWidth())
        self.paraLine_22.setSizePolicy(sizePolicy1)
        self.paraLine_22.setMinimumSize(QSize(150, 0))
        self.paraLine_22.setMaximumSize(QSize(150, 16777215))
        self.paraLine_22.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_22.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_22, 0, 4, 1, 1)

        self.label_44 = QLabel(self.layoutWidget_2)
        self.label_44.setObjectName(u"label_44")
        sizePolicy.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy)
        self.label_44.setMinimumSize(QSize(100, 0))
        self.label_44.setMaximumSize(QSize(100, 16777215))
        self.label_44.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_44, 1, 0, 1, 1)

        self.label_22 = QLabel(self.layoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 0))
        self.label_22.setMaximumSize(QSize(100, 16777215))
        self.label_22.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_22, 1, 1, 1, 1)

        self.paraLine_23 = QLineEdit(self.layoutWidget_2)
        self.paraLine_23.setObjectName(u"paraLine_23")
        sizePolicy1.setHeightForWidth(self.paraLine_23.sizePolicy().hasHeightForWidth())
        self.paraLine_23.setSizePolicy(sizePolicy1)
        self.paraLine_23.setMinimumSize(QSize(150, 0))
        self.paraLine_23.setMaximumSize(QSize(150, 16777215))
        self.paraLine_23.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_23.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_23, 1, 2, 1, 1)

        self.label_45 = QLabel(self.layoutWidget_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(100, 0))
        self.label_45.setMaximumSize(QSize(100, 16777215))
        self.label_45.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_45, 1, 3, 1, 1)

        self.paraLine_24 = QLineEdit(self.layoutWidget_2)
        self.paraLine_24.setObjectName(u"paraLine_24")
        sizePolicy1.setHeightForWidth(self.paraLine_24.sizePolicy().hasHeightForWidth())
        self.paraLine_24.setSizePolicy(sizePolicy1)
        self.paraLine_24.setMinimumSize(QSize(150, 0))
        self.paraLine_24.setMaximumSize(QSize(150, 16777215))
        self.paraLine_24.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_24.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_24, 1, 4, 1, 1)

        self.label_46 = QLabel(self.layoutWidget_2)
        self.label_46.setObjectName(u"label_46")
        sizePolicy.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy)
        self.label_46.setMinimumSize(QSize(100, 0))
        self.label_46.setMaximumSize(QSize(100, 16777215))
        self.label_46.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_46, 2, 0, 1, 1)

        self.label_23 = QLabel(self.layoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 0))
        self.label_23.setMaximumSize(QSize(100, 16777215))
        self.label_23.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_23, 2, 1, 1, 1)

        self.paraLine_25 = QLineEdit(self.layoutWidget_2)
        self.paraLine_25.setObjectName(u"paraLine_25")
        sizePolicy1.setHeightForWidth(self.paraLine_25.sizePolicy().hasHeightForWidth())
        self.paraLine_25.setSizePolicy(sizePolicy1)
        self.paraLine_25.setMinimumSize(QSize(150, 0))
        self.paraLine_25.setMaximumSize(QSize(150, 16777215))
        self.paraLine_25.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_25.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_25, 2, 2, 1, 1)

        self.label_47 = QLabel(self.layoutWidget_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(100, 0))
        self.label_47.setMaximumSize(QSize(100, 16777215))
        self.label_47.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_47, 2, 3, 1, 1)

        self.paraLine_26 = QLineEdit(self.layoutWidget_2)
        self.paraLine_26.setObjectName(u"paraLine_26")
        sizePolicy1.setHeightForWidth(self.paraLine_26.sizePolicy().hasHeightForWidth())
        self.paraLine_26.setSizePolicy(sizePolicy1)
        self.paraLine_26.setMinimumSize(QSize(150, 0))
        self.paraLine_26.setMaximumSize(QSize(150, 16777215))
        self.paraLine_26.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_26.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_26, 2, 4, 1, 1)

        self.label_48 = QLabel(self.layoutWidget_2)
        self.label_48.setObjectName(u"label_48")
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setMinimumSize(QSize(100, 0))
        self.label_48.setMaximumSize(QSize(100, 16777215))
        self.label_48.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_48, 3, 0, 1, 1)

        self.label_24 = QLabel(self.layoutWidget_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(100, 0))
        self.label_24.setMaximumSize(QSize(100, 16777215))
        self.label_24.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_24, 3, 1, 1, 1)

        self.paraLine_27 = QLineEdit(self.layoutWidget_2)
        self.paraLine_27.setObjectName(u"paraLine_27")
        sizePolicy1.setHeightForWidth(self.paraLine_27.sizePolicy().hasHeightForWidth())
        self.paraLine_27.setSizePolicy(sizePolicy1)
        self.paraLine_27.setMinimumSize(QSize(150, 0))
        self.paraLine_27.setMaximumSize(QSize(150, 16777215))
        self.paraLine_27.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_27.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_27, 3, 2, 1, 1)

        self.label_49 = QLabel(self.layoutWidget_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(100, 0))
        self.label_49.setMaximumSize(QSize(100, 16777215))
        self.label_49.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_49, 3, 3, 1, 1)

        self.paraLine_28 = QLineEdit(self.layoutWidget_2)
        self.paraLine_28.setObjectName(u"paraLine_28")
        sizePolicy1.setHeightForWidth(self.paraLine_28.sizePolicy().hasHeightForWidth())
        self.paraLine_28.setSizePolicy(sizePolicy1)
        self.paraLine_28.setMinimumSize(QSize(150, 0))
        self.paraLine_28.setMaximumSize(QSize(150, 16777215))
        self.paraLine_28.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_28.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_28, 3, 4, 1, 1)

        self.label_50 = QLabel(self.layoutWidget_2)
        self.label_50.setObjectName(u"label_50")
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QSize(100, 0))
        self.label_50.setMaximumSize(QSize(100, 16777215))
        self.label_50.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_50, 4, 0, 1, 1)

        self.label_51 = QLabel(self.layoutWidget_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(100, 0))
        self.label_51.setMaximumSize(QSize(100, 16777215))
        self.label_51.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_51, 4, 1, 1, 1)

        self.paraLine_29 = QLineEdit(self.layoutWidget_2)
        self.paraLine_29.setObjectName(u"paraLine_29")
        sizePolicy1.setHeightForWidth(self.paraLine_29.sizePolicy().hasHeightForWidth())
        self.paraLine_29.setSizePolicy(sizePolicy1)
        self.paraLine_29.setMinimumSize(QSize(150, 0))
        self.paraLine_29.setMaximumSize(QSize(150, 16777215))
        self.paraLine_29.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_29.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_29, 4, 2, 1, 1)

        self.label_52 = QLabel(self.layoutWidget_2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(100, 0))
        self.label_52.setMaximumSize(QSize(100, 16777215))
        self.label_52.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_3.addWidget(self.label_52, 4, 3, 1, 1)

        self.paraLine_30 = QLineEdit(self.layoutWidget_2)
        self.paraLine_30.setObjectName(u"paraLine_30")
        sizePolicy1.setHeightForWidth(self.paraLine_30.sizePolicy().hasHeightForWidth())
        self.paraLine_30.setSizePolicy(sizePolicy1)
        self.paraLine_30.setMinimumSize(QSize(150, 0))
        self.paraLine_30.setMaximumSize(QSize(150, 16777215))
        self.paraLine_30.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_30.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_3.addWidget(self.paraLine_30, 4, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.layoutWidget_3 = QWidget(self.page_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 0, 782, 291))
        self.gridLayout_4 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.paraLine_34 = QLineEdit(self.layoutWidget_3)
        self.paraLine_34.setObjectName(u"paraLine_34")
        sizePolicy1.setHeightForWidth(self.paraLine_34.sizePolicy().hasHeightForWidth())
        self.paraLine_34.setSizePolicy(sizePolicy1)
        self.paraLine_34.setMinimumSize(QSize(150, 0))
        self.paraLine_34.setMaximumSize(QSize(150, 16777215))
        self.paraLine_34.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_34.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_4.addWidget(self.paraLine_34, 1, 1, 1, 1)

        self.paraLine_31 = QLineEdit(self.layoutWidget_3)
        self.paraLine_31.setObjectName(u"paraLine_31")
        sizePolicy1.setHeightForWidth(self.paraLine_31.sizePolicy().hasHeightForWidth())
        self.paraLine_31.setSizePolicy(sizePolicy1)
        self.paraLine_31.setMinimumSize(QSize(150, 0))
        self.paraLine_31.setMaximumSize(QSize(150, 16777215))
        self.paraLine_31.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_31.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_4.addWidget(self.paraLine_31, 0, 1, 1, 1)

        self.paraLine_32 = QLineEdit(self.layoutWidget_3)
        self.paraLine_32.setObjectName(u"paraLine_32")
        sizePolicy1.setHeightForWidth(self.paraLine_32.sizePolicy().hasHeightForWidth())
        self.paraLine_32.setSizePolicy(sizePolicy1)
        self.paraLine_32.setMinimumSize(QSize(150, 0))
        self.paraLine_32.setMaximumSize(QSize(150, 16777215))
        self.paraLine_32.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_32.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_4.addWidget(self.paraLine_32, 0, 3, 1, 1)

        self.label_54 = QLabel(self.layoutWidget_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(100, 0))
        self.label_54.setMaximumSize(QSize(100, 16777215))
        self.label_54.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_4.addWidget(self.label_54, 0, 2, 1, 1)

        self.paraLine_35 = QLineEdit(self.layoutWidget_3)
        self.paraLine_35.setObjectName(u"paraLine_35")
        sizePolicy1.setHeightForWidth(self.paraLine_35.sizePolicy().hasHeightForWidth())
        self.paraLine_35.setSizePolicy(sizePolicy1)
        self.paraLine_35.setMinimumSize(QSize(150, 0))
        self.paraLine_35.setMaximumSize(QSize(150, 16777215))
        self.paraLine_35.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_35.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_4.addWidget(self.paraLine_35, 1, 3, 1, 1)

        self.label_25 = QLabel(self.layoutWidget_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(100, 0))
        self.label_25.setMaximumSize(QSize(100, 16777215))
        self.label_25.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_4.addWidget(self.label_25, 0, 0, 1, 1)

        self.paraLine_33 = QLineEdit(self.layoutWidget_3)
        self.paraLine_33.setObjectName(u"paraLine_33")
        sizePolicy1.setHeightForWidth(self.paraLine_33.sizePolicy().hasHeightForWidth())
        self.paraLine_33.setSizePolicy(sizePolicy1)
        self.paraLine_33.setMinimumSize(QSize(150, 0))
        self.paraLine_33.setMaximumSize(QSize(150, 16777215))
        self.paraLine_33.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_33.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_4.addWidget(self.paraLine_33, 0, 5, 1, 1)

        self.label_29 = QLabel(self.layoutWidget_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(100, 0))
        self.label_29.setMaximumSize(QSize(100, 16777215))
        self.label_29.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_4.addWidget(self.label_29, 0, 4, 1, 1)

        self.label_56 = QLabel(self.layoutWidget_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(100, 0))
        self.label_56.setMaximumSize(QSize(100, 16777215))
        self.label_56.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_4.addWidget(self.label_56, 1, 2, 1, 1)

        self.label_26 = QLabel(self.layoutWidget_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(100, 0))
        self.label_26.setMaximumSize(QSize(100, 16777215))
        self.label_26.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_4.addWidget(self.label_26, 1, 0, 1, 1)

        self.paraLine_36 = QLineEdit(self.layoutWidget_3)
        self.paraLine_36.setObjectName(u"paraLine_36")
        sizePolicy1.setHeightForWidth(self.paraLine_36.sizePolicy().hasHeightForWidth())
        self.paraLine_36.setSizePolicy(sizePolicy1)
        self.paraLine_36.setMinimumSize(QSize(150, 0))
        self.paraLine_36.setMaximumSize(QSize(150, 16777215))
        self.paraLine_36.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine_36.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_4.addWidget(self.paraLine_36, 1, 5, 1, 1)

        self.label_57 = QLabel(self.layoutWidget_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(100, 0))
        self.label_57.setMaximumSize(QSize(100, 16777215))
        self.label_57.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.gridLayout_4.addWidget(self.label_57, 1, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.btnDump.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e3b\u66f2\u7ebf\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u4e3b\u66f2\u7ebf</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u9875", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"S0", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"S1", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"S2", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"S3", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"S4", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"S5", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"S6", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"S7", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"S8", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"S9", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u53d1\u5149\u503c</p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u6d53\u5ea6</p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">RLU1</p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">CALPos1</p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Conc1</p></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">RLU2</p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">CALPos2</p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Conc2</p></body></html>", None))
    # retranslateUi

