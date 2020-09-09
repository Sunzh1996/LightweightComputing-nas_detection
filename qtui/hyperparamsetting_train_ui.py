# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hyperparamsetting_train.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 405)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(90, 60, 111, 20))
        self.label_12.setObjectName("label_12")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(280, 60, 171, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(280, 100, 171, 21))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(90, 100, 111, 20))
        self.label_13.setObjectName("label_13")
        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(280, 140, 171, 21))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(90, 140, 141, 20))
        self.label_14.setObjectName("label_14")
        self.lineEdit_14 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(280, 180, 171, 21))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(90, 180, 161, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(280, 220, 171, 21))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(90, 260, 111, 20))
        self.label_16.setObjectName("label_16")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(470, 260, 81, 21))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 330, 121, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(230, 330, 121, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(410, 330, 121, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(90, 220, 191, 20))
        self.label_17.setObjectName("label_17")
        self.lineEdit_16 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(280, 260, 171, 21))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "超参数设置"))
        self.label_11.setText(_translate("Dialog", "请输入超参数："))
        self.label_12.setText(_translate("Dialog", "total epochs："))
        self.label_13.setText(_translate("Dialog", "weight_optimizer"))
        self.label_14.setText(_translate("Dialog", "weight_optimizer lr："))
        self.label_15.setText(_translate("Dialog", "weight_optimizer momentum："))
        self.label_16.setText(_translate("Dialog", "output path："))
        self.pushButton_11.setText(_translate("Dialog", "选择"))
        self.pushButton_12.setText(_translate("Dialog", "确定"))
        self.pushButton_13.setText(_translate("Dialog", "重置"))
        self.pushButton_14.setText(_translate("Dialog", "退出"))
        self.label_17.setText(_translate("Dialog", "weight_optimizer weight_decay ："))

