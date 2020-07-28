# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:48:35 2020

@author: SZC
"""
###################################
#       QtGUI界面
###################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import qtdesigner_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 264)
        MainWindow.setMinimumSize(QtCore.QSize(320, 264))
        MainWindow.setMaximumSize(QtCore.QSize(320, 264))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"\n"
"QPushButton{\n"
"    border-radius:2;\n"
"    background-color: #E1E1E1;\n"
"    border-color:#B7B7B7;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:2;\n"
"    background-color: #E5F1FB;\n"
"    border-color:#B7B7B7;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-radius:2;\n"
"    background-color: #CCE4F7;\n"
"    border-color:#B7B7B7;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 50, 321, 151))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 0, 281, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mTextUserName = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextUserName.setFont(font)
        self.mTextUserName.setObjectName("mTextUserName")
        self.verticalLayout.addWidget(self.mTextUserName)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.mTextPassword = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextPassword.setFont(font)
        self.mTextPassword.setStyleSheet("border-color: rgb(250, 0, 0);")
        self.mTextPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mTextPassword.setObjectName("mTextPassword")
        self.verticalLayout.addWidget(self.mTextPassword)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 220, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.mBtnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.mBtnLogin.setGeometry(QtCore.QRect(226, 220, 75, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.mBtnLogin.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mBtnLogin.setFont(font)
        self.mBtnLogin.setStyleSheet("QPushButton{\n"
"    border-radius:2;\n"
"    background-color: #E1E1E1;\n"
"    border-color:#B7B7B7;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:2;\n"
"    background-color: #E5F1FB;\n"
"    border-color:#B7B7B7;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-radius:2;\n"
"    background-color: #CCE4F7;\n"
"    border-color:#B7B7B7;\n"
"}")
        self.mBtnLogin.setObjectName("mBtnLogin")
        self.mBtnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.mBtnCancel.setGeometry(QtCore.QRect(130, 220, 75, 27))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 225, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.mBtnCancel.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mBtnCancel.setFont(font)
        self.mBtnCancel.setStyleSheet("QPushButton{\n"
"    border-radius:2;\n"
"    background-color: #E1E1E1;\n"
"    border-color:#B7B7B7;\n"
"}\n"
"QPushButton:hover{\n"
"    border-radius:2;\n"
"    background-color: #E5F1FB;\n"
"    border-color:#B7B7B7;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-radius:2;\n"
"    background-color: #CCE4F7;\n"
"    border-color:#B7B7B7;\n"
"}")
        self.mBtnCancel.setObjectName("mBtnCancel")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 20, 90, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户登录"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密   码："))
        self.checkBox.setText(_translate("MainWindow", "保持登录"))
        self.mBtnLogin.setText(_translate("MainWindow", "登  录"))
        self.mBtnCancel.setText(_translate("MainWindow", "取消"))
        self.label.setText(_translate("MainWindow", "登  录"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(846, 605)
        Dialog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Dialog.setAutoFillBackground(False)
        # Dialog.setSizeGripEnabled(False)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(440, 100, 321, 151))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(440, 260, 361, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label11 = QtWidgets.QLabel(Dialog)
        self.label11.setGeometry(QtCore.QRect(440, 310, 321, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label11.setFont(font)
        self.label11.setAutoFillBackground(False)
        self.label11.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: red;")
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setWordWrap(False)
        self.label11.setObjectName("label11")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 70, 391, 331))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 400, 391, 191))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton1.setGeometry(QtCore.QRect(30, 30, 141, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton1.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 0);\n"
"")
        self.pushButton1.setObjectName("pushButton1")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(30, 160, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton2.setGeometry(QtCore.QRect(200, 30, 141, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-top-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);\n"
"")
        self.pushButton2.setObjectName("pushButton2")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(230, 120, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setAutoFillBackground(False)
        self.label2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setWordWrap(False)
        self.label2.setObjectName("label2")
        self.label9 = QtWidgets.QLabel(Dialog)
        self.label9.setGeometry(QtCore.QRect(90, 480, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label9.setFont(font)
        self.label9.setAutoFillBackground(False)
        self.label9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label9.setAlignment(QtCore.Qt.AlignCenter)
        self.label9.setWordWrap(False)
        self.label9.setObjectName("label9")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(90, 210, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setAutoFillBackground(False)
        self.label3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setWordWrap(False)
        self.label3.setObjectName("label3")
        self.label7 = QtWidgets.QLabel(Dialog)
        self.label7.setGeometry(QtCore.QRect(90, 390, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label7.setFont(font)
        self.label7.setAutoFillBackground(False)
        self.label7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label7.setAlignment(QtCore.Qt.AlignCenter)
        self.label7.setWordWrap(False)
        self.label7.setObjectName("label7")
        self.label5 = QtWidgets.QLabel(Dialog)
        self.label5.setGeometry(QtCore.QRect(90, 300, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5.setFont(font)
        self.label5.setAutoFillBackground(False)
        self.label5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setWordWrap(False)
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(Dialog)
        self.label6.setGeometry(QtCore.QRect(230, 300, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label6.setFont(font)
        self.label6.setAutoFillBackground(False)
        self.label6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label6.setAlignment(QtCore.Qt.AlignCenter)
        self.label6.setWordWrap(False)
        self.label6.setObjectName("label6")
        self.label10 = QtWidgets.QLabel(Dialog)
        self.label10.setGeometry(QtCore.QRect(230, 480, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label10.setFont(font)
        self.label10.setAutoFillBackground(False)
        self.label10.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label10.setAlignment(QtCore.Qt.AlignCenter)
        self.label10.setWordWrap(False)
        self.label10.setObjectName("label10")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(90, 120, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")
        self.label8 = QtWidgets.QLabel(Dialog)
        self.label8.setGeometry(QtCore.QRect(230, 390, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label8.setFont(font)
        self.label8.setAutoFillBackground(False)
        self.label8.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label8.setAlignment(QtCore.Qt.AlignCenter)
        self.label8.setWordWrap(False)
        self.label8.setObjectName("label8")
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(230, 210, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setAutoFillBackground(False)
        self.label4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setWordWrap(False)
        self.label4.setObjectName("label4")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 70, 331, 521))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SR 硬件生产测试系统"))
        self.label.setText(_translate("Dialog", "SR 硬件生产测试平台"))
        self.label11.setText(_translate("Dialog", "请连接扫描枪！"))
        self.groupBox_2.setTitle(_translate("Dialog", "当前状态与测试进度"))
        self.groupBox_3.setTitle(_translate("Dialog", "选项"))
        self.pushButton1.setText(_translate("Dialog", "生成PDF\n"
"写入数据库\n"
"打印标签"))
        self.checkBox.setText(_translate("Dialog", "自动运行"))
        self.pushButton2.setText(_translate("Dialog", "取消本次测试"))
        self.label2.setText(_translate("Dialog", "未连接"))
        self.label9.setText(_translate("Dialog", "功能固件版本"))
        self.label3.setText(_translate("Dialog", "控制器版本"))
        self.label7.setText(_translate("Dialog", "是否合格"))
        self.label5.setText(_translate("Dialog", "测试固件版本"))
        self.label6.setText(_translate("Dialog", "None"))
        self.label10.setText(_translate("Dialog", "None"))
        self.label1.setText(_translate("Dialog", "扫码枪状态"))
        self.label8.setText(_translate("Dialog", "None"))
        self.label4.setText(_translate("Dialog", "None"))
        self.groupBox.setTitle(_translate("Dialog", "硬件信息"))
        
###################################
#       PDF类
###################################
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.platypus import Image as reportImage
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('pingbold', 'msyh.ttf'))

# 生成PDF文件
class PDFGenerator:
    def __init__(self):
        #规定格式规范
        self.file_path = ''#当前文件夹
        self.title_style = ParagraphStyle(name="TitleStyle", fontName="pingbold", fontSize=48, alignment=TA_LEFT,)
        self.sub_title_style = ParagraphStyle(name="SubTitleStyle", fontName="pingbold", fontSize=32,
                                              textColor=colors.HexColor(0x666666), alignment=TA_LEFT, )
        self.content_style = ParagraphStyle(name="ContentStyle", fontName="pingbold", fontSize=18, leading=25, spaceAfter=20,
                                            underlineWidth=1, alignment=TA_LEFT, )
        self.foot_style = ParagraphStyle(name="FootStyle", fontName="pingbold", fontSize=14, textColor=colors.HexColor(0xB4B4B4),
                                         leading=25, spaceAfter=20, alignment=TA_CENTER, )
        self.table_title_style = ParagraphStyle(name="TableTitleStyle", fontName="pingbold", fontSize=20, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.sub_table_style = ParagraphStyle(name="SubTableTitleStyle", fontName="pingbold", fontSize=16, leading=25,
                                                spaceAfter=10, alignment=TA_LEFT, )
        self.basic_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'pingbold'),
                                       ('FONTSIZE', (0, 0), (-1, -1), 12),
                                       ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                       ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                       ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                       # 'SPAN' (列,行)坐标
                                       ('SPAN', (1, 0), (3, 0)),
                                       ('SPAN', (1, 1), (3, 1)),
                                       ('SPAN', (1, 2), (3, 2)),
                                       ('SPAN', (1, 5), (3, 5)),
                                       ('SPAN', (1, 6), (3, 6)),
                                       ('SPAN', (1, 7), (3, 7)),
                                       ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                       ])
        self.common_style = TableStyle([('FONTNAME', (0, 0), (-1, -1), 'pingbold'),
                                      ('FONTSIZE', (0, 0), (-1, -1), 12),
                                      ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                                      ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                                      ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                                     ])
        
    def genTaskPDF(self,pcb_data):
        self.pcb_data=pcb_data
        # self.filename = self.pcb_data[0]['report_code']#编号
        print(self.pcb_data[2][1])
        self.filename = self.pcb_data[2][1] #二维码数据
        print(self.filename)
        story = []
        # 首页内容
        story.append(Spacer(1, 20 * mm))
        imgofsr = reportImage('sr.png')
        # img.drawHeight = 20 * mm
        # img.drawWidth = 40 * mm
        imgofsr.hAlign = TA_LEFT
        story.append(imgofsr)
        story.append(Spacer(1, 10 * mm))
        story.append(Paragraph("测试报告", self.title_style))
        story.append(Spacer(1, 20 * mm))
        story.append(Paragraph("Test Report of PCB", self.sub_title_style))
        story.append(Spacer(1, 45 * mm))
        story.append(Paragraph("报告编号：" + self.pcb_data[0]['report_code'], self.content_style))
        story.append(Paragraph("测试名称：" + self.pcb_data[0]['task_name'], self.content_style))
        story.append(Paragraph("报告日期：" + self.pcb_data[0]['report_date'], self.content_style))
        story.append(Paragraph(" 测试人：" + self.pcb_data[0]['report_creator'], self.content_style))
        story.append(Spacer(1, 55 * mm))
        story.append(Paragraph("内部文档，请勿外传", self.foot_style))
        story.append(PageBreak())

        # 表格允许单元格内容自动换行格式设置
        stylesheet = getSampleStyleSheet()
        body_style = stylesheet["BodyText"]
        body_style.wordWrap = 'CJK'
        body_style.fontName = 'pingbold'
        body_style.fontSize = 12

        # PCB测试数据
        story.append(Paragraph("PCB测试数据", self.table_title_style))
        story.append(Spacer(1, 3 * mm))
        task_table = Table(self.pcb_data[1:], colWidths=[40 * mm, 141 * mm], rowHeights=12 * mm, style=self.common_style)
        story.append(task_table)

        story.append(Spacer(1, 10 * mm))
        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
        doc.build(story)
        print('已经生成PDF，文件名为 %s.pdf，请查看！' % self.pcb_data[2][1])

###################################
#       串口类
###################################
import serial 
import serial.tools.list_ports
 
class ReadPcbData:
    def __init__(self):
        self.connect_flag = True
        self.hd_flag = [0,0]#硬件连接标志位
        print("init the ReadPcbData")
        
    def waitForPcbData(self): 
        #调用函数即可，循环接收一行数据
        # while True:
        data=[0,0]
        if (self.is_connected()):#判断端口是否硬件连接
            self.hd_flag[1] = 1
            try:#硬件连接时，接受数据
                
                self.line = self.ser.readline()                              #读取一行数据
                if len(self.line) !=0:
                    print("Rsponse : %s" % self.line.decode('utf-8'))  #串口接收到数据，然后显示
                    data[0] = True
                else:
                    data[0] = False
                    pass
                data[1] = self.line.decode('utf-8')
            except: #情况一：读取数据时被硬件拔掉
                    #情况二：拔掉，重新硬件连接上后，还未软件连接
                if self.connect_uart()==False:
                    print("接受数据时串口被拔下！")
                else:
                    print("端口重连成功！")

        else:#无硬件连接，原有的软件连接关闭
            self.hd_flag[1]=0
            try:#尝试关闭软件连接
                self.ser.close()
            except:#第一次端口就未连接，则没有串口实例,会出现异常
                pass
            if (self.hd_flag[0]==1 and self.hd_flag[1]==0):#检测第一次硬件拔掉的下降沿，该字符只显示一次
                print("端口硬件未连接！软件连接已关闭！")
        self.hd_flag[0] = self.hd_flag[1]
        return data

    
    def connect_uart(self):
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:#判断端口是否硬件连接
            print("没有发现端口!")
            self.connect_flag = False
        else:#已硬件连接，尝试软件连接
            plist_0 = list(plist[0])
            serialName = plist_0[0]       #先自动检测串口， 检测到可用串口，取出串口名
            print("可用端口>>>",serialName)
            try:#尝试软件连接
                self.ser = serial.Serial(serialName, 115200, timeout=1)  # timeout=1s
                print("已连接端口>>>", self.ser.name,"波特率115200")
                self.connect_flag = True
            except:#软件连接失败，原因未知，插拔重试
                print("尝试连接端口失败，请拔下重试，并且检查设置！")
                self.connect_flag = False
        return self.connect_flag
    
    def is_connected(self):#判断端口是否硬件连接
        return len(list(serial.tools.list_ports.comports()))

###################################
#       数据库写入函数
###################################
import pymysql
def write_database(pcb_data):
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    
    sql = """INSERT INTO `sr_test`.`pcb_data` 
            (`user_name`, `pcb_version`, `qualified_or_not`, `firmware_version`, `pcb_numb`) 
             VALUES (%s, %s, %s, %s, %s)"""
    sr_user_name = pcb_data[1][1]
    sr_pcb_version = pcb_data[2][1]
    sr_qualified_or_not = pcb_data[3][1]
    sr_firmware_version = pcb_data[4][1]
    sr_pcb_numb = pcb_data[5][1]
    values = (sr_user_name,sr_pcb_version,sr_qualified_or_not,sr_firmware_version,sr_pcb_numb)
    try:
        cursor.execute(sql,values)
        db.commit()
        print("成功向表pcb_data中插入数据")
    except:
        db.rollback()
        print("向表pcb_data插入数据失败")
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")

###################################
#       串口任务
###################################
def runuart():
    global pcb_data
    global readpcbdata
    global thread_destroy_flag
    while thread_destroy_flag:
        recevied_data = readpcbdata.waitForPcbData()
        if recevied_data[0] is True:
            pcb_data[2][1] = recevied_data[1]
###################################
#       二维码打印函数
###################################
import win32print
import win32ui
from PIL import Image, ImageWin
import qrcode
import os

def print_barcode(imgname):
    img = qrcode.make(imgname)
    img_path = os.getcwd() + "/barcode/" + imgname + ".png"
    img.save(img_path)
    #
    # Constants for GetDeviceCaps
    #
    #
    # HORZRES / VERTRES = printable area
    #
    HORZRES = 8
    VERTRES = 10
    #
    # LOGPIXELS = dots per inch
    #
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    #
    # PHYSICALWIDTH/HEIGHT = total area
    #
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111
    #
    # PHYSICALOFFSETX/Y = left / top margin
    #
    PHYSICALOFFSETX = 112
    PHYSICALOFFSETY = 113
    
    printer_name = win32print.GetDefaultPrinter ()
    file_name = img_path
    
    #
    # You can only write a Device-independent bitmap
    #  directly to a Windows device context; therefore
    #  we need (for ease) to use the Python Imaging
    #  Library to manipulate the image.
    #
    # Create a device context from a named printer
    #  and assess the printable size of the paper.
    #
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
    printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
    
    #
    # Open the image, rotate it if it's wider than
    #  it is high, and work out how much to multiply
    #  each pixel by to get it as big as possible on
    #  the page without distorting.
    #
    bmp = Image.open (file_name)
    if bmp.size[0] > bmp.size[1]:
      bmp = bmp.rotate (90)
    
    ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
    scale = min (ratios)
    
    #
    # Start the print job, and draw the bitmap to
    #  the printer device at the scaled size.
    #
    hDC.StartDoc (file_name)
    hDC.StartPage ()
    
    dib = ImageWin.Dib (bmp)
    scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
    scaled_width = int(scaled_width/2)
    scaled_height = int(scaled_height/2)
    x1 = int ((printer_size[0] - scaled_width) / 3)+100
    y1 = int ((printer_size[1] - scaled_height) / 3)
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height
    dib.draw (hDC.GetHandleOutput (), (x1, y1, x2, y2))
    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.mBtnLogin.clicked.connect(self.onLoginClick)
        #一定要在主窗口类的初始化函数中对子窗口进行实例化，如果在其他函数中实例化子窗口
        #可能会出现子窗口闪退的问题
        self.ChildDialog = ChildWin()
   
    def onLoginClick(self):
        # print('打开子窗口！')
        self.close()
        self.ChildDialog.show()
        #连接信号
        # self.ChildDialog._signal.connect(self.getData)
    # def closeEvent(self, event):
    #     # 创建一个消息盒子（提示框）
    #     quitMsgBox = QMessageBox()
    #     # 设置提示框的标题
    #     quitMsgBox.setWindowTitle('确认窗口')
    #     # 设置提示框的内容
    #     quitMsgBox.setText('你确定退出吗？')
    #     # 创建两个点击的按钮，修改文本显示内容
    #     buttonY = QPushButton('确定')
    #     buttonN = QPushButton('取消')
    #     # 将两个按钮加到这个消息盒子中去，并指定yes和no的功能
    #     quitMsgBox.addButton(buttonY, QMessageBox.YesRole)
    #     quitMsgBox.addButton(buttonN, QMessageBox.NoRole)
    #     quitMsgBox.exec_()
    #     # 判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否则就忽略关闭事件
    #     if quitMsgBox.clickedButton() == buttonY:
    #         event.accept()
    #     else:
    #         event.ignore()
class ChildWin(QMainWindow, Ui_Dialog):
    #定义信号
    _signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(ChildWin, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.connect_event()
        self.mytimer()
        
    def connect_event(self):
        self.pushButton1.clicked.connect(self.onButton1Click) 

        #我的代码
    def onButton1Click(self):
        global pcb_data
        global test_pdf
        _translate = QtCore.QCoreApplication.translate
        self.label11.setText(_translate("Dialog", "已生成PDF,写入数据库，生成二维码，请查看"))
        test_pdf.genTaskPDF(pcb_data)
        write_database(pcb_data)
        print_barcode(pcb_data[2][1])
#         a = "ffff"
#         self.label4.setText(_translate("Dialog", a))
#         self.label4.setStyleSheet("color: rgb(255, 255, 255);\n"
# "background-color: red;\n"
# "")
        
    def mytimer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)
        
    def update(self):
        global pcb_data
        global readpcbdata #使用全局变量调用串口实例
        _translate = QtCore.QCoreApplication.translate
        #扫描枪状态
        if readpcbdata.connect_flag == True:
            self.label2.setText(_translate("Dialog", "已连接"))
            self.label2.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label11.setText(_translate("Dialog", "请扫描PCB二维码"))
        else:
            self.label2.setText(_translate("Dialog", "未连接"))
            self.label2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label11.setText(_translate("Dialog", "请连接扫码枪"))
        #PCB版本
        if pcb_data[2][1] != 'none':
            self.label4.setText(_translate("Dialog", pcb_data[2][1]))
            self.label4.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label11.setText(_translate("Dialog", "收到PCB二维码数据！"))
        else:
            self.label4.setText(_translate("Dialog", "None"))
            self.label4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label11.setText(_translate("Dialog", "请连接扫码枪"))
        
    def closeEvent(self, event):
        # 创建一个消息盒子（提示框）
        quitMsgBox = QMessageBox()
        # 设置提示框的标题
        quitMsgBox.setWindowTitle('确认窗口')
        # 设置提示框的内容
        quitMsgBox.setText('你确定退出吗？')
        # 创建两个点击的按钮，修改文本显示内容
        buttonY = QPushButton('确定')
        buttonN = QPushButton('取消')
        # 将两个按钮加到这个消息盒子中去，并指定yes和no的功能
        quitMsgBox.addButton(buttonY, QMessageBox.YesRole)
        quitMsgBox.addButton(buttonN, QMessageBox.NoRole)
        quitMsgBox.exec_()
        # 判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否则就忽略关闭事件
        if quitMsgBox.clickedButton() == buttonY:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    import threading
    thread_destroy_flag = True
    pcb_data = [ #初始化数据
        {'report_code': 'none', 
         'task_name':'第四代电气PCB测试',
         'report_date':'none',
         'report_creator':'SRUser'},
        ['user_name','SRUser'],
        ['pcb_version','none'],
        ['qualified_or_not','none'],
        ['firmwave_version','none'],
        ['pcb_numb','none']
    ]
    test_pdf = PDFGenerator()#生成PDF实例，规定PDF格式
    readpcbdata = ReadPcbData()#生成串口实例
    readpcbdata.connect_uart()

    app = QApplication(sys.argv) 
    mainwindow = MainWindow()
    # childwindow = ChildWin()
    t2 = threading.Thread(target=runuart)
    t2.start()

    mainwindow.show()
    sys.exit(app.exec_())
# 要从ui文件生成py文件，使用命令：pyuic5 -o C:\Users\liuya\Desktop\SR_work\miangui.py C:\Users\liuya\Desktop\SR_work\miangui.ui