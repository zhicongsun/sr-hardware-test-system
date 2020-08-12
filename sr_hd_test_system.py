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

##############################################################################################################
#       注册界面
##############################################################################################################
class Ui_Register_Dialog(object):
    def setupUi(self, Register_Dialog):
        Register_Dialog.setObjectName("Register_Dialog")
        Register_Dialog.setWindowModality(QtCore.Qt.NonModal)
        Register_Dialog.resize(322, 500)
        Register_Dialog.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Register_Dialog)
        self.centralwidget.setStyleSheet("background-color: rgb(68, 68, 68);\n"
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
        self.frame.setGeometry(QtCore.QRect(0, 50, 321, 391))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 0, 281, 158))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mTextUserName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextUserName.setFont(font)
        self.mTextUserName.setObjectName("mTextUserName")
        self.verticalLayout.addWidget(self.mTextUserName)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.mTextPassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextPassword.setFont(font)
        self.mTextPassword.setStyleSheet("border-color: rgb(250, 0, 0);")
        self.mTextPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mTextPassword.setObjectName("mTextPassword")
        self.verticalLayout.addWidget(self.mTextPassword)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 183, 68, 37))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 101, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.mTextUserName_2 = QtWidgets.QLineEdit(self.frame)
        self.mTextUserName_2.setGeometry(QtCore.QRect(20, 240, 279, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextUserName_2.setFont(font)
        self.mTextUserName_2.setObjectName("mTextUserName_2")
        self.mTextPassword_2 = QtWidgets.QLineEdit(self.frame)
        self.mTextPassword_2.setGeometry(QtCore.QRect(20, 320, 279, 29))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextPassword_2.setFont(font)
        self.mTextPassword_2.setStyleSheet("border-color: rgb(250, 0, 0);")
        self.mTextPassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mTextPassword_2.setObjectName("mTextPassword_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 111, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(170, 160, 131, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(110, 350, 191, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.mBtnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.mBtnLogin.setGeometry(QtCore.QRect(220, 460, 75, 27))
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
        self.mBtnCancel.setGeometry(QtCore.QRect(130, 460, 75, 27))
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
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 102, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        Register_Dialog.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Register_Dialog)

    def retranslateUi(self, Register_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Register_Dialog.setWindowTitle(_translate("Register_Dialog", "注册"))
        self.label_2.setText(_translate("Register_Dialog", "用户名："))
        self.label_3.setText(_translate("Register_Dialog", "密   码："))
        self.label_4.setText(_translate("Register_Dialog", "用户名："))
        self.label_5.setText(_translate("Register_Dialog", "新用户名称："))
        self.label_6.setText(_translate("Register_Dialog", "新用户密码："))
        self.label_7.setText(_translate("Register_Dialog", "注：系统管理员的账户"))
        self.label_8.setText(_translate("Register_Dialog", "注：可通过注册覆盖原账号密码"))
        self.mBtnLogin.setText(_translate("Register_Dialog", "注册"))
        self.mBtnCancel.setText(_translate("Register_Dialog", "取消"))
        self.label.setText(_translate("Register_Dialog", "注册与修改"))

##############################################################################################################
#       登录界面.ui生成的类
##############################################################################################################
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
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 0, 281, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mTextUserName = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextUserName.setFont(font)
        self.mTextUserName.setObjectName("mTextUserName")
        self.verticalLayout.addWidget(self.mTextUserName)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.mTextPassword = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.mTextPassword.setFont(font)
        self.mTextPassword.setStyleSheet("border-color: rgb(250, 0, 0);")
        self.mTextPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mTextPassword.setObjectName("mTextPassword")
        self.verticalLayout.addWidget(self.mTextPassword)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(20, 220, 81, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setChecked(True)
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
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 90, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
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
        self.mBtnCancel.setText(_translate("MainWindow", "注册"))
        self.label.setText(_translate("MainWindow", "登  录"))

##############################################################################################################
#       主界面.ui生成的类
##############################################################################################################
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1543, 642)
        Dialog.setMaximumSize(QtCore.QSize(1543, 642))
        Dialog.setBaseSize(QtCore.QSize(1543, 642))
        Dialog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Dialog.setAutoFillBackground(False)
        # Dialog.setSizeGripEnabled(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(630, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(1130, 70, 401, 381))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 341, 221))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(30, 270, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label11 = QtWidgets.QLabel(self.groupBox_2)
        self.label11.setGeometry(QtCore.QRect(30, 310, 341, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label11.setFont(font)
        self.label11.setAutoFillBackground(False)
        self.label11.setStyleSheet("background-color: rgb(215, 227, 250);\n"
"color: rgb(255, 0, 0);")
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setWordWrap(False)
        self.label11.setObjectName("label11")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(1130, 460, 401, 171))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton1.setGeometry(QtCore.QRect(150, 50, 101, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton1.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 0, 0);\n"
"background-color: rgb(85, 170, 0);\n"
"")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton2.setGeometry(QtCore.QRect(270, 50, 101, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 127);\n"
"selection-background-color: rgb(255, 0, 0);")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton3.setGeometry(QtCore.QRect(30, 50, 101, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton3.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(255, 0, 0);\n"
"background-color: rgb(55, 111, 167);")
        self.pushButton3.setObjectName("pushButton3")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 331, 561))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label3 = QtWidgets.QLabel(self.groupBox)
        self.label3.setGeometry(QtCore.QRect(40, 140, 121, 71))
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
        self.label4 = QtWidgets.QLabel(self.groupBox)
        self.label4.setGeometry(QtCore.QRect(180, 140, 121, 71))
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
        self.label7 = QtWidgets.QLabel(self.groupBox)
        self.label7.setGeometry(QtCore.QRect(40, 340, 121, 71))
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
        self.label2 = QtWidgets.QLabel(self.groupBox)
        self.label2.setGeometry(QtCore.QRect(180, 40, 121, 71))
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
        self.label10 = QtWidgets.QLabel(self.groupBox)
        self.label10.setGeometry(QtCore.QRect(180, 440, 121, 71))
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
        self.label5 = QtWidgets.QLabel(self.groupBox)
        self.label5.setGeometry(QtCore.QRect(40, 240, 121, 71))
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
        self.label8 = QtWidgets.QLabel(self.groupBox)
        self.label8.setGeometry(QtCore.QRect(180, 340, 121, 71))
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
        self.label9 = QtWidgets.QLabel(self.groupBox)
        self.label9.setGeometry(QtCore.QRect(40, 440, 121, 71))
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
        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setGeometry(QtCore.QRect(40, 40, 121, 71))
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
        self.label6 = QtWidgets.QLabel(self.groupBox)
        self.label6.setGeometry(QtCore.QRect(180, 240, 121, 71))
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
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 70, 771, 561))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label5_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label5_4.setGeometry(QtCore.QRect(100, 330, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_4.setFont(font)
        self.label5_4.setAutoFillBackground(False)
        self.label5_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_4.setWordWrap(False)
        self.label5_4.setObjectName("label5_4")
        self.label2_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label2_2.setGeometry(QtCore.QRect(180, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_2.setFont(font)
        self.label2_2.setAutoFillBackground(False)
        self.label2_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_2.setWordWrap(False)
        self.label2_2.setObjectName("label2_2")
        self.label4_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label4_4.setGeometry(QtCore.QRect(180, 290, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_4.setFont(font)
        self.label4_4.setAutoFillBackground(False)
        self.label4_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_4.setWordWrap(False)
        self.label4_4.setObjectName("label4_4")
        self.label2_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label2_3.setGeometry(QtCore.QRect(540, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_3.setFont(font)
        self.label2_3.setAutoFillBackground(False)
        self.label2_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_3.setWordWrap(False)
        self.label2_3.setObjectName("label2_3")
        self.label3_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label3_7.setGeometry(QtCore.QRect(540, 430, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_7.setFont(font)
        self.label3_7.setAutoFillBackground(False)
        self.label3_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_7.setWordWrap(False)
        self.label3_7.setObjectName("label3_7")
        self.label3_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label3_3.setGeometry(QtCore.QRect(540, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_3.setFont(font)
        self.label3_3.setAutoFillBackground(False)
        self.label3_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_3.setWordWrap(False)
        self.label3_3.setObjectName("label3_3")
        self.label5_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label5_7.setGeometry(QtCore.QRect(100, 510, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_7.setFont(font)
        self.label5_7.setAutoFillBackground(False)
        self.label5_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_7.setWordWrap(False)
        self.label5_7.setObjectName("label5_7")
        self.label4_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label4_7.setGeometry(QtCore.QRect(180, 470, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_7.setFont(font)
        self.label4_7.setAutoFillBackground(False)
        self.label4_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_7.setWordWrap(False)
        self.label4_7.setObjectName("label4_7")
        self.label5_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label5_6.setGeometry(QtCore.QRect(460, 510, 251, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_6.setFont(font)
        self.label5_6.setAutoFillBackground(False)
        self.label5_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_6.setWordWrap(False)
        self.label5_6.setObjectName("label5_6")
        self.label5_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label5_2.setGeometry(QtCore.QRect(100, 160, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_2.setFont(font)
        self.label5_2.setAutoFillBackground(False)
        self.label5_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_2.setWordWrap(False)
        self.label5_2.setObjectName("label5_2")
        self.label1_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_4.setGeometry(QtCore.QRect(20, 210, 71, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_4.setFont(font)
        self.label1_4.setAutoFillBackground(False)
        self.label1_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_4.setWordWrap(False)
        self.label1_4.setObjectName("label1_4")
        self.label1_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_6.setGeometry(QtCore.QRect(20, 390, 71, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_6.setFont(font)
        self.label1_6.setAutoFillBackground(False)
        self.label1_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_6.setWordWrap(False)
        self.label1_6.setObjectName("label1_6")
        self.label4_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label4_3.setGeometry(QtCore.QRect(540, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_3.setFont(font)
        self.label4_3.setAutoFillBackground(False)
        self.label4_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_3.setWordWrap(False)
        self.label4_3.setObjectName("label4_3")
        self.label1_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_2.setGeometry(QtCore.QRect(20, 40, 71, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_2.setFont(font)
        self.label1_2.setAutoFillBackground(False)
        self.label1_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_2.setWordWrap(False)
        self.label1_2.setObjectName("label1_2")
        self.label3_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label3_6.setGeometry(QtCore.QRect(180, 430, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_6.setFont(font)
        self.label3_6.setAutoFillBackground(False)
        self.label3_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_6.setWordWrap(False)
        self.label3_6.setObjectName("label3_6")
        self.label2_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label2_6.setGeometry(QtCore.QRect(540, 390, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_6.setFont(font)
        self.label2_6.setAutoFillBackground(False)
        self.label2_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_6.setWordWrap(False)
        self.label2_6.setObjectName("label2_6")
        self.label2_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label2_7.setGeometry(QtCore.QRect(180, 390, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_7.setFont(font)
        self.label2_7.setAutoFillBackground(False)
        self.label2_7.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_7.setWordWrap(False)
        self.label2_7.setObjectName("label2_7")
        self.label1_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_7.setGeometry(QtCore.QRect(380, 390, 71, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_7.setFont(font)
        self.label1_7.setAutoFillBackground(False)
        self.label1_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_7.setWordWrap(False)
        self.label1_7.setObjectName("label1_7")
        self.label1_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_3.setGeometry(QtCore.QRect(380, 40, 71, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_3.setFont(font)
        self.label1_3.setAutoFillBackground(False)
        self.label1_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setWordWrap(False)
        self.label1_3.setObjectName("label1_3")
        self.label5_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label5_3.setGeometry(QtCore.QRect(460, 160, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_3.setFont(font)
        self.label5_3.setAutoFillBackground(False)
        self.label5_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_3.setWordWrap(False)
        self.label5_3.setObjectName("label5_3")
        self.label3_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label3_4.setGeometry(QtCore.QRect(180, 250, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_4.setFont(font)
        self.label3_4.setAutoFillBackground(False)
        self.label3_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_4.setWordWrap(False)
        self.label3_4.setObjectName("label3_4")
        self.label2_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label2_4.setGeometry(QtCore.QRect(180, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_4.setFont(font)
        self.label2_4.setAutoFillBackground(False)
        self.label2_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_4.setWordWrap(False)
        self.label2_4.setObjectName("label2_4")
        self.label4_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label4_6.setGeometry(QtCore.QRect(540, 470, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_6.setFont(font)
        self.label4_6.setAutoFillBackground(False)
        self.label4_6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_6.setWordWrap(False)
        self.label4_6.setObjectName("label4_6")
        self.label3_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label3_2.setGeometry(QtCore.QRect(180, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_2.setFont(font)
        self.label3_2.setAutoFillBackground(False)
        self.label3_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_2.setWordWrap(False)
        self.label3_2.setObjectName("label3_2")
        self.label4_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label4_2.setGeometry(QtCore.QRect(180, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_2.setFont(font)
        self.label4_2.setAutoFillBackground(False)
        self.label4_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_2.setWordWrap(False)
        self.label4_2.setObjectName("label4_2")
        self.label1_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_8.setGeometry(QtCore.QRect(100, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_8.setFont(font)
        self.label1_8.setAutoFillBackground(False)
        self.label1_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_8.setWordWrap(False)
        self.label1_8.setObjectName("label1_8")
        self.label1_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_9.setGeometry(QtCore.QRect(100, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_9.setFont(font)
        self.label1_9.setAutoFillBackground(False)
        self.label1_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_9.setWordWrap(False)
        self.label1_9.setObjectName("label1_9")
        self.label1_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_10.setGeometry(QtCore.QRect(100, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_10.setFont(font)
        self.label1_10.setAutoFillBackground(False)
        self.label1_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_10.setWordWrap(False)
        self.label1_10.setObjectName("label1_10")
        self.label1_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_11.setGeometry(QtCore.QRect(20, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_11.setFont(font)
        self.label1_11.setAutoFillBackground(False)
        self.label1_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_11.setWordWrap(False)
        self.label1_11.setObjectName("label1_11")
        self.label1_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_12.setGeometry(QtCore.QRect(460, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_12.setFont(font)
        self.label1_12.setAutoFillBackground(False)
        self.label1_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_12.setWordWrap(False)
        self.label1_12.setObjectName("label1_12")
        self.label1_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_13.setGeometry(QtCore.QRect(460, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_13.setFont(font)
        self.label1_13.setAutoFillBackground(False)
        self.label1_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_13.setWordWrap(False)
        self.label1_13.setObjectName("label1_13")
        self.label1_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_14.setGeometry(QtCore.QRect(460, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_14.setFont(font)
        self.label1_14.setAutoFillBackground(False)
        self.label1_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_14.setWordWrap(False)
        self.label1_14.setObjectName("label1_14")
        self.label1_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_15.setGeometry(QtCore.QRect(380, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_15.setFont(font)
        self.label1_15.setAutoFillBackground(False)
        self.label1_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_15.setWordWrap(False)
        self.label1_15.setObjectName("label1_15")
        self.label1_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_16.setGeometry(QtCore.QRect(100, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_16.setFont(font)
        self.label1_16.setAutoFillBackground(False)
        self.label1_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_16.setWordWrap(False)
        self.label1_16.setObjectName("label1_16")
        self.label1_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_17.setGeometry(QtCore.QRect(100, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_17.setFont(font)
        self.label1_17.setAutoFillBackground(False)
        self.label1_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_17.setWordWrap(False)
        self.label1_17.setObjectName("label1_17")
        self.label1_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_18.setGeometry(QtCore.QRect(100, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_18.setFont(font)
        self.label1_18.setAutoFillBackground(False)
        self.label1_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_18.setWordWrap(False)
        self.label1_18.setObjectName("label1_18")
        self.label1_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_19.setGeometry(QtCore.QRect(20, 330, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_19.setFont(font)
        self.label1_19.setAutoFillBackground(False)
        self.label1_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_19.setWordWrap(False)
        self.label1_19.setObjectName("label1_19")
        self.label3_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label3_5.setGeometry(QtCore.QRect(540, 250, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3_5.setFont(font)
        self.label3_5.setAutoFillBackground(False)
        self.label3_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label3_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_5.setWordWrap(False)
        self.label3_5.setObjectName("label3_5")
        self.label1_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_5.setGeometry(QtCore.QRect(380, 210, 71, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_5.setFont(font)
        self.label1_5.setAutoFillBackground(False)
        self.label1_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 133, 131);")
        self.label1_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_5.setWordWrap(False)
        self.label1_5.setObjectName("label1_5")
        self.label5_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label5_5.setGeometry(QtCore.QRect(460, 330, 261, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5_5.setFont(font)
        self.label5_5.setAutoFillBackground(False)
        self.label5_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label5_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_5.setWordWrap(False)
        self.label5_5.setObjectName("label5_5")
        self.label4_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label4_5.setGeometry(QtCore.QRect(540, 290, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label4_5.setFont(font)
        self.label4_5.setAutoFillBackground(False)
        self.label4_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label4_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_5.setWordWrap(False)
        self.label4_5.setObjectName("label4_5")
        self.label2_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label2_5.setGeometry(QtCore.QRect(540, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2_5.setFont(font)
        self.label2_5.setAutoFillBackground(False)
        self.label2_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(4, 4, 4);")
        self.label2_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_5.setWordWrap(False)
        self.label2_5.setObjectName("label2_5")
        self.label1_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_20.setGeometry(QtCore.QRect(460, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_20.setFont(font)
        self.label1_20.setAutoFillBackground(False)
        self.label1_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_20.setWordWrap(False)
        self.label1_20.setObjectName("label1_20")
        self.label1_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_21.setGeometry(QtCore.QRect(460, 250, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_21.setFont(font)
        self.label1_21.setAutoFillBackground(False)
        self.label1_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_21.setWordWrap(False)
        self.label1_21.setObjectName("label1_21")
        self.label1_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_22.setGeometry(QtCore.QRect(460, 290, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_22.setFont(font)
        self.label1_22.setAutoFillBackground(False)
        self.label1_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_22.setWordWrap(False)
        self.label1_22.setObjectName("label1_22")
        self.label1_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_23.setGeometry(QtCore.QRect(380, 330, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_23.setFont(font)
        self.label1_23.setAutoFillBackground(False)
        self.label1_23.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_23.setWordWrap(False)
        self.label1_23.setObjectName("label1_23")
        self.label1_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_24.setGeometry(QtCore.QRect(100, 390, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_24.setFont(font)
        self.label1_24.setAutoFillBackground(False)
        self.label1_24.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_24.setWordWrap(False)
        self.label1_24.setObjectName("label1_24")
        self.label1_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_25.setGeometry(QtCore.QRect(100, 430, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_25.setFont(font)
        self.label1_25.setAutoFillBackground(False)
        self.label1_25.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_25.setWordWrap(False)
        self.label1_25.setObjectName("label1_25")
        self.label1_26 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_26.setGeometry(QtCore.QRect(100, 470, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_26.setFont(font)
        self.label1_26.setAutoFillBackground(False)
        self.label1_26.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_26.setWordWrap(False)
        self.label1_26.setObjectName("label1_26")
        self.label1_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_27.setGeometry(QtCore.QRect(20, 510, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_27.setFont(font)
        self.label1_27.setAutoFillBackground(False)
        self.label1_27.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_27.setWordWrap(False)
        self.label1_27.setObjectName("label1_27")
        self.label1_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_28.setGeometry(QtCore.QRect(460, 390, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_28.setFont(font)
        self.label1_28.setAutoFillBackground(False)
        self.label1_28.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_28.setWordWrap(False)
        self.label1_28.setObjectName("label1_28")
        self.label1_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_29.setGeometry(QtCore.QRect(460, 430, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_29.setFont(font)
        self.label1_29.setAutoFillBackground(False)
        self.label1_29.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_29.setWordWrap(False)
        self.label1_29.setObjectName("label1_29")
        self.label1_30 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_30.setGeometry(QtCore.QRect(460, 470, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_30.setFont(font)
        self.label1_30.setAutoFillBackground(False)
        self.label1_30.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_30.setWordWrap(False)
        self.label1_30.setObjectName("label1_30")
        self.label1_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label1_31.setGeometry(QtCore.QRect(380, 510, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1_31.setFont(font)
        self.label1_31.setAutoFillBackground(False)
        self.label1_31.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(185, 185, 185);")
        self.label1_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_31.setWordWrap(False)
        self.label1_31.setObjectName("label1_31")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SR 硬件生产测试系统"))
        self.label.setText(_translate("Dialog", "SR 硬件生产测试平台"))
        self.groupBox_2.setTitle(_translate("Dialog", "当前状态与测试进度"))
        self.label11.setText(_translate("Dialog", "请连接扫描枪！"))
        self.groupBox_3.setTitle(_translate("Dialog", "选项"))
        self.pushButton1.setText(_translate("Dialog", "生成PDF\n"
"写入数据库\n"
"打印标签\n"
"打印日志"))
        self.pushButton2.setText(_translate("Dialog", "取消本次测试"))
        self.pushButton3.setText(_translate("Dialog", "开始测试"))
        self.groupBox.setTitle(_translate("Dialog", "硬件信息"))
        self.label3.setText(_translate("Dialog", "控制器版本"))
        self.label4.setText(_translate("Dialog", "None"))
        self.label7.setText(_translate("Dialog", "是否合格"))
        self.label2.setText(_translate("Dialog", "未连接"))
        self.label10.setText(_translate("Dialog", "None"))
        self.label5.setText(_translate("Dialog", "测试固件版本"))
        self.label8.setText(_translate("Dialog", "None"))
        self.label9.setText(_translate("Dialog", "功能固件版本"))
        self.label1.setText(_translate("Dialog", "扫码枪状态"))
        self.label6.setText(_translate("Dialog", "None"))
        self.groupBox_4.setTitle(_translate("Dialog", "外设检测情况"))
        self.label5_4.setText(_translate("Dialog", "Note:Null"))
        self.label2_2.setText(_translate("Dialog", "None"))
        self.label4_4.setText(_translate("Dialog", "None"))
        self.label2_3.setText(_translate("Dialog", "None"))
        self.label3_7.setText(_translate("Dialog", "None"))
        self.label3_3.setText(_translate("Dialog", "None"))
        self.label5_7.setText(_translate("Dialog", "Note:Null"))
        self.label4_7.setText(_translate("Dialog", "None"))
        self.label5_6.setText(_translate("Dialog", "Note:Null"))
        self.label5_2.setText(_translate("Dialog", "Note:Null"))
        self.label1_4.setText(_translate("Dialog", "UART"))
        self.label1_6.setText(_translate("Dialog", "其他1"))
        self.label4_3.setText(_translate("Dialog", "None"))
        self.label1_2.setText(_translate("Dialog", "IO"))
        self.label3_6.setText(_translate("Dialog", "None"))
        self.label2_6.setText(_translate("Dialog", "None"))
        self.label2_7.setText(_translate("Dialog", "None"))
        self.label1_7.setText(_translate("Dialog", "其他2"))
        self.label1_3.setText(_translate("Dialog", "CAN"))
        self.label5_3.setText(_translate("Dialog", "Note:Null"))
        self.label3_4.setText(_translate("Dialog", "None"))
        self.label2_4.setText(_translate("Dialog", "None"))
        self.label4_6.setText(_translate("Dialog", "None"))
        self.label3_2.setText(_translate("Dialog", "None"))
        self.label4_2.setText(_translate("Dialog", "None"))
        self.label1_8.setText(_translate("Dialog", "DI"))
        self.label1_9.setText(_translate("Dialog", "DOR"))
        self.label1_10.setText(_translate("Dialog", "DOM"))
        self.label1_11.setText(_translate("Dialog", "Note"))
        self.label1_12.setText(_translate("Dialog", "丢包率"))
        self.label1_13.setText(_translate("Dialog", "误码率"))
        self.label1_14.setText(_translate("Dialog", "延迟"))
        self.label1_15.setText(_translate("Dialog", "Note"))
        self.label1_16.setText(_translate("Dialog", "丢包率"))
        self.label1_17.setText(_translate("Dialog", "误码率"))
        self.label1_18.setText(_translate("Dialog", "延迟"))
        self.label1_19.setText(_translate("Dialog", "Note"))
        self.label3_5.setText(_translate("Dialog", "None"))
        self.label1_5.setText(_translate("Dialog", "SPI"))
        self.label5_5.setText(_translate("Dialog", "Note:Null"))
        self.label4_5.setText(_translate("Dialog", "None"))
        self.label2_5.setText(_translate("Dialog", "None"))
        self.label1_20.setText(_translate("Dialog", "丢包率"))
        self.label1_21.setText(_translate("Dialog", "误码率"))
        self.label1_22.setText(_translate("Dialog", "延迟"))
        self.label1_23.setText(_translate("Dialog", "Note"))
        self.label1_24.setText(_translate("Dialog", "Note"))
        self.label1_25.setText(_translate("Dialog", "Note"))
        self.label1_26.setText(_translate("Dialog", "Note"))
        self.label1_27.setText(_translate("Dialog", "Note"))
        self.label1_28.setText(_translate("Dialog", "Note"))
        self.label1_29.setText(_translate("Dialog", "Note"))
        self.label1_30.setText(_translate("Dialog", "Note"))
        self.label1_31.setText(_translate("Dialog", "Note"))

##############################################################################################################
#       版本界面.ui生成的类
##############################################################################################################
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
    """PDF类

    生成PDF
    """
    def __init__(self):
        """构造函数

        规定PDF保存路径，PDF的格式规范
        """
        self.file_path = './pdfs/' # 保存路径，pdfs文件夹
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
        """生成PDF

        pcb_data的信息通过表格显示，UART等外设的通信测试结果折线图表示
        """
        self.pcb_data=pcb_data
        print("pcb_numb编号：" + self.pcb_data[7][1]) # 用pcb_nub作为二维码数据
        mainwindow.ChildDialog.textBrowser.append("pcb_numb编号：" + self.pcb_data[7][1])
        self.filename = self.pcb_data[7][1] 
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

        # PCB通信测试结果，插入图片
        # UART
        story.append(Spacer(1, 20 * mm))
        img_uart_path = "./matplot_images/" + pcb_data[7][1] + "UART.png"
        img_uart = reportImage(img_uart_path)
        img_uart.drawHeight = 80 * mm
        img_uart.drawWidth = 130 * mm
        img_uart.hAlign = TA_LEFT
        story.append(img_uart)

        # CAN
        story.append(Spacer(1, 20 * mm))
        img_can_path = "./matplot_images/" + pcb_data[7][1] + "CAN.png"
        img_can = reportImage(img_can_path)
        img_can.drawHeight = 80 * mm
        img_can.drawWidth = 130 * mm
        img_can.hAlign = TA_LEFT
        story.append(img_can)

        doc = SimpleDocTemplate(self.file_path + self.filename + ".pdf",
                                leftMargin=20 * mm, rightMargin=20 * mm, topMargin=20 * mm, bottomMargin=20 * mm)
        doc.build(story)
        print('已经生成PDF，文件名为 %s.pdf，请查看！' % self.pcb_data[7][1])#用pcb_num命名
        mainwindow.ChildDialog.textBrowser.append('已经生成PDF，文件名为 %s.pdf，请查看！' % self.pcb_data[7][1])

##############################################################################################################
#       标签打印函数
##############################################################################################################
import win32print
import win32ui
from PIL import Image, ImageWin,ImageDraw,ImageFont
import qrcode
import os
# SN码使用
import barcode
from barcode.writer import ImageWriter

def print_barcode(imgname,pcb_type):
    """打印二维码函数
    
    可支持大部分打印机机型，功能是生成SN码图片并保存在barcode/sncode文件夹，接着调用打印机打印该SN码图片
    """
    global pcb_data
    # 控制板测试通过
    if pcb_type == "True":
        # 生成二维码并保存
        EAN = barcode.get_barcode_class("code39") #设置生成一维码的类型
        ean = EAN(imgname, writer=ImageWriter())
        img_path = os.getcwd() + "/sncode/" + imgname # 这里的路径不用自己加.png，因为EAN的save函数的特性决定的
        ean.save(img_path,
        {'dpi':1200,'write_text':False}) 
        # 引入中文需要的字体：微软雅黑
        ttfont = ImageFont.truetype("msyh.ttf",180) 
        # 取出二维码图片，准备进行放缩
        img_path = img_path + ".png"
        im = Image.open(img_path)
        width = im.size[0]
        hight = im.size[1]
        # 创建空白图片，用于粘贴条形码图片和文字图片
        target = Image.new('RGBA', (hight*6, hight), (255, 255, 255))
        # 按比例缩放条形码，因为条形码是1x6的，故将条形码宽度放大为原高度x6，再x2/3，即占用最终图片长度的2/3，而高度为原高度的1/2
        width_of_sn = int (hight*6/3*2)
        hight_of_sn = int(hight/2)
        im = im.resize((width_of_sn,hight_of_sn),Image.ANTIALIAS)
        # 将SN码图片加入空白图片target，(0, 0)表示x,y轴位置 单位像素 target的左上角为原点 y轴向下 
        target.paste(im, (int((6*hight-width_of_sn)/2), 0))
        draw = ImageDraw.Draw(target)
        draw.text((int((6*hight)/2-width_of_sn/4),hight_of_sn+10),"SN:"+imgname, fill="#000000",font=ttfont)
        target.save(img_path)
    # 控制板测试不通过
    else:
        ## 不合格产品用二维码打印，去掉注释即可使用 
        # # 生成二维码并保存在barcode文件夹，以imgname.png命名
        # img = qrcode.make(imgname)
        # img_path = os.getcwd() + "/barcode/" + imgname + ".png"
        # img.save(img_path)
        # #向二维码图片的底端中加入imgname的文字，再次保存覆盖原文件
        # ttfont = ImageFont.truetype("msyh.ttf",20) 
        # im = Image.open(img_path)
        # draw = ImageDraw.Draw(im)
        # draw.text((35,250),imgname, fill="#000000",font=ttfont)
        # draw.text((85,0),pcb_data[0]['task_name'], fill="#000000",font=ttfont)
        # im.save(img_path)

        # 生成SN码并保存
        EAN = barcode.get_barcode_class("code39") #设置生成一维码的类型
        ean = EAN(imgname, writer=ImageWriter())
        img_path = os.getcwd() + "/barcode/" + imgname # 这里的路径不用自己加.png，因为EAN的save函数的特性决定的
        ean.save(img_path,
        {'dpi':1200,'write_text':False}) 
        # 引入中文需要的字体：微软雅黑
        ttfont = ImageFont.truetype("msyh.ttf",180) 
        # 取出二维码图片，准备进行放缩
        img_path = img_path + ".png"
        im = Image.open(img_path)
        width = im.size[0]
        hight = im.size[1]
        # 创建空白图片，用于粘贴条形码图片和文字图片
        target = Image.new('RGBA', (hight*6, hight), (255, 255, 255))
         # 按比例缩放条形码，因为条形码是1x6的，故将条形码宽度放大为原高度x6，再x2/3，即占用最终图片长度的2/3，而高度为原高度的1/2
        width_of_sn = int (hight*6/3*2)
        hight_of_sn = int(hight/2)
        im = im.resize((width_of_sn,hight_of_sn),Image.ANTIALIAS)
        # 将SN码图片加入空白图片target，(0, 0)表示x,y轴位置 单位像素 target的左上角为原点 y轴向下 
        target.paste(im, (int((6*hight-width_of_sn)/2), 0))
        draw = ImageDraw.Draw(target)
        draw.text((int((6*hight)/2-width_of_sn/4),hight_of_sn+10),"SN:"+imgname, fill="#000000",font=ttfont)
        draw.text((width_of_sn+int((6*hight-width_of_sn)/2),int(hight_of_sn/2)),"不合格", fill="#000000",font=ttfont)
        target.save(img_path)

    # 以下为打印功能，读取图片，按比例不失真缩放，并居中打印在标签上
    # 更改标签大小时，以下代码不需要改变，会自动读取打印机数据，只需更改打印机的配置
    # 下面这8个参数是固定的，通过GetDeviceCaps读取WIN对应的信息
    # HORZRES / VERTRES 代表可打印的区域，给GetDeviceCaps用
    HORZRES = 8
    VERTRES = 10
    # 每英寸点数，即精度
    LOGPIXELSX = 88
    LOGPIXELSY = 90
    # 物理宽度和高度
    PHYSICALWIDTH = 110
    PHYSICALHEIGHT = 111
    # 左边距和顶端边距
    PHYSICALOFFSETX = 112
    PHYSICALOFFSETY = 113
    
    printer_name = win32print.GetDefaultPrinter () # 获取已连接的打印机的名字
    file_name = img_path

    # 可以将不依赖于设备的位图bitmap直接写入设备，因此需要使用Imaging库来生成image
    # 从已连接的打印机获取设备信息，得到可以打印的标签的大小
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    printable_area = hDC.GetDeviceCaps (HORZRES), hDC.GetDeviceCaps (VERTRES) # 获取可打印的区域
    printer_size = hDC.GetDeviceCaps (PHYSICALWIDTH), hDC.GetDeviceCaps (PHYSICALHEIGHT) # 获取打印的大小 
    printer_margins = hDC.GetDeviceCaps (PHYSICALOFFSETX), hDC.GetDeviceCaps (PHYSICALOFFSETY) # 获取打印的位置

    # 打开图像，如果宽度大于高度，则乘以一个比例，尽量不失真
    bmp = Image.open (file_name)
    # 按比例放大图像
    ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
    scale = min (ratios)

    # 开始打印工作，将图片按照刚才的scaled size去打印
    hDC.StartDoc (file_name)
    hDC.StartPage ()
    
    dib = ImageWin.Dib (bmp)
    scaled_width, scaled_height = [int (scale * i) for i in bmp.size]
    x1 = int ((printer_size[0] - scaled_width) / 2) # 居中打印
    y1 = int ((printer_size[1] - scaled_height) / 2)-5 # 5为微调的高度 
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
 
class DriveUART:
    """UART驱动类

    读取串口信息，主要是扫码枪使用
    """
    def __init__(self):
        self.connect_flag = True # UART软件连接标志位，输出使用
        self.hd_flag = [0,0] # 硬件连接标志位，包括前后两个时刻的标志，用来检测拔下瞬间的下降沿，内部使用
        print("初始化DriveUART")
        mainwindow.ChildDialog.textBrowser.append("初始化DriveUART")

    def connect_uart(self):
        """UART连接函数

        判断是否硬件连接（接上串口），若是则尝试软件连接，否则提示信息
        返回：
            connect_flag: True表连接；False表连接失败
        """
        plist = list(serial.tools.list_ports.comports())
        # 判断端口是否硬件连接
        if len(plist) <= 0: 
            print("没有发现端口!")
            mainwindow.ChildDialog.textBrowser.append("没有发现端口")
            self.connect_flag = False
        # 已硬件连接，尝试软件连接
        else: 
            plist_0 = list(plist[0])
            serialName = plist_0[0] # 先自动检测串口,检测到可用串口，取出串口名，从plist_0[0]可看出目前只支持一个UART
            print("可用端口>>>",serialName)
            mainwindow.ChildDialog.textBrowser.append("可用端口>>> " + str(serialName))
            # 尝试软件连接
            try: 
                self.ser = serial.Serial(serialName, 115200, timeout=1) # timeout=1s
                print("已连接端口>>>", self.ser.name,"波特率115200")
                mainwindow.ChildDialog.textBrowser.append("已连接端口>>> " + self.ser.name + " 波特率115200")
                self.connect_flag = True
            # 软件连接失败，原因未知，插拔重试
            except: 
                print("尝试连接端口失败，请拔下重试，并且检查设置！")
                mainwindow.ChildDialog.textBrowser.append("尝试连接端口失败，请拔下重试，并且检查设置！")
                self.connect_flag = False
        return self.connect_flag
    
    def is_connected(self): 
        """判断端口是否硬件连接

        返回：已经硬件连接的端口数目
        """
        return len(list(serial.tools.list_ports.comports()))
        
    def waitForPcbData(self): 
        """数据接受函数
        
        读取一数据并显示
        """
        # 调用函数即可，循环接收一行数据
        # while True:
        data=[0,0]
        if (self.is_connected()): # 判断端口是否硬件连接
            self.hd_flag[1] = 1
            try: # 硬件连接时，接受数据
                self.line = self.ser.readline() # 读取一行数据
                if len(self.line) !=0:
                    print("Rsponse : %s" % self.line.decode('utf-8')) # 串口接收到数据，然后显示
                    mainwindow.ChildDialog.textBrowser.append("Rsponse : %s" % self.line.decode('utf-8'))
                    data[0] = True
                else:
                    data[0] = False
                    pass
                data[1] = self.line.decode('utf-8')
            except: # 情况一：读取数据时被硬件拔掉
                    # 情况二：拔掉，重新硬件连接上后，还未软件连接
                if self.connect_uart()==False:
                    print("接受数据时串口被拔下！")
                    mainwindow.ChildDialog.textBrowser.append("接受数据时串口被拔下！")
                else:
                    print("端口重连成功！")
                    mainwindow.ChildDialog.textBrowser.append("端口重连成功！")

        else: # 无硬件连接，原有的软件连接关闭
            self.hd_flag[1]=0
            try: # 尝试关闭软件连接
                self.ser.close()
            except: # 第一次端口就未连接，则没有串口实例,会出现异常
                pass
            if (self.hd_flag[0]==1 and self.hd_flag[1]==0): # 检测第一次硬件拔掉的下降沿，该字符只显示一次
                print("端口硬件未连接！软件连接已关闭！")
                mainwindow.ChildDialog.textBrowser.append("端口硬件未连接！软件连接已关闭！")
        self.hd_flag[0] = self.hd_flag[1]
        return data

##############################################################################################################
#       串口任务
##############################################################################################################
def runuart():
    """UART线程的任务函数

    如果线程标识位为True，则不断调用读取函数，对pcb_version赋值
    """
    global pcb_data
    global objUART
    global uart_thread_destroy_flag
    while uart_thread_destroy_flag:
        recevied_data = objUART.waitForPcbData()
        if recevied_data[0] is True:
            # 获取控制板（pcb）版本，对应pcb_data的pcb_version
            pcb_data[3][1] = recevied_data[1] 
    try:
        objUART.ser.close() # 得到线程结束标识，则关闭串口
    except:
        print("串口还没打开，不用重复关闭")
        mainwindow.ChildDialog.textBrowser.append("串口还没打开，不用重复关闭")

##############################################################################################################
#       CAN类
##############################################################################################################
import PCANBasic
from PCANBasic import *

class DriveCAN(PCANBasic):
    """PCAN的类
    
    继承自PCANBasic类
    """
    def can_init(self,
        chanel=PCAN_USBBUS1,
        bautrate=PCAN_BAUD_500K): #默认参数：通道、波特率
        """CAN的初始化函数

        热插拔CAN的初始化
        """
        # 初始化可热插拔的CAN
        result = self.Initialize(chanel, bautrate)
        if result != PCAN_ERROR_OK:
            # 错误发生，显示错误信息
            result = self.GetErrorText(result)
            print(result[1])
            mainwindow.ChildDialog.textBrowser.append(str(result[1]))
        else:
            print("PCAN-USB (Ch-1) 初始化成功")
            mainwindow.ChildDialog.textBrowser.append("PCAN-USB (Ch-1) 初始化成功")

    def can_filter(self,
        chanel=PCAN_USBBUS1,
        from_id=0,to_id=0x7FF,
        fileter_mode=PCAN_MODE_STANDARD): #默认参数：通道，起始id，结束id，滤波器模式（标准）
        """CAN滤波器配置函数
        """
        #  先关闭CAN滤波器，以确保接受新设的ID
        result = self.SetValue(PCAN_USBBUS1,PCAN_MESSAGE_FILTER,PCAN_FILTER_CLOSE)
        if result != PCAN_ERROR_OK:
            result = self.GetErrorText(result)
            print(result[1])
            mainwindow.ChildDialog.textBrowser.append(str(result[1]))
        else:
            # 设定滤波器的ID范围，滤波模式，CAN通道
            result = self.FilterMessages(chanel,from_id,to_id,fileter_mode)
            if result != PCAN_ERROR_OK:
                result = self.GetErrorText(result)
                print(result[1])
                mainwindow.ChildDialog.textBrowser.append(result[1])
            else:
                print("CAN滤波器成功配置，ID范围从 %d 到 %d" % (from_id,to_id))
                mainwindow.ChildDialog.textBrowser.append("CAN滤波器成功配置，ID范围从 %d 到 %d" % (from_id,to_id))

    def can_read(self,chanel=PCAN_USBBUS1): # 默认参数：通道
         # 所有初始化的通道被释放
        readResult = PCAN_ERROR_OK,
        if (readResult[0] & PCAN_ERROR_QRCVEMPTY) != PCAN_ERROR_QRCVEMPTY:
            # 确保接受队列可以接受新的信息
            readResult = self.Read(chanel)
            if readResult[0] != PCAN_ERROR_QRCVEMPTY:
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
            else:
                # 错误发生，显示信息
                result = self.GetErrorText(readResult[0])
        else:
            pass
    def can_processmessage(self,Result):
        """CAN接受数据后的处理函数
        """
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
        send_data=[1,2,3,4]): # 默认参数：通道，帧类型（标准），帧id，发送数据（列表）
        """CAN的写数据函数
        """
        msg = TPCANMsg()   
        msg.ID = frame_id
        msg.MSGTYPE = PCAN_MESSAGE_STANDARD
        msg.LEN = len(send_data)
        for i in range(0,msg.LEN): # 从0到len-1,如果发送数据有5位，则是0到4
            msg.DATA[i] = send_data[i]
        
        # 发送数据
        result = self.Write(chanel,msg)
        if result != PCAN_ERROR_OK:
            # 错误发生，显示错误信息
            result = self.GetErrorText(result)
            print(result)
            mainwindow.ChildDialog.textBrowser.append(result)
        else:
            print("CAN数据发送成功")
            mainwindow.ChildDialog.textBrowser.append("CAN数据发送成功")

##############################################################################################################
#       CAN任务
##############################################################################################################
def runcan():
    """CAN线程执行的任务函数

    如果线程标识位为True，就调用读取函数不断读取数据，否则尝试关闭CAN
    """
    global objPCAN
    global can_thread_destroy_flag
    while can_thread_destroy_flag:
        objPCAN.can_read()
    try:
        objPCAN.Uninitialize(PCAN_NONEBUS)
        print("成功关闭了CAN口")
        mainwindow.ChildDialog.textBrowser.append("成功关闭了CAN口")
    except:
        print("已经关闭CAN口，不用重新关闭")
        mainwindow.ChildDialog.textBrowser.append("已经关闭CAN口，不用重新关闭")

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
    """USB2SPI类

    实现配置、写数据、读数据、写读数据，都是主机模式
    """
    def __init__(self,
        config_mode = SPI_MODE_SOFT_HDX,
        config_master = SPI_MASTER,
        config_cpol = 0,
        config_cpha = 0,
        config_lsbfirst = SPI_MSB,
        config_selpolarity = SPI_SEL_LOW,
        config_clockspeedhz = 500000):
        """构造函数

        扫描可用的SPI，配置并开启，注意这个函数只能打开一个SPI
        """
        self.DevIndex = 0 # 关键参数，设备的ID，默认只有一个设备连接，因此赋值为0
        self.DevHandles = (c_uint * 20)()
        # 扫描设备
        self.ret = USB_ScanDevice(byref(self.DevHandles))
        if(self.ret == 0):
            print("没有SPI设备连接")
            mainwindow.ChildDialog.textBrowser.append("没有SPI设备连接")
        else:
            print("有 %d SPI设备连接!" % self.ret)
            mainwindow.ChildDialog.textBrowser.append("有 %d SPI设备连接!" % self.ret)
            # 打开设备
            self.ret = USB_OpenDevice(self.DevHandles[self.DevIndex])
            if(bool(self.ret)==False):
                print("打开SPI设备失败")
                mainwindow.ChildDialog.textBrowser.append("打开SPI设备失败")
            else:
                print("成功打开SPI设备")
                mainwindow.ChildDialog.textBrowser.append("成功打开SPI设备")
                # 获取设备信息
                USB2XXXInfo = DEVICE_INFO()
                USB2XXXFunctionString = (c_char * 256)()
                self.ret = DEV_GetDeviceInfo(self.DevHandles[self.DevIndex],byref(USB2XXXInfo),byref(USB2XXXFunctionString))
                if(bool(self.ret)==False):
                    print("Get device infomation faild!")
                    mainwindow.ChildDialog.textBrowser.append("Get device infomation faild!")
                else:
                    print("USB2XXX device infomation:")
                    mainwindow.ChildDialog.textBrowser.append("Get USB2XXX device infomation")
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
                    SPIConfig.Mode = config_mode # 硬件半双工模式
                    SPIConfig.Master = config_master # 主机模式
                    SPIConfig.CPOL = config_cpol
                    SPIConfig.CPHA = config_cpha
                    SPIConfig.LSBFirst = config_lsbfirst
                    SPIConfig.SelPolarity = config_selpolarity
                    SPIConfig.ClockSpeedHz = config_clockspeedhz
                    self.ret = SPI_Init(self.DevHandles[self.DevIndex],SPI2_CS0,byref(SPIConfig))
                    if(self.ret != SPI_SUCCESS):
                        print("初始化SPI失败")
                        mainwindow.ChildDialog.textBrowser.append("初始化SPI失败")
                    else:
                        print("成功初始化SPI")
                        mainwindow.ChildDialog.textBrowser.append("成功初始化SPI")

    def spi_master_read(self):
        """SPI主机读取函数
        
        读取数据并print
        """
        self.ReadBuffer = (c_ubyte * 16)()
        self.ret = SPI_ReadBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.ReadBuffer),len(self.ReadBuffer))
        if(self.ret != SPI_SUCCESS):
            print("SPI读取数据失败")
            mainwindow.ChildDialog.textBrowser.append("SPI读取数据失败")
        else:
            print("SPI 读取的数据为:")
            mainwindow.ChildDialog.textBrowser.append("SPI 读取的数据为:")
            for i in range(0,len(self.ReadBuffer)):
                print("%02X " % self.ReadBuffer[i],end='')
                mainwindow.ChildDialog.textBrowser.append("%02X " % self.ReadBuffer[i])
            print("")
            mainwindow.ChildDialog.textBrowser.append(" ")

    def spi_master_write(self):
        """SPI主机数据发送函数
        """
        self.WriteBuffer = (c_ubyte * 16)()
        for i in range(0,len(self.WriteBuffer)):
            self.WriteBuffer[i] = i
        self.ret = SPI_WriteBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.WriteBuffer),len(self.WriteBuffer))
        if(self.ret != SPI_SUCCESS):
            print("SPI发送数据失败")
            mainwindow.ChildDialog.textBrowser.append("SPI发送数据失败")
        else:
            print("SPI发送数据成功")
            mainwindow.ChildDialog.textBrowser.append("SPI发送数据成功")

    def spi_master_write_and_read(self):
        """SPI写读函数
        """
        self.ret = SPI_WriteReadBytes(self.DevHandles[self.DevIndex],SPI2_CS0,byref(self.WriteBuffer),len(self.WriteBuffer),byref(self.ReadBuffer),len(self.ReadBuffer),10)
        if(self.ret != SPI_SUCCESS):
            print("SPI 写读数据失败")
            mainwindow.ChildDialog.textBrowser.append("SPI 写读数据失败")
        else:
            print("SPI 写读的数据为:")
            mainwindow.ChildDialog.textBrowser.append("SPI 写读的数据为:")
            for i in range(0,len(self.ReadBuffer)):
                print("%02X " % self.ReadBuffer[i],end='')
                mainwindow.ChildDialog.textBrowser.append("%02X " % self.ReadBuffer[i])
            print("")
            mainwindow.ChildDialog.textBrowser.append("")
    
    def spi_close(self):
        """SPI关闭函数
        """
        self.ret = USB_CloseDevice(self.DevHandles[self.DevIndex])
        DLL_FreeLib() # 释放dll资源，关键
        if(bool(self.ret)):
            print("成功关闭SPI设备")
            mainwindow.ChildDialog.textBrowser.append("成功关闭SPI设备")
        else:
            print("无法关闭SPI设备")
            mainwindow.ChildDialog.textBrowser.append("无法关闭SPI设备")

##############################################################################################################
#       向数据库pcb_data和peripheral_data写入数据
##############################################################################################################
import pymysql

def write_database(pcb_data):
    """向数据库pcb_data和peripheral_data写入数据函数
    """
    # 要写入的参数赋值
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
    sr_uart9600_packet_loss_rate = pcb_data[15][1]
    sr_uart9600_error_rate = pcb_data[16][1]
    sr_uart9600_delay_time = pcb_data[17][1]
    sr_can100k_packet_loss_rate = pcb_data[18][1]
    sr_can100k_error_rate = pcb_data[19][1]

    # 连接数据库并获取光标
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
        mainwindow.ChildDialog.textBrowser.append("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()

    # 向数据库的pcb_data表中写入数据
    sql = """INSERT INTO `sr_test`.`pcb_data` 
            (`admin_name`, `date_time`,`pcb_version`, `test_firmwave_version`,`qualified_or_not`, `func_firmwave_version`, 
            `pcb_numb`,`io_din`,`io_dout`,`uart115200_packet_loss_rate`,`uart115200_error_rate`,
            `uart115200_delay_time`,`can50k_packet_loss_rate`,`can50k_error_rate`) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (sr_admin_name,sr_date_time,sr_pcb_version,sr_test_firmwave_version,sr_qualified_or_not,sr_func_firmware_version,
    sr_pcb_numb,sr_io_din,sr_io_dout,sr_uart115200_packet_loss_rate,sr_uart115200_error_rate,sr_uart115200_delay_time,
    sr_can50k_packet_loss_rate,sr_can50k_error_rate)
    try:
        cursor.execute(sql,values)
        db.commit()
        print("成功向表pcb_data中插入数据")
        mainwindow.ChildDialog.textBrowser.append("成功向表pcb_data中插入数据")
    except:
        db.rollback()
        print("向表pcb_data插入数据失败")
        mainwindow.ChildDialog.textBrowser.append("向表pcb_data插入数据失败")
    
    # 向数据库的peripheral_data表中写入数据
    sql = """INSERT INTO `sr_test`.`peripheral_data` 
        (`pcb_numb`,`io_din`,`io_dout`,
        `uart115200_packet_loss_rate`,`uart115200_error_rate`,`uart115200_delay_time`,
        `can50k_packet_loss_rate`,`can50k_error_rate`,
        `uart9600_packet_loss_rate`,`uart9600_error_rate`,`uart9600_delay_time`,
        `can100k_packet_loss_rate`,`can100k_error_rate`) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 
   
    values = (sr_pcb_numb,sr_io_din,sr_io_dout,
            sr_uart115200_packet_loss_rate,sr_uart115200_error_rate,sr_uart115200_delay_time,
            sr_can50k_packet_loss_rate,sr_can50k_error_rate,
            sr_uart9600_packet_loss_rate,sr_uart9600_error_rate,sr_uart9600_delay_time,
            sr_can100k_packet_loss_rate,sr_can100k_error_rate)
    try:
        cursor.execute(sql,values)
        db.commit()
        print("成功向表peripheral_data中插入数据")
        mainwindow.ChildDialog.textBrowser.append("成功向表peripheral_data中插入数据")
    except:
        db.rollback()
        print("向表peripheral_data插入数据失败")
        mainwindow.ChildDialog.textBrowser.append("向表peripheral_data插入数据失败")
    
    # 断开与数据库的连接
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
        mainwindow.ChildDialog.textBrowser.append("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("断开连接失败，请检查设置")

##############################################################################################################
#       通过读取数据库administrators_data判断是否为管理员
##############################################################################################################
import pymysql

def is_admin(admin_name,password):
    """判断是否为已注册的管理员
    
    通过数据库判断是否未管理员，是则返回True,否则返回False
    参数：
        admin_name: 输入的账号名。string类型
        password：输入的密码。string类型
    返回：
        allow_open[0]: 代表是否在注册列表中
        allow_open[1]: 提示信息
    """
    global pcb_data
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
        mainwindow.ChildDialog.textBrowser.append("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    search_cmd = """select * from sr_test.administrators_data"""
    cursor.execute(search_cmd)
    admin_data = cursor.fetchall()
    each_result = []*len(admin_data)
    allow_open  =  [None,"None"]    
    for i in range(len(admin_data)):
        each_result.append((admin_name in admin_data[i]))
    result = True in each_result
    # 用户存在
    if result == True:
        id_admin = each_result.index(True) # 记录是哪个用户
        print("用户 %s 存在" %admin_name)
        mainwindow.ChildDialog.textBrowser.append("用户 %s 存在" %admin_name)
        # 用户存在，密码正确
        if password == admin_data[id_admin][1]: # 判断密码是否正确
            allow_open[0] = True
            print("用户 %s 密码正确" % admin_name)
            mainwindow.ChildDialog.textBrowser.append("用户 %s 密码正确" % admin_name)
            pcb_data[1][1] = admin_name # 为数据库的pcb_data的管理员名字赋值
            allow_open[1] = "你好管理员"
        # 用户存在，密码错误
        else:
            allow_open[0] = False
            print("用户 %s 密码错误" % admin_name)
            mainwindow.ChildDialog.textBrowser.append("用户 %s 密码错误" % admin_name)
            allow_open[1]="用户存在，密码错误"
    # 用户不存在
    else:
        print("用户不存在")
        mainwindow.ChildDialog.textBrowser.append("用户不存在")
        allow_open[1] = "用户不存在"
    
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
        mainwindow.ChildDialog.textBrowser.append("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("断开连接失败，请检查设置")
    return allow_open

##############################################################################################################
#       向数据库administrators_data注册新的管理员信息
##############################################################################################################
def register_admin(new_adimn_name,new_admin_password,admin_mac_address,admin_remember):
    """向数据库administrators_data注册管理员信息

    只能由已在数据库中的成员来注册，该函数也可以用来更改密码
    """
    # 连接数据库并获取光标
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
        mainwindow.ChildDialog.textBrowser.append("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()

    # 查询当前想要注册的账户是否存在
    search_cmd = """select * from sr_test.administrators_data"""
    cursor.execute(search_cmd)
    admin_data = cursor.fetchall()
    each_result = []*len(admin_data)
    for i in range(len(admin_data)):
        each_result.append((new_adimn_name in admin_data[i]))
    result = True in each_result
    # 如果账户存在，则更新账户信息
    if result == True:
        id_admin = each_result.index(True)
        values = (new_admin_password,admin_mac_address,admin_remember,new_adimn_name,admin_data[id_admin][1],admin_data[id_admin][2],admin_data[id_admin][3])
        sql="""UPDATE `sr_test`.`administrators_data` 
                SET `administrators_password` = %s, 
                `admin_mac_address` = %s, `admin_remember` = %s 
                WHERE (`admin_name` = %s) 
                and (`administrators_password` = %s) 
                and (`admin_mac_address` = %s) and (`admin_remember` = %s)"""
        try:
            cursor.execute(sql,values)
            db.commit()
            print("成功修改账号信息")
            mainwindow.ChildDialog.textBrowser.append("成功修改账号信息")
        except:
            db.rollback()
            print("修改账号信息失败")
            mainwindow.ChildDialog.textBrowser.append("修改账号信息失败")
    # 账户不存在这写入新的信息
    else:
        # 向数据库的pcb_data表中写入数据
        sql = """INSERT INTO `sr_test`.`administrators_data` 
                (`admin_name`, `administrators_password`, `admin_mac_address`, `admin_remember`) 
                VALUES (%s, %s, %s, %s)"""

        values = (new_adimn_name,new_admin_password,admin_mac_address,admin_remember)
        try:
            cursor.execute(sql,values)
            db.commit()
            print("成功注册账号")
            mainwindow.ChildDialog.textBrowser.append("成功注册账号")
        except:
            db.rollback()
            print("注册账号失败")
            mainwindow.ChildDialog.textBrowser.append("注册账号失败")

    # 断开与数据库的连接
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
        mainwindow.ChildDialog.textBrowser.append("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("断开连接失败，请检查设置")

##############################################################################################################
#       读取数据库pcb_data表生成控制板PCB编号的函数
############################################################################################################## 
import pymysql
import re
import datetime

def generate_pcb_numb(): 
    """生成pcb_numb的函数

    查询数据库中的编号，分配新编号，编码格式：日期+T/F+号码（容量9999），如20200801T0001
    对pcb_numb和date_time都赋值
    """
    global pcb_data

    # 从数据库获取数据
    try:
        db = pymysql.connect("localhost","root","SR2020","sr_test")
        print("已连接数据库sr_test")
        mainwindow.ChildDialog.textBrowser.append("已连接数据库sr_test")
    except:
        print("连接数据库sr_test失败，以下操作无效，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("连接数据库sr_test失败，以下操作无效，请检查设置")
    cursor = db.cursor()
    search_cmd = """select * from sr_test.pcb_data"""
    cursor.execute(search_cmd)
    pcb_database_info = cursor.fetchall()
    try:
        db.close()
        print("已断开与数据库sr_test的连接")
        mainwindow.ChildDialog.textBrowser.append("已断开与数据库sr_test的连接")
    except:
        print("断开连接失败，请检查设置")
        mainwindow.ChildDialog.textBrowser.append("断开连接失败，请检查设置")
    
    # 产生pcb_numb
    now = datetime.datetime.now()
    now_ymd = now.strftime("%Y%m%d") # 获取当时的年月日
    each_result = []*len(pcb_database_info)
    for i in range(len(pcb_database_info)): # 遍历数据库中的每个pcb_numb，将合格与否记录在each_result中
        comp = re.match(now_ymd, pcb_database_info[i][6]) # 利用正则表达式比较数据库中的编码日期是否为当天
        if pcb_database_info[i][6] == "None" or comp == None:
            each_result.append('None')
        elif (comp.span() == (0,8)) and (pcb_database_info[i][4] == 'True'):
            each_result.append('True')
        elif (comp.span() == (0,8)) and (pcb_database_info[i][4] == 'False'):
            each_result.append('False')
        else:
            print("检测pcb_numb时发现数据库内容异常，请检查")
            mainwindow.ChildDialog.textBrowser.append("检测pcb_numb时发现数据库内容异常，请检查")

    pcb_data[2][1] = now.strftime("%Y-%m-%d %H:%M:%S") # 为数据库的pcb_data的date_time赋值
    if pcb_data[5][1] == "True": # 当前待加入的pcb是合格的，产生合格编号否则产生不合格编号，编号格式：日期+T/F+合格/不合格编号
        numb = each_result.count('True')+1 # 如2020年8月4号第三个合格pcb的编号pcb_numb为20200804T0003
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
            mainwindow.ChildDialog.textBrowser.append("生产超过9999个合格产品，编号不足，请修改程序")
        print("生成合格编码：%s " % pcb_data[7][1])
        mainwindow.ChildDialog.textBrowser.append("生成合格编码：%s " % pcb_data[7][1])
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
            mainwindow.ChildDialog.textBrowser.append("生产超过9999个不合格产品，编号不足，请修改程序")
        print("生成不合格编码：%s " % pcb_data[7][1])
        mainwindow.ChildDialog.textBrowser.append("生成不合格编码：%s " % pcb_data[7][1])
    else:
        print("未进行外设检测，无法正常生成pcb_numb")
        mainwindow.ChildDialog.textBrowser.append("未进行外设检测，无法正常生成pcb_numb")

##############################################################################################################
#       根据测试结果绘制UART和CAN统计表格
##############################################################################################################
import matplotlib.pyplot as plt
import os

def draw_line_chart(pcb_numb,peripheral_type,loss_rate,error_rate,delay_time = None):
    """画外设测试信息的函数

    将UART和CAN的测试指标分别用折线图绘制，图保存在matplot_images文件夹，命名pcb_numb + 外设类型
    参数：
        peripheral_type: 外设类型。string类型，"CAN" "UART"两种
        loss_rate: 丢包率，以%为单位。list类型，如[10,20,30]，10代表丢包率10%
        error_rate: 误码率，以%为单位。list类型，如[10,4,12]，10代表丢包率10%
        delay_time: 传输时延，以%为单位。list类型，如[100,120]，100代表延迟100ms
    返回：
        保存两个.png在matplot_images文件夹，命名pcb_numb + 外设类型
    """
    # 定义自己的字体，微软雅黑，否则中文显示不出来,这边不用了
    # myfont = fm.FontProperties(fname=r'.\msyh.ttf') # 设置字体,配合，需要fontproperties = myfont，import matplotlib.font_manager as fm
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 支持中文

    # 根据检测外设速度的类型显示Label
    if len(loss_rate)==1:
        x = range(1,2)
        x_label = ["50K_9600"]
    elif len(loss_rate)==2:
        x = range(1,3)
        x_label = ["50K_9600","100K_115200"]
    elif len(loss_rate)==3:
        x = range(1,4)
        x_label = ["50K_9600","100K_115200","200K_150000"]
    else:
        print("输入列表参数包含超过3个元素，有问题")
        mainwindow.ChildDialog.textBrowser.append("输入列表参数包含超过3个元素，有问题")
        pass

    # 创建画布
    plt.figure()
    # 绘图
    plt.plot(x, loss_rate, marker='o', color='r', label='丢包率')
    plt.plot(x, error_rate, marker='*', color='b', label='误码率')
    if peripheral_type == "UART": # CAN没有延迟参数
        plt.plot(x,delay_time,marker='o', color='y', label='传输延迟')
    elif peripheral_type == "CAN":
        pass
    # 显示图例（使绘制生效）
    plt.legend()
    # 横坐标名称
    plt.xlabel('波特率')
    # 横坐标刻度转换为文字
    plt.xticks([1,2],x_label)
    # 纵坐标名称
    plt.ylabel('% / ms')
    # 标题
    if peripheral_type == "UART":
        plt.title("UART通信数据统计")
    elif peripheral_type == "CAN":
        plt.title("CAN通信数据统计")
    else:
        pass

    # 保存图片到本地，命名格式：pcb_numb + 外设类型
    img_path = os.getcwd() + "/matplot_images/" + pcb_numb + peripheral_type + ".png"
    plt.savefig(img_path,dpi=500,bbox_inches = 'tight')

##############################################################################################################
#       登录界面的类
##############################################################################################################
import uuid

def get_mac_address():
    """获取电脑的mac地址
    """
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

##############################################################################################################
#       登录界面的类
##############################################################################################################
class MainWindow(QMainWindow,Ui_MainWindow):
    """登录界面的类

    继承自Ui_MainWindow，实现用户权限功能，可调用测试界面、提示错误信息
    """
    exit_flag = "x" # 关闭事件的标识位，点击了取消或者x按钮置"x"，登录测试系统后自动关闭登录界面时置"onGloginClick"
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.mBtnLogin.clicked.connect(self.onLoginClick)
        self.mBtnCancel.clicked.connect(self.onCancelClick)
        # 要在主窗口类的初始化函数中对子窗口进行实例化，如果在其他函数中实例化子窗口
        # 可能会出现子窗口闪退的问题
        self.ChildDialog = ChildWin() # 测试界面的类
        self.RegisterDialog = RegisterWin() # 注册界面的类
        [is_mac_existence,admin_name,password] = self.is_remenbered_admin()
        if is_mac_existence == "True":
            self.mTextUserName.setText(admin_name)
            self.mTextPassword.setText(password)
   
    def onLoginClick(self):
        """登录按钮的响应函数

        判断输入的账户信息是否存在数据库中，是则关闭登录界面、打开测试界面，否则提示原因
        """
        admin_name = self.mTextUserName.text()
        password = self.mTextPassword.text()
        is_admin_or_not = is_admin(admin_name,password)
        # 账户正确
        if is_admin_or_not[0] == True:
            self.exit_flag = "onLoginClick"
            # 如果选择保持登录状态，则把PC的MAC地址写入数据库，再次打开程序的时候会检测MAC地址是否匹配，匹配则自动显示账户密码
            if self.checkBox.isChecked():
                admin_mac_address = get_mac_address()
                admin_remember = "True"
                register_admin(admin_name,password,admin_mac_address,admin_remember)
            #不选择保持登录，则向MAC地址和是否保存写入"None"
            else:
                register_admin(admin_name,password,"None","None")
            self.close()
            self.ChildDialog.show()
        # 账户不正确
        else:
            self.exit_flag = "x"
            QMessageBox.information(None, "登录提示", is_admin_or_not[1], QMessageBox.Ok, QMessageBox.Ok)
    
    def onCancelClick(self):
        """取消按钮的响应函数
        
        exit_flag置"x"，关闭窗口self.close()
        """
        self.RegisterDialog.show()
        self.exit_flag = "onRegisterClick"
        self.close()

    def closeEvent(self, event):
        """窗口关闭响应事件
        
        self.close()后触发该函数
        """
        global uart_thread_destroy_flag
        global can_thread_destroy_flag
        # 根据两种窗口关闭类型，选择不同操作
        if self.exit_flag == "x": # 
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
                mainwindow.ChildDialog.textBrowser.append("关闭GUI的时候关闭串口和CAN")
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def is_remenbered_admin(self):
        """根据MAC地址返回账户信息
        
        通过数据库查询本PC的MAC地址是否存在，存在说明上次点的是保存密码，则返回对应的账户信息
        返回：
            is_mac_exitence：MAC地址是否存在标识符。string类型，"True"或者"False"
            admin_name: 输入的账号名。string类型。不存在返回"None"
            password：输入的密码。string类型。不存在返回"None"
        """
        pc_mac_address = get_mac_address()
        try:
            db = pymysql.connect("localhost","root","SR2020","sr_test")
            print("已连接数据库sr_test")
            self.ChildDialog.textBrowser.append("已连接数据库sr_test")
        except:
            print("连接数据库sr_test失败，以下操作无效，请检查设置")
            self.ChildDialog.textBrowser.append("连接数据库sr_test失败，以下操作无效，请检查设置")
        cursor = db.cursor()
        search_cmd = """select * from sr_test.administrators_data"""
        cursor.execute(search_cmd)
        admin_data = cursor.fetchall()
        each_result = []*len(admin_data)
        for i in range(len(admin_data)):
            each_result.append((pc_mac_address in admin_data[i]))
        result = True in each_result
        # MAC地址存在,将账户信息返回
        if result == True:
            id_admin = each_result.index(True) # 记录是哪个用户
            print("MAC地址 %s 存在" % pc_mac_address)
            self.ChildDialog.textBrowser.append("MAC地址 %s 存在" % pc_mac_address)
            is_mac_existence = "True"
            admin_name = admin_data[id_admin][0]
            password = admin_data[id_admin][1]
            print("根据MAC地址检查到的账户，name:%s,password:%s" %(admin_name,password))
            self.ChildDialog.textBrowser.append("根据MAC地址检查到的账户，name:%s,password:%s" %(admin_name,password))
        # MAC地址不存在
        else:
            is_mac_existence = "False"
            admin_name = "None"
            password = "None"
            print("MAC地址不存在")
            self.ChildDialog.textBrowser.append("MAC地址不存在")
        
        try:
            db.close()
            print("已断开与数据库sr_test的连接")
            self.ChildDialog.textBrowser.append("已断开与数据库sr_test的连接")
        except:
            print("断开连接失败，请检查设置")
            self.ChildDialog.textBrowser.append("断开连接失败，请检查设置")
        return [is_mac_existence,admin_name,password]


##############################################################################################################
#       注册界面的类
##############################################################################################################
class RegisterWin(QMainWindow,Ui_Register_Dialog):
    """注册界面的类
    """
    # 点击注册和取消都会调用self.close()，但两者触发的事件不同，点击注册需要出现提示窗口
    # 因此使用exit_flag来区别，self.closeEvent()中根据exit_flag的不同做不同的处理
    exit_flag = "x" 
    def __init__(self):
        super(RegisterWin, self).__init__()
        self.setupUi(self)
        # 绑定响应事件
        self.mBtnLogin.clicked.connect(self.onLoginClick)
        self.mBtnCancel.clicked.connect(self.onCancelClick)

    def onLoginClick(self):
        """注册按钮的响应函数

        判断输入的账户信息是否存在数据库中，是则关闭登录界面、打开测试界面，否则提示原因
        """
        # 读取Text上输入的信息
        admin_name = self.mTextUserName.text()
        password = self.mTextPassword.text()
        new_admin_name = self.mTextUserName_2.text()
        new_admin_password = self.mTextPassword_2.text()
        # 判断是否为管理员
        is_admin_or_not = is_admin(admin_name,password)
        # 如果系统管理员账户正确，则可以插入信息，否则显示错误原因
        if is_admin_or_not[0] == True:
            register_admin(new_admin_name,new_admin_password,"None","None") # 第一次注册时候默认不保存密码 
            self.exit_flag = "register_suscced"
            self.close()
        else:
            QMessageBox.information(None, "注册提示", is_admin_or_not[1], QMessageBox.Ok, QMessageBox.Ok)
    
    def onCancelClick(self):
        """取消按钮的响应函数
        
        """
        self.exit_flag == "x"
        self.close()

    def closeEvent(self, event):
        """窗口关闭响应事件
        
        self.close()后触发该函数
        """
        # 注册成功提示，按下“确定”或者关闭“x”则退出注册界面进入登录界面
        if self.exit_flag == "register_suscced": # 
            # 创建一个消息盒子（提示框）
            quitMsgBox = QMessageBox()
            # 设置提示框的标题
            quitMsgBox.setWindowTitle('提示信息')
            # 设置提示框的内容
            quitMsgBox.setText('注册成功')
            # 创建“确定”点击的按钮，修改文本显示内容
            buttonY = QPushButton('确定')
            # 将“确定”按钮加到这个消息盒子中去
            quitMsgBox.addButton(buttonY, QMessageBox.YesRole)
            quitMsgBox.exec_()
            # 判断返回值，如果点击的是确定按钮则接受事件，否则就忽略事件
            # 在这里“确定”和“x”没有区别，都是关闭注册界面，进入登录界面
            if quitMsgBox.clickedButton() == buttonY:
                event.accept()
                mainwindow.exit_flag = "x" 
                mainwindow.show() # 打开注册界面的时候，登陆界面被关闭，因此需要重新打开，注意调用了别的类！
            else:
                event.ignore()
                mainwindow.exit_flag = "x"
                mainwindow.show()
        # 按下注册界面的取消则执行以下内容
        else:
            event.accept()
            mainwindow.exit_flag = "x"
            mainwindow.show()

##############################################################################################################
#       测试界面的类
##############################################################################################################
import datetime
import webbrowser
import os
class ChildWin(QMainWindow, Ui_Dialog):
    """测试界面的类
    
    继承自Ui_Dialog
    """
    def __init__(self):
        """构造函数
        
        加入菜单栏，连接响应时间connnet_event()，开启定时器
        """
        super(ChildWin, self).__init__()
        self.VersionDialog = VersionWin()
        bar=self.menuBar()
        # 向菜单栏中添加新的QMenu对象，父菜单
        helpbar = bar.addMenu('Help')
        helpbar.addAction('Help Document')
        about = helpbar.addMenu('About')
        about.addAction('Version')
        about.addAction('Standard Robots')
        # 单击任何Qmenu对象，都会发射信号，绑定槽函数
        helpbar.triggered[QAction].connect(self.processtrigger)
        self.setupUi(self)
        self.retranslateUi(self)
        self.connect_event()
        self.mytimer()
        
    def processtrigger(self,q):
        """菜单栏响应函数

        点击Version打开版本界面，点击Help Document打开网页版的帮助文档，点击Standard Robots打开斯坦德官网
        """
        #输出那个Qmenu对象被点击
        print(q.text()+'is triggeres')
        mainwindow.ChildDialog.textBrowser.append(q.text()+'被点击')
        if q.text() == "Version":
            self.VersionDialog.show()#打开版本界面
        elif q.text() == "Help Document":
            webbrowser.open('https://www.yuque.com/radarsun/rl2hzg/fiwwni')
        elif q.text() == "Standard Robots":
            webbrowser.open("https://www.standard-robots.com/")
        
    def connect_event(self):
        self.pushButton1.clicked.connect(self.onButton1Click) 
        self.pushButton2.clicked.connect(self.onButton2Click)

    def onButton1Click(self):
        """"生成PDF写入数据库打印二维码"按钮的响应函数

        生成pcb_numb，为封面内容的pcb_data赋值，生成外设统计图，生成PDF，写入数据库，生成并打印二维码，记录过程为txt，重置pcb_data数据
        """
        global pcb_data
        global objPDF
        global default_pcb_data
        _translate = QtCore.QCoreApplication.translate
        
        # 对pcb_numb和date_time赋值
        generate_pcb_numb() 
        #封面内容赋值
        pcb_data[0]['report_code'] = pcb_data[7][1] 
        pcb_data[0]['task_name'] = 'EU200'
        pcb_data[0]['report_date'] = pcb_data[2][1]
        pcb_data[0]['report_creator'] = pcb_data[1][1]
        #生成外设统计图
        uart_loss = [pcb_data[10][1],pcb_data[15][1]]
        uart_error = [pcb_data[11][1],pcb_data[16][1]]
        uart_delay = [pcb_data[12][1],pcb_data[17][1]]
        can_loss = [pcb_data[13][1],pcb_data[18][1]]
        can_error = [pcb_data[14][1],pcb_data[19][1]]
        draw_line_chart(pcb_data[7][1],"UART",uart_loss,uart_error,uart_delay) # 绘制UART统计图
        draw_line_chart(pcb_data[7][1],"CAN",can_loss,can_error) # 绘制CAN统计图
        # 生成PDF
        objPDF.genTaskPDF(pcb_data) 
        self.label11.setText(_translate("Dialog", "已生成PDF,写入数据库，生成二维码，请查看"))
        # 写入数据库
        write_database(pcb_data) 
        # pcb_numb作为编号，生成二维码
        print_barcode(pcb_data[7][1],pcb_data[5][1]) 
        # 将print到textBrowser的内容写入pcb_numb.txt，存入txt文件夹
        try:
            get_text = mainwindow.ChildDialog.textBrowser.toPlainText()
            str_text = str(get_text)
            f = open('./txt/' + pcb_data[7][1] + '.txt', 'w') 
            print(f.write('{}'.format(str_text)))
            f.close()
        except Exception as e:
            print(e)
        # 写入数据一次后重置为默认数据
        pcb_data = default_pcb_data.copy()
        
    def onButton2Click(self):
        """"取消本次测试"按钮的响应函数

        重置pcb_data数据
        """
        global pcb_data
        global default_pcb_data
        pcb_data = default_pcb_data.copy()
        print("重置数据成功")
        mainwindow.ChildDialog.textBrowser.append("重置数据成功")

    def mytimer(self): 
        """100ms定时器

        绑定updata函数
        """
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100) # ms
        
    def update(self):
        """GUI界面的更新函数

        每100ms被调用一次
        """
        global pcb_data
        global objUART # 使用全局变量调用串口实例
        _translate = QtCore.QCoreApplication.translate

        # 扫描枪状态
        if objUART.connect_flag == True:
            self.label2.setText(_translate("Dialog", "已连接"))
            self.label2.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label2.setText(_translate("Dialog", "未连接"))
            self.label2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
         # 控制器版本
        if pcb_data[3][1] != 'None':
            self.label4.setText(_translate("Dialog", pcb_data[3][1]))
            self.label4.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label4.setText(_translate("Dialog", "Null"))
            self.label4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # 测试固件版本
        if pcb_data[4][1] != 'None':
            self.label6.setText(_translate("Dialog", pcb_data[4][1]))
            self.label6.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label6.setText(_translate("Dialog", "Null"))
            self.label6.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # 测试是否通过
        if pcb_data[5][1] != 'None':
            self.label8.setText(_translate("Dialog", pcb_data[5][1]))
            self.label8.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label8.setText(_translate("Dialog", "Null"))
            self.label8.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # 功能固件版本
        if pcb_data[6][1] != 'None':
            self.label10.setText(_translate("Dialog", pcb_data[6][1]))
            self.label10.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label10.setText(_translate("Dialog", "Null"))
            self.label10.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # io_in测试信息
        if pcb_data[8][1] != 'None' and pcb_data[9][1] != "None":
            self.label2_2.setText(_translate("Dialog", pcb_data[8][1]))
            self.label2_2.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label3_2.setText(_translate("Dialog", pcb_data[9][1]))
            self.label3_2.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label4_2.setText(_translate("Dialog", "测试数据"))
            self.label4_2.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label5_2.setText(_translate("Dialog", "测试数据"))
            self.label5_2.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label2_2.setText(_translate("Dialog", "Null"))
            self.label2_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label3_2.setText(_translate("Dialog", "Null"))
            self.label3_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label4_2.setText(_translate("Dialog", "Null"))
            self.label4_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label5_2.setText(_translate("Dialog", "Note:Null"))
            self.label5_2.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # CAN测试信息_丢包率
        if pcb_data[13][1] != (-1) and pcb_data[18][1]!= (-1):
            self.label2_3.setText(_translate("Dialog", "[50K,100K]:[" + str(pcb_data[13][1]) + "," + str(pcb_data[18][1]) + "]%"))
            self.label2_3.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label2_3.setText(_translate("Dialog", "Null"))
            self.label2_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # CAN测试信息_误码率
        if pcb_data[14][1] != (-1) and pcb_data[19][1]!= (-1):
            self.label3_3.setText(_translate("Dialog", "[50K,100K]:[" + str(pcb_data[14][1]) + "," + str(pcb_data[19][1]) + "]%"))
            self.label3_3.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label3_3.setText(_translate("Dialog", "Null"))
            self.label3_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # CAN测试信息_其他两个提示label
        if pcb_data[14][1] != (-1) and pcb_data[19][1]!= (-1) and pcb_data[13][1] != (-1) and pcb_data[18][1]!= (-1):
            self.label4_3.setText(_translate("Dialog", "测试数据"))
            self.label4_3.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label4_3.setText(_translate("Dialog", "Null"))
            self.label4_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        if pcb_data[14][1] != (-1) and pcb_data[19][1]!= (-1) and pcb_data[13][1] != (-1) and pcb_data[18][1]!= (-1):
            self.label5_3.setText(_translate("Dialog", "测试数据"))
            self.label5_3.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label5_3.setText(_translate("Dialog", "Null"))
            self.label5_3.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # UART测试信息_丢包率
        if pcb_data[10][1] != (-1) and pcb_data[15][1] != (-1):
            self.label2_4.setText(_translate("Dialog", "[1152,9600]:[" + str(pcb_data[10][1]) + "," + str(pcb_data[15][1]) + "]%"))
            self.label2_4.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label2_4.setText(_translate("Dialog", "Null"))
            self.label2_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # UART测试信息_误码率
        if pcb_data[11][1] != (-1) and pcb_data[16][1] != (-1):
            self.label3_4.setText(_translate("Dialog", "[1152,9600]:[" + str(pcb_data[11][1]) + "," + str(pcb_data[16][1]) + "]%"))
            self.label3_4.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label3_4.setText(_translate("Dialog", "Null"))
            self.label3_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # UART测试信息_延迟
        if pcb_data[12][1] != (-1) and pcb_data[17][1] != (-1):
            self.label4_4.setText(_translate("Dialog","[1152,9600]:[" + str(pcb_data[12][1]) + "," + str(pcb_data[17][1]) + "]%"))
            self.label4_4.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label4_4.setText(_translate("Dialog", "Null"))
            self.label4_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # UART测试信息_提示label
        if pcb_data[11][1] != (-1) and pcb_data[12][1] != (-1) and pcb_data[13][1] != (-1):
            self.label5_4.setText(_translate("Dialog", "测试数据"))
            self.label5_4.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label5_4.setText(_translate("Dialog", "Null"))
            self.label5_4.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
        # SPI测试信息
        if pcb_data[9][1] != 'None':
            self.label2_5.setText(_translate("Dialog", pcb_data[9][1]))
            self.label2_5.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label3_5.setText(_translate("Dialog", pcb_data[9][1]))
            self.label3_5.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label4_5.setText(_translate("Dialog", "测试数据"))
            self.label4_5.setStyleSheet("color: white;\n"
                "background-color: red;")
            self.label5_5.setText(_translate("Dialog", "测试数据"))
            self.label5_5.setStyleSheet("color: white;\n"
                "background-color: red;")
        else:
            self.label2_5.setText(_translate("Dialog", "Null"))
            self.label2_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label3_5.setText(_translate("Dialog", "Null"))
            self.label3_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label4_5.setText(_translate("Dialog", "Null"))
            self.label4_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")
            self.label5_5.setText(_translate("Dialog", "Note:Null"))
            self.label5_5.setStyleSheet("background-color: rgb(231, 231, 231);\n"
                "color: rgb(4, 4, 4);")

        # 提示界面的信息
        if objUART.connect_flag != True:
            self.label11.setText(_translate("Dialog", "请连接扫码枪"))
        elif (objUART.connect_flag == True) and (pcb_data[3][1] == "None"):
            self.label11.setText(_translate("Dialog", "请扫描控制器的二维码"))
        elif (objUART.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] =="None"):
            self.label11.setText(_translate("Dialog", "请烧写测试固件"))
        elif (objUART.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "None"):
            self.label11.setText(_translate("Dialog", "已烧写测试固件，等待测试结果"))
        elif (objUART.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "False"):
            self.label11.setText(_translate("Dialog", "不合格，请点按钮生成报告"))
        elif ((objUART.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "True") 
             and (pcb_data[6][1] == "None")):
            self.label11.setText(_translate("Dialog", "合格，请烧录功能固件"))
        elif ((objUART.connect_flag == True) and (pcb_data[3][1] != "None") and(pcb_data[4][1] !="None") and (pcb_data[5][1] == "True") 
             and (pcb_data[6][1] != "None")):
            self.label11.setText(_translate("Dialog", "功能固件已烧录，请点按钮生成报告与SN码"))
        else: 
            self.label11.setText(_translate("Dialog", "程序逻辑出错，请联系开发人员"))

        # 将textBrowser显示在底端，保证最新的信息被显示
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        
    def closeEvent(self, event):
        """关闭窗口响应事件

        确认关闭后，将UART和CAN的线程控制位置False，从而结束对应的无限循环线程
        """
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
            uart_thread_destroy_flag = False # 关闭UART
            can_thread_destroy_flag = False # 关闭CAN
            print("关闭GUI的时候关闭串口和CAN")
            mainwindow.ChildDialog.textBrowser.append("关闭GUI的时候关闭串口和CAN")
            event.accept()
        else:
            event.ignore()
            
##############################################################################################################
#       版本界面的类
############################################################################################################## 
class VersionWin(QMainWindow,Ui_version_dialog):
    """版本界面的类

    显示斯坦德LOGO，版本信息，开发人员信息
    """
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
    pcb_data = [ # 测试的数据
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},# 在测试界面类的onButton1Click中赋值
        ['admin_name','None'], # 在is_admin中赋值，登录时
        ['date_time','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['pcb_version','None'], # 在runuart中赋值，扫码时
        ['test_firmwave_version','V0.0.1'],
        ['qualified_or_not','True'],
        ['func_firmwave_version','V0.0.1'],
        ['pcb_numb','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['io_din','1101'],
        ['io_dout','0001'],
        ['uart115200_packet_loss_rate',10],
        ['uart115200_error_rate',20],
        ['uart115200_delay_time',100],
        ['can50k_packet_loss_rate',35],
        ['can50k_error_rate',45],
        ['uart9600_packet_loss_rate',20],
        ['uart9600_error_rate',10],
        ['uart9600_delay_time',200],
        ['can100k_packet_loss_rate',45],
        ['can100k_error_rate',35]
    ]
     
    default_pcb_data = [ # 默认的数据，重置数据时候使用
        {'report_code': 'None', 
         'task_name':'None',
         'report_date':'None',
         'report_creator':'None'},
        ['admin_name','None'], # 在is_admin中赋值，登录时
        ['date_time','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['pcb_version','None'], # 在runuart中赋值，扫码时
        ['test_firmwave_version','None'],
        ['qualified_or_not','None'],
        ['func_firmwave_version','None'],
        ['pcb_numb','None'], # 在generate_pcb_nub中赋值，最后按下生成PDF按钮时
        ['io_din','None'],
        ['io_dout','None'],
        ['uart115200_packet_loss_rate',-1],
        ['uart115200_error_rate',-1],
        ['uart115200_delay_time',-1],
        ['can50k_packet_loss_rate',-1],
        ['can50k_error_rate',-1],
        ['uart9600_packet_loss_rate',-1],
        ['uart9600_error_rate',-1],
        ['uart9600_delay_time',-1],
        ['can100k_packet_loss_rate',-1],
        ['can100k_error_rate',-1]
    ]
    # lock = threading.lock()
    
    app = QApplication(sys.argv) 
    mainwindow = MainWindow()

    objPDF = PDFGenerator()#生成PDF实例，规定PDF格式

    objUART = DriveUART()#生成串口实例
    objUART.connect_uart()

    objPCAN = DriveCAN()#CAN实例
    objPCAN.can_init()
    objPCAN.can_filter()

    uart_thread = threading.Thread(target=runuart)
    uart_thread.start()
    
    can_thread = threading.Thread(target=runcan)#非守护线程
    can_thread.start()

    mainwindow.show()
    sys.exit(app.exec_())
    
# 要从ui文件生成py文件，使用命令：pyuic5 -o C:\Users\liuya\Desktop\SR_work\miangui.py C:\Users\liuya\Desktop\SR_work\miangui.ui