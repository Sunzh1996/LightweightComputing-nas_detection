# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nas.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1355, 825)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_12.addItem(spacerItem)
        self.pushButton_start = QtWidgets.QPushButton(self.widget)
        self.pushButton_start.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_12.addWidget(self.pushButton_start)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_12.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout_12, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_2.addWidget(self.comboBox_8, 4, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "FNA")
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_2.addWidget(self.comboBox_5, 3, 1, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_2.addWidget(self.comboBox_6, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "coco2017")
        self.gridLayout_2.addWidget(self.comboBox_4, 2, 2, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_2.addWidget(self.comboBox_7, 4, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 4, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_2)
        self.gridLayout_3.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_14.addWidget(self.tableWidget)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.widget)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 523, 328))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.scrollArea_7 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 1057, 330))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_6)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout.addWidget(self.scrollArea_7, 1, 0, 1, 2)
        self.comboBox_9 = QtWidgets.QComboBox(self.tab)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout.addWidget(self.comboBox_9, 2, 0, 1, 1)
        self.pushButton_modelcheck = QtWidgets.QPushButton(self.tab)
        self.pushButton_modelcheck.setObjectName("pushButton_modelcheck")
        self.gridLayout.addWidget(self.pushButton_modelcheck, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_5.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.scrollArea_9 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_9.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 23, 16))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_5.addWidget(self.scrollArea_9, 0, 1, 2, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_5.addWidget(self.textBrowser_2, 1, 0, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setEnabled(True)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 80, 16))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.addWidget(self.scrollArea_3, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1057, 701))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 515, 629))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_4)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout.addWidget(self.graphicsView_2)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.addWidget(self.scrollArea_4, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 514, 629))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents_5)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_5.addWidget(self.graphicsView_3)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_4.addWidget(self.scrollArea_5, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 67, 16))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_2.addWidget(self.scrollArea_6)
        self.pushButton_vis = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_vis.setObjectName("pushButton_vis")
        self.verticalLayout_2.addWidget(self.pushButton_vis)
        self.tabWidget.addTab(self.tab_6, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1355, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.groupBox_7.setTitle(_translate("MainWindow", "输入"))
        self.checkBox.setText(_translate("MainWindow", "分类"))
        self.label_2.setText(_translate("MainWindow", "模型"))
        self.label_3.setText(_translate("MainWindow", "数据"))
        self.checkBox_3.setText(_translate("MainWindow", "分割"))
        self.checkBox_2.setText(_translate("MainWindow", "检测"))
        self.checkBox_4.setText(_translate("MainWindow", "多任务"))
        self.groupBox.setTitle(_translate("MainWindow", "模型性能对比"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "精度对比"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "资源消耗"))
        self.pushButton_2.setText(_translate("MainWindow", "超参数设置"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">total_epochs = 14</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">image_size = (800, 1088)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">weight_optimizer：SGD, lr=0.02, momentum=0.9, weight_decay=0.0001</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">arch_optimizer：Adam, lr=0.0003, weight_decay=0.001</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "model_epoch1"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "model_epoch2"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "model_epoch3"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "model_epoch4"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "model_epoch5"))
        self.comboBox_9.setItemText(5, _translate("MainWindow", "model_epoch6"))
        self.comboBox_9.setItemText(6, _translate("MainWindow", "model_epoch7"))
        self.comboBox_9.setItemText(7, _translate("MainWindow", "model_epoch8"))
        self.comboBox_9.setItemText(8, _translate("MainWindow", "model_epoch9"))
        self.comboBox_9.setItemText(9, _translate("MainWindow", "model_epoch10"))
        self.comboBox_9.setItemText(10, _translate("MainWindow", "model_epoch11"))
        self.comboBox_9.setItemText(11, _translate("MainWindow", "model_epoch12"))
        self.comboBox_9.setItemText(12, _translate("MainWindow", "model_epoch13"))
        self.comboBox_9.setItemText(13, _translate("MainWindow", "model_epoch14"))
        self.pushButton_modelcheck.setText(_translate("MainWindow", "model_check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "搜索可视化"))
        self.pushButton_3.setText(_translate("MainWindow", "超参数设置"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">total_epochs = 12</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">image_size = (800, 1088)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">optimizer：SGD, lr=0.05, momentum=0.9, weight_decay=0.00005</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "训练可视化"))
        self.label.setText(_translate("MainWindow", "输入图片"))
        self.label_4.setText(_translate("MainWindow", "检测结果"))
        self.label_5.setText(_translate("MainWindow", "The image infer time is"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "推断可视化"))
        self.pushButton_vis.setText(_translate("MainWindow", "模型可视化"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "模型可视化"))

