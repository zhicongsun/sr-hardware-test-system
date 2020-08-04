# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:48:35 2020

@author: SZC
"""
##############################################################################################################
#       QtGUI界面
##############################################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import qtdesigner_rc
import version_rc

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
        self.progressBar.setProperty("value", 0)
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


class Ui_version_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(563, 430)
        dialog.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 411, 171))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/sr_new/sr_new.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 210, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 240, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 270, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(100, 300, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setGeometry(QtCore.QRect(100, 330, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(dialog)
        self.label_8.setGeometry(QtCore.QRect(100, 360, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Version"))
        self.label_2.setText(_translate("dialog", "Version 1.0"))
        self.label_3.setText(_translate("dialog", "CopeRight  © 2020 Standard Robots"))
        self.label_4.setText(_translate("dialog", "All rights reserved"))
        self.label_5.setText(_translate("dialog", "Technical support:"))
        self.label_6.setText(_translate("dialog", "SunZhicong, SUSTech, Shenzhen, China"))
        self.label_7.setText(_translate("dialog", "Email:hitsunzhicong@163.com"))
        self.label_8.setText(_translate("dialog", "Github: https://github.com/RadarSun/SR_work"))
        
##############################################################################################################
#       PDF类
##############################################################################################################
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
        self.file_path = './pdfs/'#当前文件夹
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
        print(self.pcb_data[7][1])#用pcb_nub作为二维码数据
        self.filename = self.pcb_data[7][1] 
        print(self.filename)
        story = []
        # 首页内容
        story.append(Spacer(1, 20 * mm))
        imgofsr = reportImage('sr_new.jpg')
        imgofsr.drawHeight = 20 * mm
        imgofsr.drawWidth = 100 * mm
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
        task_table = Table(self.pcb_data[1:], colWidths=[60 * mm, 120 * mm], rowHeights=12 * mm, style=self.common_style)#调整宽度高度
        story.append(task_table)

        story.append(Spacer(1, 20 * mm))
        img_uart_loss_rate = reportImage('./matplot_images/20200803001.png')
        img_uart_loss_rate.drawHeight = 80 * mm
        img_uart_loss_rate.drawWidth = 130 * mm
        img_uart_loss_rate.hAlign = TA_LEFT
        story.append(img_uart_loss_rate)

        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
        doc.build(story)
        print('已经生成PDF，文件名为 %s.pdf，请查看！' % self.pcb_data[7][1])#用pcb_num命名

##############################################################################################################
#       二维码打印函数
##############################################################################################################
import win32print
import win32ui
from PIL import Image, ImageWin,ImageDraw,ImageFont
import qrcode
import os

def print_barcode(imgname):
    img = qrcode.make(imgname)
    img_path = os.getcwd() + "/barcode/" + imgname + ".png"
    img.save(img_path)

    ttfont = ImageFont.truetype("msyh.ttf",20) 
    im = Image.open(img_path)
    draw = ImageDraw.Draw(im)
    draw.text((35,250),imgname, fill="#000000",font=ttfont)
    im.save(img_path)
    # Constants for GetDeviceCaps
    # HORZRES / VERTRES = printable area
    HORZRES = 8
    VERTRES = 10
    # LOGPIXELS = dots per inch
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    # PHYSICALWIDTH/HEIGHT = total area
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111
    # PHYSICALOFFSETX/Y = left / top margin
    PHYSICALOFFSETX = 112
    PHYSICALOFFSETY = 113
    
    printer_name = win32print.GetDefaultPrinter ()
    file_name = img_path
    # You can only write a Device-independent bitmap
    #  directly to a Windows device context; therefore
    #  we need (for ease) to use the Python Imaging
    #  Library to manipulate the image.
    #
    # Create a device context from a named printer
    #  and assess the printable size of the paper.
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES)
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT)
    printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY)
    # Open the image, rotate it if it's wider than
    #  it is high, and work out how much to multiply
    #  each pixel by to get it as big as possible on
    #  the page without distorting.
    bmp = Image.open (file_name)
    if bmp.size[0] > bmp.size[1]:
      bmp = bmp.rotate (90)
    
    ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
    scale = min (ratios)
    # Start the print job, and draw the bitmap to
    #  the printer device at the scaled size.
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


##############################################################################################################
#       串口类
##############################################################################################################
import serial 
import serial.tools.list_ports
 
class ReadPcbData:
    def __init__(self):
        self.connect_flag = True
        self.hd_flag = [0,0]#硬件连接标志位
        print("init the ReadPcbData")

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

##############################################################################################################
#       串口任务
##############################################################################################################
def runuart():
    global pcb_data
    global readpcbdata
    global uart_thread_destroy_flag
    while uart_thread_destroy_flag:
        recevied_data = readpcbdata.waitForPcbData()
        if recevied_data[0] is True:
            pcb_data[3][1] = recevied_data[1]#获取控制板（pcb）版本，对应pcb_data的pcb_version
    try:
        readpcbdata.ser.close()#得到线程结束标识，则关闭串口
    except:
        print("串口还没打开，不用重复关闭")
##############################################################################################################
#       CAN类
##############################################################################################################
import PCANBasic
from PCANBasic import *

class DriveCAN(PCANBasic):
    def can_init(self,
        chanel=PCAN_USBBUS1,
        bautrate=PCAN_BAUD_500K): #默认参数：通道、波特率

        # The Plug & Play Channel (PCAN-PCI) is initialized
        result = self.Initialize(chanel, bautrate)
        if result != PCAN_ERROR_OK:
            # An error occurred, get a text describing the error and show it
            result = self.GetErrorText(result)
            print(result[1])
        else:
            print ("PCAN-USB (Ch-1) was initialized")

    def can_filter(self,
        chanel=PCAN_USBBUS1,
        from_id=0,to_id=0x7FF,
        fileter_mode=PCAN_MODE_STANDARD): #默认参数：通道，起始id，结束id，滤波器模式（标准）

        #  The message filter is closed first to ensure the reception of the new range of IDs.
        result = self.SetValue(PCAN_USBBUS1,PCAN_MESSAGE_FILTER,PCAN_FILTER_CLOSE)
        if result != PCAN_ERROR_OK:
            # An error occurred, get a text describing the error and show it
            result = self.GetErrorText(result)
            print(result[1])
        else:
            # The message filter is configured to receive the IDs 2,3,4 and 5 on the PCAN-USB, Channel 1
            result = self.FilterMessages(chanel,from_id,to_id,fileter_mode)
            if result != PCAN_ERROR_OK:
                # An error occurred, get a text describing the error and show it
                result = objPCAN.GetErrorText(result)
                print(result[1])
            else:
                print("Filter successfully configured for IDs from %d to %d" % (from_id,to_id))

    def can_read(self,chanel=PCAN_USBBUS1): #默认参数：通道
         # All initialized channels are released
        readResult = PCAN_ERROR_OK,
        if (readResult[0] & PCAN_ERROR_QRCVEMPTY) != PCAN_ERROR_QRCVEMPTY:
            # Check the receive queue for new messages
            readResult = self.Read(chanel)
            if readResult[0] != PCAN_ERROR_QRCVEMPTY:
                # Process the received message
                # print("id = %x data=[%x %x %x %x %x %x %x %x]" 
                #       % (readResult[1].ID,
                #           readResult[1].DATA[0], 
                #           readResult[1].DATA[1], 
                #           readResult[1].DATA[2],
                #           readResult[1].DATA[3],
                #           readResult[1].DATA[4],
                #           readResult[1].DATA[5],
                #           readResult[1].DATA[6],
                #           readResult[1].DATA[7]))
                self.can_processmessage(readResult[1])
                # ProcessMessage(result[1],result[2]) # Possible processing function, ProcessMessage(msg,timestamp)
            else:
                # An error occurred, get a text describing the error and show it
                result = objPCAN.GetErrorText(readResult[0])
                # print(result[1])
                # HandleReadError(readResult[0]) # Possible errors handling function, HandleError(function_result)
        else:
            pass
    def can_processmessage(self,Result):
        if Result.ID == 0x601:
            print("id = %x data=[%x %x %x %x %x %x %x %x]" 
                      % (Result.ID,
                          Result.DATA[0], 
                          Result.DATA[1], 
                          Result.DATA[2],
                          Result.DATA[3],
                          Result.DATA[4],
                          Result.DATA[5],
                          Result.DATA[6],
                          Result.DATA[7]))
        else:
            pass

    def can_write(self,
        chanel=PCAN_USBBUS1,
        msg_type=PCAN_MESSAGE_STANDARD,
        frame_id=0x100,
        send_data=[1,2,3,4]): #默认参数：通道，帧类型（标准），帧id，发送数据（列表）

        msg = TPCANMsg()
        msg.ID = frame_id
        msg.MSGTYPE = PCAN_MESSAGE_STANDARD
        msg.LEN = len(send_data)
        for i in range(0,msg.LEN): #从0到len-1,如果发送数据有5位，则是0到4
            msg.DATA[i] = send_data[i]
        
        #  The message is sent using the PCAN-USB Channel 1
        result = self.Write(chanel,msg)
        if result != PCAN_ERROR_OK:
            # An error occurred, get a text describing the error and show it
            result = self.GetErrorText(result)
            print(result)
        else:
            print("Message sent successfully")
##############################################################################################################
#       CAN任务
##############################################################################################################
def runcan():
    global objPCAN
    global can_thread_destroy_flag
    while can_thread_destroy_flag:
        objPCAN.can_read()
    try:
        objPCAN.Uninitialize(PCAN_NONEBUS)
        print("成功关闭了CAN口")
    except:
        print("已经关闭CAN口，不用重新关闭")

##############################################################################################################
#       USB2SPI类
##############################################################################################################
from ctypes import *
import platform
from time import sleep
from usb_device import *
from usb2spi import *
from sys import *

class DriveUSB2SPI():
    def __init__(self,
        config_mode = SPI_MODE_SOFT_HDX,
        config_master = SPI_MASTER,
        config_cpol = 0,
        config_cpha = 0,
        config_lsbfirst = SPI_MSB,
        config_selpolarity = SPI_SEL_LOW,
        config_clockspeedhz = 500000):

        self.DevIndex = 0
        self.DevHandles = (c_uint * 20)()
        # 扫描设备
        self.ret = USB_ScanDevice(byref(self.DevHandles))
        if(self.ret == 0):
            print("没有SPI设备连接")
        else:
            print("有 %d SPI设备连接!" % self.ret)
            # 打开设备
            self.ret = USB_OpenDevice(self.DevHandles[self.DevIndex])
            if(bool(self.ret)==False):
                print("打开SPI设备失败")
            else:
                print("成功打开SPI设备")
                # 获取设备信息
                USB2XXXInfo = DEVICE_INFO()
                USB2XXXFunctionString = (c_char * 256)()
                self.ret = DEV_GetDeviceInfo(self.DevHandles[self.DevIndex],byref(USB2XXXInfo),byref(USB2XXXFunctionString))
                if(bool(self.ret)==False):
                    print("Get device infomation faild!")
                else:
                    print("USB2XXX device infomation:")
                    print("--Firmware Name: %s"%bytes(USB2XXXInfo.FirmwareName).decode('ascii'))
                    print("--Firmware Version: v%d.%d.%d"%((USB2XXXInfo.FirmwareVersion>>24)&0xFF,(USB2XXXInfo.FirmwareVersion>>16)&0xFF,USB2XXXInfo.FirmwareVersion&0xFFFF))
                    print("--Hardware Version: v%d.%d.%d"%((USB2XXXInfo.HardwareVersion>>24)&0xFF,(USB2XXXInfo.HardwareVersion>>16)&0xFF,USB2XXXInfo.HardwareVersion&0xFFFF))
                    print("--Build Date: %s"%bytes(USB2XXXInfo.BuildDate).decode('ascii'))
                    print("--Serial Number: ",end='')
                    for i in range(0, len(USB2XXXInfo.SerialNumber)):
                        print("%08X"%USB2XXXInfo.SerialNumber[i],end='')
                    print("")
                    print("--Function String: %s"%bytes(USB2XXXFunctionString.value).decode('ascii'))
                    
                    # 配置初始化SPI
                    SPIConfig = SPI_CONFIG()
                    SPIConfig.Mode = config_mode      # 硬件半双工模式
                    SPIConfig.Master = config_master    # 主机模式
                    SPIConfig.CPOL = config_cpol
                    SPIConfig.CPHA = config_cpha
                    SPIConfig.LSBFirst = config_lsbfirst
                    SPIConfig.SelPolarity = config_selpolarity
                    SPIConfig.ClockSpeedHz = config_clockspeedhz
                    self.ret = SPI_Init(self.DevHandles[self.DevIndex],SPI2_CS0,byref(SPIConfig))
                    if(self.ret != SPI_SUCCESS):
                        print("初始化SPI失败")
                    else:
                        print("成功初始化SPI")
    def spi_master_read(self):
        self.ReadBuffer = (c_ubyte * 16)()
        self.ret = SPI_ReadBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.ReadBuffer),len(self.ReadBuffer))
        if(self.ret != SPI_SUCCESS):
            print("SPI读取数据失败")
        else:
            print("SPI 读取的数据为:")
            for i in range(0,len(self.ReadBuffer)):
                print("%02X " % self.ReadBuffer[i],end='')
            print("")

    def spi_master_write(self):
        self.WriteBuffer = (c_ubyte * 16)()
        for i in range(0,len(self.WriteBuffer)):
            self.WriteBuffer[i] = i
        self.ret = SPI_WriteBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.WriteBuffer),len(self.WriteBuffer))
        if(self.ret != SPI_SUCCESS):
            print("SPI发送数据失败")
        else:
            print("SPI发送数据成功")

    def spi_master_write_and_read(self):
        self.ret = SPI_WriteReadBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.WriteBuffer),len(self.WriteBuffer),byref(self.ReadBuffer),len(self.ReadBuffer),10)
        if(self.ret != SPI_SUCCESS):
            print("SPI 写读数据失败")
        else:
            print("SPI 写读的数据为:")
            for i in range(0,len(self.ReadBuffer)):
                print("%02X " % self.ReadBuffer[i],end='')
            print("")
    
    def spi_close(self):
        self.ret = USB_CloseDevice(self.DevHandles[self.DevIndex])
        DLL_FreeLib()#释放dll资源
        if(bool(self.ret)):
            print("成功关闭SPI设备")
        else:
            print("无法关闭SPI设备")

##############################################################################################################
#       数据库写入函数
##############################################################################################################
import pymysql
def write_database(pcb_data):
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    
    sql = """INSERT INTO `sr_test`.`pcb_data` 
            (`admin_name`, `date_time`,`pcb_version`, `test_firmwave_version`,`qualified_or_not`, `func_firmwave_version`, 
            `pcb_numb`,`io_din`,`io_dout`,`uart115200_packet_loss_rate`,`uart115200_error_rate`,
            `uart115200_delay_time`,`can50k_packet_loss_rate`,`can50k_error_rate`) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    sr_admin_name = pcb_data[1][1]
    sr_date_time = pcb_data[2][1]
    sr_pcb_version = pcb_data[3][1]
    sr_test_firmwave_version = pcb_data[4][1]
    sr_qualified_or_not = pcb_data[5][1]
    sr_func_firmware_version = pcb_data[6][1]
    sr_pcb_numb = pcb_data[7][1]
    sr_io_din = pcb_data[8][1]
    sr_io_dout = pcb_data[9][1]
    sr_uart115200_packet_loss_rate = pcb_data[10][1]
    sr_uart115200_error_rate = pcb_data[11][1]
    sr_uart115200_delay_time = pcb_data[12][1]
    sr_can50k_packet_loss_rate = pcb_data[13][1]
    sr_can50k_error_rate = pcb_data[14][1]

    values = (sr_admin_name,sr_date_time,sr_pcb_version,sr_test_firmwave_version,sr_qualified_or_not,sr_func_firmware_version,
    sr_pcb_numb,sr_io_din,sr_io_dout,sr_uart115200_packet_loss_rate,sr_uart115200_error_rate,sr_uart115200_delay_time,
    sr_can50k_packet_loss_rate,sr_can50k_error_rate)
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

##############################################################################################################
#       通过读取数据库判断是否为管理员
##############################################################################################################
import pymysql
def is_admin(admin_name,password):#通过数据库判断是否未管理员，是则返回True,否则返回False
    global pcb_data
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    search_cmd = """select * from sr_test.administrators_data"""
    cursor.execute(search_cmd)
    admin_data = cursor.fetchall()
    each_result = []*len(admin_data)
    allow_open  =  [None,"None"]    
    for i in range(len(admin_data)):
        each_result.append((admin_name in admin_data[i]))
    result = True in each_result
    print(each_result)
    
    if result == True:
        id_admin = each_result.index(True)#记录是哪个用户
        print("用户 %s 存在" %admin_name)
        if password == admin_data[id_admin][1]:#判断密码是否正确
            allow_open[0] = True
            print("用户 %s 密码正确" % admin_name)
            pcb_data[1][1] = admin_name#为数据库的pcb_data的管理员名字赋值
            allow_open[1] = "你好管理员"
        else:
            allow_open[0] = False
            print("用户 %s 密码错误" % admin_name)
            allow_open[1]="用户存在，密码错误"
    else:
        print("用户不存在")
        allow_open[1] = "用户不存在"
    
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
    return allow_open

##############################################################################################################
#       读取数据库生成控制板PCB编号的函数
############################################################################################################## 
import pymysql
import re
import datetime

def generate_pcb_numb():#对pcb_numb和date_time都赋值
    global pcb_data
    
    #从数据库获取数据
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    search_cmd = """select * from sr_test.pcb_data"""
    cursor.execute(search_cmd)
    pcb_database_info = cursor.fetchall()
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
    
    #产生pcb_numb
    now = datetime.datetime.now()
    now_ymd = now.strftime("%Y%m%d")#获取当时的年月日
    each_result = []*len(pcb_database_info)
    for i in range(len(pcb_database_info)):#遍历数据库中的每个pcb_numb，将合格与否记录在each_result中
        comp = re.match(now_ymd, pcb_database_info[i][6])#利用正则表达式比较数据库中的编码日期是否为当天
        if pcb_database_info[i][6] == "None" or comp == None:
            each_result.append('None')
        elif (comp.span() == (0,8)) and (pcb_database_info[i][4] == 'True'):
            each_result.append('True')
        elif (comp.span() == (0,8)) and (pcb_database_info[i][4] == 'False'):
            each_result.append('False')
        else:
            print("检测pcb_numb时发现数据库内容异常，请检查")

    pcb_data[2][1] = now.strftime("%Y-%m-%d %H:%M:%S")#为数据库的pcb_data的date_time赋值
    if pcb_data[5][1] == "True":#当前待加入的pcb是合格的，产生合格编号否则产生不合格编号，编号格式：日期+T/F+合格/不合格编号
        numb = each_result.count('True')+1  #如2020年8月4号第三个合格pcb的编号pcb_numb为20200804T0003
        if len(str(numb)) == 1:
            pcb_data[7][1] = now_ymd + "T" + "000" + str(numb)
        elif len(str(numb)) == 2:
            pcb_data[7][1] = now_ymd + "T" + "00" + str(numb)
        elif len(str(numb)) == 3:
            pcb_data[7][1] = now_ymd + "T" + "0" + str(numb)        
        elif len(str(numb)) == 4:
            pcb_data[7][1] = now_ymd + "T" + str(numb)        
        else:
            print("生产超过9999个合格产品，编号不足，请修改程序")
        print("生成合格编码：%s " % pcb_data[7][1])
    elif pcb_data[5][1] == "False":
        numb = each_result.count('False')+1
        if len(str(numb)) == 1:
            pcb_data[7][1] = now_ymd + "F" + "000" + str(numb)
        elif len(str(numb)) == 2:
            pcb_data[7][1] = now_ymd + "F" + "00" + str(numb)
        elif len(str(numb)) == 3:
            pcb_data[7][1] = now_ymd + "F" + "0" + str(numb)  
        elif len(str(numb)) == 4:
            pcb_data[7][1] = now_ymd + "F" + str(numb)        
        else:
            print("生产超过9999个不合格产品，编号不足，请修改程序")
        print("生成不合格编码：%s " % pcb_data[7][1])
    else:#
        print("未进行外设检测，无法正常生成pcb_numb")

##############################################################################################################
#       主界面的类
##############################################################################################################
class MainWindow(QMainWindow,Ui_MainWindow):
    exit_flag = "x"
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.mBtnLogin.clicked.connect(self.onLoginClick)
        self.mBtnCancel.clicked.connect(self.onCancelClick)
        #一定要在主窗口类的初始化函数中对子窗口进行实例化，如果在其他函数中实例化子窗口
        #可能会出现子窗口闪退的问题
        self.ChildDialog = ChildWin()
   
    def onLoginClick(self):
        admin_name = self.mTextUserName.text()
        password = self.mTextPassword.text()
        is_admin_or_not = is_admin(admin_name,password)
        if is_admin_or_not[0] == True:
            # QMessageBox.information(None, "登录提示", "用户名：" + admin_name + "密码：" + password, QMessageBox.Ok, QMessageBox.Ok)
            self.exit_flag = "onLoginClick"
            self.close()
            self.ChildDialog.show()
        else:
            QMessageBox.information(None, "登录提示", is_admin_or_not[1], QMessageBox.Ok, QMessageBox.Ok)
    
    def onCancelClick(self):
        self.exit_flag = "x"
        self.close()

    def closeEvent(self, event):
        global uart_thread_destroy_flag
        global can_thread_destroy_flag
        if self.exit_flag == "x":
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
                uart_thread_destroy_flag = False
                can_thread_destroy_flag = False
                print("关闭GUI的时候关闭串口和CAN")
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
##############################################################################################################
#       操作界面的类
##############################################################################################################
import datetime

class ChildWin(QMainWindow, Ui_Dialog):
    #定义信号
    def __init__(self):
        super(ChildWin, self).__init__()
        self.VersionDialog = VersionWin()
        bar=self.menuBar()
        #向菜单栏中添加新的QMenu对象，父菜单
        helpbar=bar.addMenu('Help')
        helpbar.addAction('Help Document')
        about = helpbar.addMenu('About')
        about.addAction('Version')

        #单击任何Qmenu对象，都会发射信号，绑定槽函数
        helpbar.triggered[QAction].connect(self.processtrigger)
        
        self.setupUi(self)
        self.retranslateUi(self)
        self.connect_event()
        self.mytimer()
        
    def processtrigger(self,q):
        #输出那个Qmenu对象被点击
        print(q.text()+'is triggeres')
        if q.text() == "Version":
            self.VersionDialog.show()#打开版本界面
        
    def connect_event(self):
        self.pushButton1.clicked.connect(self.onButton1Click) 

    def onButton1Click(self):
        global pcb_data
        global test_pdf
        global default_pcb_data
        _translate = QtCore.QCoreApplication.translate

        # now = datetime.datetime.now()
        # pcb_data[2][1] = now.strftime("%Y-%m-%d-%H-%M")#为数据库pcb_data的date_time赋值
        # pcb_data[7][1] = pcb_data[2][1]+'001'#获取当时时间作为该控制板编号，为数据库pcb_data的pcb_numb赋值
        generate_pcb_numb()
        #封面内容赋值
        pcb_data[0]['report_code'] = pcb_data[7][1] 
        pcb_data[0]['task_name'] = '第四代电气PCB测试'
        pcb_data[0]['report_date'] = pcb_data[2][1]
        pcb_data[0]['report_creator'] = pcb_data[1][1]

        test_pdf.genTaskPDF(pcb_data)#生成PDF
        self.label11.setText(_translate("Dialog", "已生成PDF,写入数据库，生成二维码，请查看"))
        write_database(pcb_data)#写入数据库
        print_barcode(pcb_data[7][1])#pcb_numb作为编号，生成二维码
        pcb_data = default_pcb_data.copy()#写入数据一次后重置为默认数据
        
    def mytimer(self):#定时器刷新GUI界面
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)#ms
        
    def update(self):
        global pcb_data
        global readpcbdata #使用全局变量调用串口实例
        _translate = QtCore.QCoreApplication.translate

        #扫描枪状态
        if readpcbdata.connect_flag == True:
            self.label2.setText(_translate("Dialog", "已连接"))
            self.label2.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label2.setText(_translate("Dialog", "未连接"))
            self.label2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
         #控制器版本
        if pcb_data[3][1] != 'None':
            self.label4.setText(_translate("Dialog", pcb_data[3][1]))
            self.label4.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label4.setText(_translate("Dialog", "None"))
            self.label4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")

        #提示界面的信息
        if readpcbdata.connect_flag != True:
            self.label11.setText(_translate("Dialog", "请连接扫码枪"))
        elif (readpcbdata.connect_flag == True) and (pcb_data[3][1] == "None"):
            self.label11.setText(_translate("Dialog", "请扫描控制器的二维码"))
        elif (readpcbdata.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] =="None"):
            self.label11.setText(_translate("Dialog", "请烧写测试固件"))
        elif (readpcbdata.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "None"):
            self.label11.setText(_translate("Dialog", "已烧写测试固件，等待测试结果"))
        elif (readpcbdata.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "False"):
            self.label11.setText(_translate("Dialog", "控制器不合格，请点按钮生成报告与二维码"))
        elif ((readpcbdata.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "True") 
             and (pcb_data[6][1] == "None")):
            self.label11.setText(_translate("Dialog", "控制器合格，请烧录功能固件"))
        elif ((readpcbdata.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "True") 
             and (pcb_data[6][1] != "None")):
            self.label11.setText(_translate("Dialog", "功能固件已烧录，请点按钮生成报告与SN码"))
        else: 
            self.label11.setText(_translate("Dialog", "程序逻辑出错，请联系开发人员"))

        
    def closeEvent(self, event):
        global uart_thread_destroy_flag
        global can_thread_destroy_flag
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
            uart_thread_destroy_flag = False
            can_thread_destroy_flag = False
            print("关闭GUI的时候关闭串口和CAN")
            event.accept()
        else:
            event.ignore()
            
##############################################################################################################
#       版本界面的类
############################################################################################################## 
class VersionWin(QMainWindow,Ui_version_dialog):
    def __init__(self):
        super(VersionWin, self).__init__()
        self.setupUi(self)
        
##############################################################################################################
#       进程结束释放资源(未起到作用，故没使用)
##############################################################################################################
import inspect
import ctypes
 
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

##############################################################################################################
#       主函数
##############################################################################################################
if __name__ == "__main__":
    import threading
    uart_thread_destroy_flag = True
    can_thread_destroy_flag = True
    pcb_data = [ #测试的数据
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},
        ['admin_name','None'],
        ['date_time','None'],
        ['pcb_version','None'],
        ['test_firmwave_version','None'],
        ['qualified_or_not','True'],
        ['func_firmwave_version','None'],
        ['pcb_numb','None'],
        ['io_din','None'],
        ['io_dout','None'],
        ['uart115200_packet_loss_rate','None'],
        ['uart115200_error_rate','None'],
        ['uart115200_delay_time','None'],
        ['can50k_packet_loss_rate','None'],
        ['can50k_error_rate','None']
    ]
    default_pcb_data = [ #初始化数据
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},
        ['admin_name','None'],
        ['date_time','None'],
        ['pcb_version','None'],
        ['test_firmwave_version','None'],
        ['qualified_or_not','None'],
        ['func_firmwave_version','None'],
        ['pcb_numb','None'],
        ['io_din','None'],
        ['io_dout','None'],
        ['uart115200_packet_loss_rate','None'],
        ['uart115200_error_rate','None'],
        ['uart115200_delay_time','None'],
        ['can50k_packet_loss_rate','None'],
        ['can50k_error_rate','None']
    ]

    test_pdf = PDFGenerator()#生成PDF实例，规定PDF格式

    readpcbdata = ReadPcbData()#生成串口实例
    readpcbdata.connect_uart()

    objPCAN = DriveCAN()#CAN实例
    objPCAN.can_init()
    objPCAN.can_filter()

    app = QApplication(sys.argv) 
    mainwindow = MainWindow()

    uart_thread = threading.Thread(target=runuart)
    uart_thread.start()
    
    can_thread = threading.Thread(target=runcan)#非守护线程
    can_thread.start()

    mainwindow.show()
    sys.exit(app.exec_())
    
# 要从ui文件生成py文件，使用命令：pyuic5 -o C:\Users\liuya\Desktop\SR_work\miangui.py C:\Users\liuya\Desktop\SR_work\miangui.ui