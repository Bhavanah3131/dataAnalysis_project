# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledowaURk.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 551)
        font = QFont()
        font.setFamily(u"Railway")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"@font-face{\n"
"	src:url(:/fonts/1x/Railway.otf)\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2 {\n"
"	border-image: url(:/assets/1x/1x/Asset 3.png) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; /* Ensure the background does not affect child widgets */\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.outerFrame = QFrame(self.frame_2)
        self.outerFrame.setObjectName(u"outerFrame")
        self.outerFrame.setMaximumSize(QSize(873, 16777215))
        self.outerFrame.setStyleSheet(u"#outerFrame {\n"
"	border-image: url(:/assets/1x/1x/Asset 2.png) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; /* Ensure the background does not affect child widgets */\n"
"}\n"
"")
        self.outerFrame.setFrameShape(QFrame.StyledPanel)
        self.outerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.outerFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 15, 20, -1)
        self.frame_15 = QFrame(self.outerFrame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"@font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#comboBox{\n"
"	font-family:\"Railway\";\n"
"	font-size: 10pt;\n"
"}\n"
"#label_2{\n"
"	color: rgb(255, 255, 255);\n"
"	font-family:\"Railway\";\n"
"	font-size:10pt;\n"
"}\n"
"#label_3{\n"
"font-family:\"Railway\";\n"
"font-size:18pt;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, -1)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_16)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.comboBox = QComboBox(self.frame_17)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMouseTracking(False)
        self.comboBox.setTabletTracking(False)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background: transparent;\n"
"    color: white;\n"
"    border: 1px solid white;\n"
"    border-radius: 5px; /* Optional: Rounded corners */\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: transparent;\n"
"    border: none;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image:url(:/assets/1x/1x/icons8-arrow-down-100.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: rgba(0, 0, 0, 0.7);\n"
"    color: white;\n"
"    border: 1px solid white;\n"
"}\n"
"")
        self.comboBox.setInputMethodHints(Qt.ImhNone)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox.setMinimumContentsLength(5)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(False)
        self.comboBox.setModelColumn(0)

        self.verticalLayout_11.addWidget(self.comboBox, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.frame_17)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame = QFrame(self.outerFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.RightToLeft)
        self.tabWidget.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"QTabWidget{\n"
"	color: rgb(255, 255, 255);\n"
"	font-family:\"Railway\";\n"
"	font-size:8pt;\n"
"}\n"
"QTabWidget::pane {\n"
"		\n"
"        border: 0; /* Remove the border around the widget */\n"
"        background: transparent; /* Transparent background */\n"
"    }\n"
"    QTabBar::tab {\n"
"        background: transparent; /* Transparent tab background */\n"
"        color: white; /* Text color */\n"
"\n"
"    }\n"
"    QTabBar::tab:selected {\n"
"        background: rgba(255, 255, 255, 0.2); /* Semi-transparent for selected tab */\n"
"    }\n"
"    QTabBar::tab:hover {\n"
"        background: rgba(255, 255, 255, 0.1); /* Hover effect */\n"
"    }")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_15 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_20 = QFrame(self.tabWidgetPage1)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTableWidget, QTableView {\n"
"    background-color: #2b2b2b;  /* Dark gray background */\n"
"    border: 2px solid #444444;  /* Border around the table */\n"
"    border-radius: 10px;  /* Rounded corners for the table */\n"
"    color: white;  /* White text */\n"
"    gridline-color: #555555;  /* Gridline color */\n"
"    font-size: 14px;  /* Font size */\n"
"    font-family: Arial, sans-serif;  /* Font family */\n"
"    selection-background-color: #454545;  /* Background color for selected cells */\n"
"    selection-color: white;  /* Text color for selected cells */\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: #3a3a3a;  /* Header background */\n"
"    border: none;  /* No border around headers */\n"
"    color: white;  /* Header text color */\n"
"    font-size: 15px;  /* Header font size */\n"
"    font-weight: bold;  /* Bold text for headers */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #3a3a3a;  /* Header section background */\n"
"    color: white;  /* Header section text col"
                        "or */\n"
"    padding: 5px;  /* Padding inside the header */\n"
"    border: 1px solid #444444;  /* Header border */\n"
"    border-radius: 5px;  /* Rounded edges for header sections */\n"
"    text-align: center;  /* Centered header text */\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 10px;  /* Rounded top-left corner of the first section */\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 10px;  /* Rounded top-right corner of the last section */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #2b2b2b;  /* Cell background color */\n"
"    padding: 5px;  /* Padding for cell content */\n"
"    border: none;  /* No border for cells */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #555555;  /* Background for selected cells */\n"
"    color: white;  /* Text color for selected cells */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #2b2b2b;  /* Scrollbar background */\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrol"
                        "lBar::handle:vertical {\n"
"    background: #555555;  /* Scrollbar handle */\n"
"    border-radius: 5px;  /* Rounded scrollbar handle */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_16.addWidget(self.tableWidget)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.horizontalLayout_2 = QHBoxLayout(self.tabWidgetPage2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_19 = QFrame(self.tabWidgetPage2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(130, 16777212))
        self.frame_19.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"QFrame{\n"
"	\n"
"	font-size: 10pt;\n"
"	font-family: \"Railway\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#high_lbl{\n"
"	color: rgb(0, 159, 0);\n"
"	font-size: 15pt;font-family: \"Railway\";\n"
"}\n"
"#low_lbl{\n"
"	color: rgb(255, 0, 0);\n"
"	font-size: 15pt;font-family: \"Railway\";\n"
"}\n"
"#equal_lbl{\n"
"	color: rgb(255, 255, 127);\n"
"	font-size: 15pt;font-family: \"Railway\";\n"
"}\n"
"#new_lbl{\n"
"	color: rgb(0, 170, 255);\n"
"	font-size: 15pt;font-family: \"Railway\";\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 15, 0, 40)
        self.high = QLabel(self.frame_19)
        self.high.setObjectName(u"high")
        self.high.setTextFormat(Qt.AutoText)
        self.high.setScaledContents(False)
        self.high.setWordWrap(False)

        self.verticalLayout_13.addWidget(self.high)

        self.high_lbl = QLabel(self.frame_19)
        self.high_lbl.setObjectName(u"high_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.high_lbl.sizePolicy().hasHeightForWidth())
        self.high_lbl.setSizePolicy(sizePolicy1)
        self.high_lbl.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.high_lbl)

        self.low = QLabel(self.frame_19)
        self.low.setObjectName(u"low")

        self.verticalLayout_13.addWidget(self.low)

        self.low_lbl = QLabel(self.frame_19)
        self.low_lbl.setObjectName(u"low_lbl")
        sizePolicy1.setHeightForWidth(self.low_lbl.sizePolicy().hasHeightForWidth())
        self.low_lbl.setSizePolicy(sizePolicy1)
        self.low_lbl.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.low_lbl)

        self.equal = QLabel(self.frame_19)
        self.equal.setObjectName(u"equal")
        self.equal.setStyleSheet(u"#frame_19{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 8pt \"Railway\";\n"
"}")

        self.verticalLayout_13.addWidget(self.equal)

        self.equal_lbl = QLabel(self.frame_19)
        self.equal_lbl.setObjectName(u"equal_lbl")
        sizePolicy1.setHeightForWidth(self.equal_lbl.sizePolicy().hasHeightForWidth())
        self.equal_lbl.setSizePolicy(sizePolicy1)
        self.equal_lbl.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.equal_lbl)

        self.new_ = QLabel(self.frame_19)
        self.new_.setObjectName(u"new_")

        self.verticalLayout_13.addWidget(self.new_)

        self.new_lbl = QLabel(self.frame_19)
        self.new_lbl.setObjectName(u"new_lbl")
        sizePolicy1.setHeightForWidth(self.new_lbl.sizePolicy().hasHeightForWidth())
        self.new_lbl.setSizePolicy(sizePolicy1)
        self.new_lbl.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.new_lbl)


        self.horizontalLayout_2.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.tabWidgetPage2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(360, 16777215))
        self.frame_18.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#frame_18{\n"
"	font-family:\"Railway\";\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_18)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")

        self.horizontalLayout_2.addWidget(self.frame_18)

        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.verticalLayout_10.addWidget(self.tabWidget)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.outerFrame)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(430, 16777215))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	border-image: url(:/assets/1x/1x/Asset 5.png)	 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; /* Ensure the background does not affect child widgets */\n"
"}\n"
"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#label_4{\n"
"	 font-family: \"Railway\";\n"
"	font-size:30px\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(20, 20))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_4)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 150))
        self.frame_4.setStyleSheet(u"border-image: url(:/assets/1x/1x/Asset 4.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#date_label1{\n"
"	 font-family: \"Railway\";\n"
"	font-size:12px\n"
"}\n"
"#label_5{\n"
"	font-family:\"Railway\";\n"
"	font-size:12px;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.date_label1 = QLabel(self.frame_10)
        self.date_label1.setObjectName(u"date_label1")
        self.date_label1.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.date_label1, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#sale_label{\n"
"	 font-family: \"Railway\";\n"
"	font-size:30px\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sale_label = QLabel(self.frame_9)
        self.sale_label.setObjectName(u"sale_label")
        self.sale_label.setStyleSheet(u"")
        self.sale_label.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.sale_label, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setStyleSheet(u"\n"
"#frame_5{\n"
"	border-image: url(:/assets/1x/1x/Asset 4.png) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; /* Ensure the background does not affect child widgets */\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#date_label_2{\n"
"	 font-family: \"Railway\";\n"
"	font-size:12px\n"
"}\n"
"#label{\n"
"	font-family:\"Railway\";\n"
"	font-size:12px;\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)

        self.date_label_2 = QLabel(self.frame_8)
        self.date_label_2.setObjectName(u"date_label_2")
        self.date_label_2.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.date_label_2, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#buy_label{\n"
"	font-family:\"Railway\";\n"
"	font-size:30px;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.buy_label = QLabel(self.frame_7)
        self.buy_label.setObjectName(u"buy_label")
        self.buy_label.setStyleSheet(u"")
        self.buy_label.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.buy_label, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 43))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        font1 = QFont()
        font1.setPointSize(13)
        self.frame_13.setFont(font1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.inputtext = QLineEdit(self.frame_13)
        self.inputtext.setObjectName(u"inputtext")
        self.inputtext.setMinimumSize(QSize(0, 0))
        self.inputtext.setMaximumSize(QSize(16777215, 45))
        self.inputtext.setCursor(QCursor(Qt.IBeamCursor))
        self.inputtext.setLayoutDirection(Qt.LeftToRight)
        self.inputtext.setStyleSheet(u"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#inputtext{\n"
"font-family: \"Railway\";\n"
"font-size:15px;\n"
"border-image: url(:/assets/1x/1x/Asset 8.png);}\n"
"")
        self.inputtext.setAlignment(Qt.AlignCenter)
        self.inputtext.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.inputtext.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.inputtext)

        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.search_button = QPushButton(self.frame_11)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMaximumSize(QSize(150, 50))
        font2 = QFont()
        font2.setFamily(u"Railway")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.search_button.setFont(font2)
        self.search_button.setStyleSheet(u"\n"
"    @font-face {\n"
"        font-family: \"Railway\";\n"
"        src: url(:/fonts/1x/Railway.otf);\n"
"    }\n"
"#search_button{\n"
"font-family: \"Railway\";\n"
"font-size:15px;\n"
"border-image: url(:/assets/1x/1x/Asset 6.png);}")
        icon = QIcon()
        icon.addFile(u":/assets/1x/1x/Asset 7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.search_button)


        self.verticalLayout_9.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_13)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_12.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1031, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Balace", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1025540.0", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"High", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Equal", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Low", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"New", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("MainWindow", u"Table", None))
        self.high.setText(QCoreApplication.translate("MainWindow", u"High value", None))
        self.high_lbl.setText(QCoreApplication.translate("MainWindow", u"+154985232", None))
        self.low.setText(QCoreApplication.translate("MainWindow", u"Low value", None))
        self.low_lbl.setText(QCoreApplication.translate("MainWindow", u"-356565363", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"Eqal value", None))
        self.equal_lbl.setText(QCoreApplication.translate("MainWindow", u"=2548989", None))
        self.new_.setText(QCoreApplication.translate("MainWindow", u"New Value", None))
        self.new_lbl.setText(QCoreApplication.translate("MainWindow", u"2545", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("MainWindow", u"Chart", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Overview", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Your Sell", None))
        self.date_label1.setText(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy", None))
        self.sale_label.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your Buy", None))
        self.date_label_2.setText(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy", None))
        self.buy_label.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.inputtext.setInputMask("")
        self.inputtext.setText("")
        self.inputtext.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of isuuer", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

if __name__=="__main__":
        app = QApplication([])
        main = QMainWindow()
        window = Ui_MainWindow()
        window.setupUi(main)
        main.show()
        app.exec_()