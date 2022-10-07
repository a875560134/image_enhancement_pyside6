# -*- coding: utf-8 -*-
# 导入需求包
import math
import os
import sys
from threading import Thread
import apprcc_rc
import cv2
import numpy as np
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


# 窗口定义
class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.verticalLayout_2 = None
        self.verticalLayout = None
        self.pushButton_13 = None
        self.gridLayout = None
        self.pushButton_8 = None
        self.pushButton = None
        self.pushButton_6 = None
        self.pushButton_9 = None
        self.pushButton_4 = None
        self.pushButton_2 = None
        self.pushButton_3 = None
        self.pushButton_7 = None
        self.pushButton_5 = None
        self.pushButton_11 = None
        self.pushButton_10 = None
        self.pushButton_12 = None
        self.menubar = None
        self.statusbar = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"图像增强工具")
        MainWindow.resize(859, 546)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
                                         "background:url(:/img/1.jpg);\n"
                                         "}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"#pushButton_13:hover{\n"
                                         "background-color:rgba(0, 136, 204, 90);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_13:pressed{\n"
                                         "background-color:rgba(0, 136, 204, 40);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_13{\n"
                                         "background-color:rgba(0, 170, 255, 140);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "font: 11pt \"\u9ed1\u4f53\";\n"
                                         "font-style:normal;\n"
                                         "font-weight:normal;\n"
                                         "\n"
                                         "text-align:center;\n"
                                         "direction:rtl;\n"
                                         "vertical-align:middle;\n"
                                         "text-transform:uppercase;\n"
                                         "line-heighr:1.0;\n"
                                         "white-space:nowrap;\n"
                                         "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                         "border-style:solid;\n"
                                         "border-width:1px;\n"
                                         "border-color:rgba(255, 170, 0,255);\n"
                                         "border-radius:6px;\n"
                                         "outline-style:solid;\n"
                                         "outline-offset:1px;\n"
                                         "outline-width:1px;\n"
                                         "outline-color:rgb(255, 170, 127);\n"
                                         "outline-offset:2px;\n"
                                         "}")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QSize(1677, 1677))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet(u"#pushButton_8:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_8:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_8{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(1677, 1677))
        self.pushButton.setFocusPolicy(Qt.StrongFocus)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"#pushButton:hover{\n"
                                      "background-color:rgba(0, 136, 204, 90);\n"
                                      "color:rgb(255, 170, 255);\n"
                                      "}\n"
                                      "#pushButton:pressed{\n"
                                      "background-color:rgba(0, 136, 204, 40);\n"
                                      "color:rgb(255, 170, 255);\n"
                                      "}\n"
                                      "#pushButton{\n"
                                      "background-color:rgba(0, 170, 255, 140);\n"
                                      "color:rgb(255, 170, 255);\n"
                                      "font: 11pt \"\u9ed1\u4f53\";\n"
                                      "font-style:normal;\n"
                                      "font-weight:normal;\n"
                                      "\n"
                                      "text-align:center;\n"
                                      "direction:rtl;\n"
                                      "vertical-align:middle;\n"
                                      "text-transform:uppercase;\n"
                                      "line-heighr:1.0;\n"
                                      "white-space:nowrap;\n"
                                      "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                      "border-style:solid;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgba(255, 170, 0,255);\n"
                                      "border-radius:6px;\n"
                                      "outline-style:solid;\n"
                                      "outline-offset:1px;\n"
                                      "outline-width:1px;\n"
                                      "outline-color:rgb(255, 170, 127);\n"
                                      "outline-offset:2px;\n"
                                      "}")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(False)
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QSize(1677, 1677))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(u"#pushButton_6:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_6:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_6{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMaximumSize(QSize(1677, 1676))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet(u"#pushButton_9:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_9:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_9{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMaximumSize(QSize(1677, 1677))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet(u"#pushButton_4:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_4:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "#pushButton_4{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(1677, 1677))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"#pushButton_2:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_2:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_2{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(1677, 1677))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(u"\n"
                                        "#pushButton_3:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_3:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_3{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QSize(1677, 1677))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet(u"#pushButton_7:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_7:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_7{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(1677, 1677))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet(u"#pushButton_5:hover{\n"
                                        "background-color:rgba(0, 136, 204, 90);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "#pushButton_5:pressed{\n"
                                        "background-color:rgba(0, 136, 204, 40);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton_5{\n"
                                        "background-color:rgba(0, 170, 255, 140);\n"
                                        "color:rgb(255, 170, 255);\n"
                                        "font: 11pt \"\u9ed1\u4f53\";\n"
                                        "font-style:normal;\n"
                                        "font-weight:normal;\n"
                                        "\n"
                                        "text-align:center;\n"
                                        "direction:rtl;\n"
                                        "vertical-align:middle;\n"
                                        "text-transform:uppercase;\n"
                                        "line-heighr:1.0;\n"
                                        "white-space:nowrap;\n"
                                        "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                        "border-style:solid;\n"
                                        "border-width:1px;\n"
                                        "border-color:rgba(255, 170, 0,255);\n"
                                        "border-radius:6px;\n"
                                        "outline-style:solid;\n"
                                        "outline-offset:1px;\n"
                                        "outline-width:1px;\n"
                                        "outline-color:rgb(255, 170, 127);\n"
                                        "outline-offset:2px;\n"
                                        "}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet(u"#pushButton_11:hover{\n"
                                         "background-color:rgba(0, 136, 204, 90);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_11:pressed{\n"
                                         "background-color:rgba(0, 136, 204, 40);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_11{\n"
                                         "background-color:rgba(0, 170, 255, 140);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "font: 11pt \"\u9ed1\u4f53\";\n"
                                         "font-style:normal;\n"
                                         "font-weight:normal;\n"
                                         "\n"
                                         "text-align:center;\n"
                                         "direction:rtl;\n"
                                         "vertical-align:middle;\n"
                                         "text-transform:uppercase;\n"
                                         "line-heighr:1.0;\n"
                                         "white-space:nowrap;\n"
                                         "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                         "border-style:solid;\n"
                                         "border-width:1px;\n"
                                         "border-color:rgba(255, 170, 0,255);\n"
                                         "border-radius:6px;\n"
                                         "outline-style:solid;\n"
                                         "outline-offset:1px;\n"
                                         "outline-width:1px;\n"
                                         "outline-color:rgb(255, 170, 127);\n"
                                         "outline-offset:2px;\n"
                                         "}")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMaximumSize(QSize(1677, 1677))
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet(u"#pushButton_10:hover{\n"
                                         "background-color:rgba(0, 136, 204, 90);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_10:pressed{\n"
                                         "background-color:rgba(0, 136, 204, 40);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_10{\n"
                                         "background-color:rgba(0, 170, 255, 140);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "font: 11pt \"\u9ed1\u4f53\";\n"
                                         "font-style:normal;\n"
                                         "font-weight:normal;\n"
                                         "\n"
                                         "text-align:center;\n"
                                         "direction:rtl;\n"
                                         "vertical-align:middle;\n"
                                         "text-transform:uppercase;\n"
                                         "line-heighr:1.0;\n"
                                         "white-space:nowrap;\n"
                                         "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                         "border-style:solid;\n"
                                         "border-width:1px;\n"
                                         "border-color:rgba(255, 170, 0,255);\n"
                                         "border-radius:6px;\n"
                                         "outline-style:solid;\n"
                                         "outline-offset:1px;\n"
                                         "outline-width:1px;\n"
                                         "outline-color:rgb(255, 170, 127);\n"
                                         "outline-offset:2px;\n"
                                         "}")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_10, 3, 0, 1, 1)
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet(u"#pushButton_12:hover{\n"
                                         "background-color:rgba(0, 136, 204, 90);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_12:pressed{\n"
                                         "background-color:rgba(0, 136, 204, 40);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "}\n"
                                         "#pushButton_12{\n"
                                         "background-color:rgba(0, 170, 255, 140);\n"
                                         "color:rgb(255, 170, 255);\n"
                                         "font: 11pt \"\u9ed1\u4f53\";\n"
                                         "font-style:normal;\n"
                                         "font-weight:normal;\n"
                                         "\n"
                                         "text-align:center;\n"
                                         "direction:rtl;\n"
                                         "vertical-align:middle;\n"
                                         "text-transform:uppercase;\n"
                                         "line-heighr:1.0;\n"
                                         "white-space:nowrap;\n"
                                         "test-shadow:2px 2px 2px rgb(0, 170, 255);\n"
                                         "border-style:solid;\n"
                                         "border-width:1px;\n"
                                         "border-color:rgba(255, 170, 0,255);\n"
                                         "border-radius:6px;\n"
                                         "outline-style:solid;\n"
                                         "outline-offset:1px;\n"
                                         "outline-width:1px;\n"
                                         "outline-color:rgb(255, 170, 127);\n"
                                         "outline-offset:2px;\n"
                                         "}")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoDefault(True)
        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 859, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.pushButton.setDefault(False)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"图像增强工具", None))
        self.pushButton_13.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u7247\u76ee\u5f55", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"MSRCP", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"HE", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"MSRCR", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"ACE", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"SSR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CLAHE", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SCB", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"AMSRCR", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"MSR", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"USM", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"SHARP", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"USM+", None))
        # retranslateUi
        self.pushButton.setDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton.clicked.connect(lambda: en.HE(img_list))
        self.pushButton_2.clicked.connect(lambda: en.CLAHE(img_list))
        self.pushButton_3.clicked.connect(lambda: en.simplestColorBalance1(img_list))
        self.pushButton_4.clicked.connect(lambda: en.singleScaleRetinex1(img_list))
        self.pushButton_5.clicked.connect(lambda: en.multiScaleRetinex1(img_list))
        self.pushButton_6.clicked.connect(lambda: en.MSRCR(img_list))
        self.pushButton_7.clicked.connect(lambda: en.AMSRCR(img_list))
        self.pushButton_8.clicked.connect(lambda: en.MSRCP(img_list))
        self.pushButton_9.clicked.connect(lambda: en.ACE(img_list))
        self.pushButton_10.clicked.connect(lambda: en.sharp(img_list))
        self.pushButton_11.clicked.connect(lambda: en.USM(img_list))
        self.pushButton_12.clicked.connect(lambda: en.USM1(img_list))
        QMetaObject.connectSlotsByName(MainWindow)


# 显示图像
def showimage(img1, img2):
    cv2.destroyAllWindows()
    both = np.hstack((img1, img2))
    cv2.imshow('img', both)
    cv2.waitKey(0)


# 图像增强类
class Enhancements(object):
    @staticmethod
    def stretchImage(data, s=0.005, bins=1000):  # 线性拉伸，去掉最大最小0.5%的像素值，然后线性拉伸至[0,1]
        ht = np.histogram(data, bins)
        d = np.cumsum(ht[0]) / float(data.size)
        lmin = 0
        lmax = bins - 1
        while lmin < bins:
            if d[lmin] >= s:
                break
            lmin += 1
        while lmax >= 0:
            if d[lmax] <= 1 - s:
                break
            lmax -= 1
        return np.clip((data - ht[1][lmin]) / (ht[1][lmax] - ht[1][lmin]), 0, 1)

    @staticmethod
    def getPara(radius=3):  # 根据半径计算权重参数矩阵
        g_para = {}
        m = g_para.get(radius, None)
        if m is not None:
            return m
        size = radius * 2 + 1
        m = np.zeros((size, size))
        for h in range(-radius, radius + 1):
            for w in range(-radius, radius + 1):
                if h == 0 and w == 0:
                    continue
                m[radius + h, radius + w] = 1.0 / math.sqrt(h ** 2 + w ** 2)
        m /= m.sum()
        g_para[radius] = m
        return m

    def zmIce(self, I, ratio=1.0, radius=3):  # 常规的ACE实现
        para = self.getPara(radius)
        height, width = I.shape
        zh, zw = [0] * radius + list(range(height)) + [height - 1] * radius, [0] * radius + list(range(width)) + [
            width - 1] * radius
        Z = I[np.ix_(zh, zw)]
        res = np.zeros(I.shape)
        for h in range(radius * 2 + 1):
            for w in range(radius * 2 + 1):
                if para[h][w] == 0:
                    continue
                res += (para[h][w] * np.clip((I - Z[h:h + height, w:w + width]) * ratio, -1, 1))
        return res

    def zmIceFast(self, I, ratio=1.0, radius=3):  # 单通道ACE快速增强实现
        height, width = I.shape[:2]
        if min(height, width) <= 2:
            return np.zeros(I.shape) + 0.5
        Rs = cv2.resize(I, ((width + 1) // 2, (height + 1) // 2))
        Rf = self.zmIceFast(Rs, ratio, radius)  # 递归调用
        Rf = cv2.resize(Rf, (width, height))
        Rs = cv2.resize(Rs, (width, height))
        return Rf + self.zmIce(I, ratio, radius) - self.zmIce(Rs, ratio, radius)

    # ACE增强
    def ACE(self, img_list, ratio=1.0, radius=3):  # rgb三通道分别增强，ratio是对比度增强因子，radius是卷积模板半径
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            I = img / 255.0
            res = np.zeros(I.shape)
            for k in range(3):
                res[:, :, k] = self.stretchImage(self.zmIceFast(I[:, :, k], ratio, radius))
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', res*255.0)
            thread = Thread(target=showimage, args=(I, res))
            thread.start()

    @staticmethod
    def singleScaleRetinex(img, sigma=300):
        retinex = np.log10(img + 0.001) - np.log10(cv2.GaussianBlur(img + 0.001, (0, 0), sigma))
        return retinex

    @staticmethod
    def touint8(img):
        for i in range(img.shape[2]):
            img[:, :, i] = (img[:, :, i] - np.min(img[:, :, i])) / (np.max(img[:, :, i]) - np.min(img[:, :, i])) * 255
        img = np.uint8(np.minimum(np.maximum(img, 0), 255))
        return img

    # SSR增强
    def singleScaleRetinex1(self, img_list, sigma=300):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            img = np.float64(img) + 1.0
            temp = cv2.GaussianBlur(img, (0, 0), sigma)
            gaussian = np.where(temp == 0, 0.01, temp)
            img_ssr = np.log10(img + 0.01) - np.log10(gaussian)
            img_ssr = self.touint8(img_ssr)
            img_ssr = self.simplestColorBalance(img_ssr)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', img_ssr)
            thread = Thread(target=showimage, args=(img1, img_ssr))
            thread.start()

    def multiScaleRetinex(self, img):
        sigma_list = [15, 80, 120]
        retinex = np.zeros_like(img)
        for sigma in sigma_list:
            retinex += self.singleScaleRetinex(img, sigma)
        retinex = retinex / len(sigma_list)
        return retinex

    # MSR增强
    def multiScaleRetinex1(self, img_list):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            img = np.float64(img) + 1.0
            sigma_list = [15, 80, 120]
            retinex = np.zeros_like(img * 1.0)
            for sigma in sigma_list:
                retinex += self.singleScaleRetinexTemp(img, sigma)
            img_msr = retinex / len(sigma_list)
            img_msr = self.touint8(img_msr)
            img_msr = self.simplestColorBalance(img_msr)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', img_msr)
            thread = Thread(target=showimage, args=(img1, img_msr))
            thread.start()

    # AMSRCR增强
    def AMSRCR(self, img_list):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            img = np.float64(img) + 1.0
            img_retinex = self.multiScaleRetinex(img)
            for j in range(img_retinex.shape[2]):
                unique, count = np.unique(np.int32(img_retinex[:, :, j] * 255), return_counts=True)
                zero_count = 0
                for u, c in zip(unique, count):
                    if u == 0:
                        zero_count = c
                        break
                low_val = unique[0] / 255.0
                high_val = unique[-1] / 255.0
                for u, c in zip(unique, count):
                    if u < 0 and c < zero_count * 0.1:
                        low_val = u / 255.0
                    if u > 0 and c < zero_count * 0.1:
                        high_val = u / 255.0
                        break
                img_retinex[:, :, j] = np.maximum(np.minimum(img_retinex[:, :, j], high_val), low_val)

                img_retinex[:, :, j] = (img_retinex[:, :, j] - np.min(img_retinex[:, :, j])) / \
                                       (np.max(img_retinex[:, :, j]) - np.min(img_retinex[:, :, j])) \
                                       * 255
            img_retinex = np.uint8(img_retinex)
            img_retinex = self.simplestColorBalance(img_retinex)
            both = np.hstack((img1, img_retinex))
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', img_retinex)
            cv2.imshow('AMSRCR', both)

    # CLAHE增强
    @staticmethod
    def CLAHE(img_list):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            b, g, r = cv2.split(img)
            clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
            b = clahe.apply(b)
            g = clahe.apply(g)
            r = clahe.apply(r)
            image = cv2.merge([b, g, r])
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', image)
            thread = Thread(target=showimage, args=(img1, image))
            thread.start()

    # SHARP增强
    @staticmethod
    def sharp(img_list):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            # 拉普拉斯算子锐化
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 定义拉普拉斯算子
            dst = cv2.filter2D(img, -1, kernel=kernel)  # 调用opencv图像锐化函数
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', dst)
            thread = Thread(target=showimage, args=(img1, dst))
            thread.start()

    # USM增强
    @staticmethod
    def USM(img_list):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            blur_img = cv2.GaussianBlur(img, (0, 0), 3)
            usm = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', usm)
            thread = Thread(target=showimage, args=(img1, usm))
            thread.start()

    # USM+增强
    @staticmethod
    def USM1(img_list):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            blur_img = cv2.medianBlur(img, 3)
            usm1 = cv2.addWeighted(img, 1.5, blur_img, -0.5, 0)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', usm1)
            thread = Thread(target=showimage, args=(img1, usm1))
            thread.start()

    # HE增强
    @staticmethod
    def HE(img_list):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
            channels = cv2.split(hsv)
            cv2.equalizeHist(channels[2], channels[2])
            cv2.merge(channels, hsv)
            cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB, img)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', img)
            thread = Thread(target=showimage, args=(img1, img))
            thread.start()

    @staticmethod
    def singleScaleRetinexTemp(img_list, sigma=300):
        # 按照公式计算
        temp = cv2.GaussianBlur(img_list, (0, 0), sigma)
        gaussian = np.where(temp == 0, 0.01, temp)
        retinex = np.log10(img_list + 0.01) - np.log10(gaussian)
        return retinex

    # MSRCP增强
    def MSRCP(self, img_list, low_clip=0.1, high_clip=0.9):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            img = img + 1.0
            intensity = np.sum(img, axis=2) / img.shape[2]
            retinex = self.multiScaleRetinex(intensity)
            intensity = np.expand_dims(intensity, 2)
            retinex = np.expand_dims(retinex, 2)
            intensity1 = self.simplestColorBalance(retinex, low_clip, high_clip)
            intensity1 = (intensity1 - np.min(intensity1)) / (np.max(intensity1) - np.min(intensity1)) * 255.0 + 1.0
            img_msrcp = np.zeros_like(img)
            for y in range(img_msrcp.shape[0]):
                for x in range(img_msrcp.shape[1]):
                    B = np.max(img[y, x])
                    A = np.minimum(256.0 / B, intensity1[y, x, 0] / intensity[y, x, 0])
                    img_msrcp[y, x, 0] = A * img[y, x, 0]
                    img_msrcp[y, x, 1] = A * img[y, x, 1]
                    img_msrcp[y, x, 2] = A * img[y, x, 2]
            img_msrcp = np.uint8(img_msrcp - 1.0)
            img_msrcp = self.simplestColorBalance(img_msrcp)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', img_msrcp)
            thread = Thread(target=showimage, args=(img1, img_msrcp))
            thread.start()

    @staticmethod
    # CR增强
    def colorRestoration(img, alpha, beta):
        img_sum = np.sum(img, axis=2, keepdims=True)
        color_restoration = beta * (np.log10(alpha * img) - np.log10(img_sum))
        return color_restoration

    @staticmethod
    def simplestColorBalance(img_list, low_clip=0.01, high_clip=0.99):
        img = img_list
        total = img.shape[0] * img.shape[1]
        for j in range(img.shape[2]):
            unique, counts = np.unique(img[:, :, j], return_counts=True)
            current = 0
            low_val = 0
            high_val = 0
            for u, c in zip(unique, counts):
                if float(current) / total < low_clip:
                    low_val = u
                if float(current) / total < high_clip:
                    high_val = u
                current += c
            img[:, :, j] = np.maximum(np.minimum(img[:, :, j], high_val), low_val)
        return img

    # SCB增强
    @staticmethod
    def simplestColorBalance1(img_list, low_clip=0.01, high_clip=0.99):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            total = img.shape[0] * img.shape[1]
            low_val = 0
            high_val = 0
            for j in range(img.shape[2]):
                unique, counts = np.unique(img[:, :, j], return_counts=True)
                current = 0
                for u, c in zip(unique, counts):
                    if float(current) / total < low_clip:
                        low_val = u
                    if float(current) / total < high_clip:
                        high_val = u
                    current += c
                img[:, :, j] = np.maximum(np.minimum(img[:, :, j], high_val), low_val)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', img)
            thread = Thread(target=showimage, args=(img1, img))
            thread.start()

    # MSRCR增强
    def MSRCR(self, img_list, G=2.0, b=0.0, alpha=126.0, beta=46.0, low_clip=0.01, high_clip=0.99):
        global count
        for i in img_list:
            img = cv2.imread(os.path.join(extract_path, i))
            img1 = img.copy()
            img = np.float64(img) + 1.0
            img_retinex = self.multiScaleRetinex(img)
            img_color = self.colorRestoration(img, alpha, beta)
            img_msrcr = G * (img_retinex * img_color + b)
            img_msrcr = self.touint8(img_msrcr)
            img_msrcr = self.simplestColorBalance(img_msrcr, low_clip, high_clip)
            count += 1
            cv2.imwrite(extract_path + str(count) + '.jpg', img_msrcr)
            thread = Thread(target=showimage, args=(img1, img_msrcr))
            thread.start()


# 主函数入口
if __name__ == '__main__':
    # 初始化目录
    extract_path = 'c:'
    img_list = os.listdir(extract_path)
    count = 1


    # 读取图像目录
    def var():
        global extract_path, img_list
        extract_path = QFileDialog.getExistingDirectory()
        img_list = os.listdir(extract_path)


    # 创建图像增强对象
    en = Enhancements()
    # 创建app对象
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('111.ico'))
    # 创建窗口对象
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    # 应用窗口样式
    ui.setupUi(mainWindow)
    ui.pushButton_13.clicked.connect(lambda: var())
    # 展示窗口
    mainWindow.show()
    sys.exit(app.exec())
