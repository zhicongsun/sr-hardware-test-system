# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\liuya\Desktop\SR_work\register.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#最新
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

import qtdesigner_rc
