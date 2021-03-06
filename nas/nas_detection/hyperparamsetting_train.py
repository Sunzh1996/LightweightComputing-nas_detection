import sys, os, time
from PyQt5.QtCore import Qt, QUrl, QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QMainWindow, QSlider, QLabel, QMessageBox, QFileDialog,
                             QHBoxLayout, QPushButton, QApplication, QLineEdit, QDialog)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from collections import OrderedDict

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../'))
from qtui.hyperparamsetting_train_ui import *
from tools.utils import *
import numpy as np


# 训练超参输入界面
class Hyperparamesetting_train_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_11.clicked.connect(self.select_path)
        self.ui.pushButton_12.clicked.connect(self.ok)
        self.ui.pushButton_13.clicked.connect(self.reset)
        self.ui.pushButton_14.clicked.connect(self.quit)

    def select_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹", "./")
        self.ui.lineEdit_16.setText(path)

    def ok(self):
        valid, info = self.valid_check()
        if valid:
            self.accept()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Alert", info)
            msg_box.exec_()

    def reset(self):
        self.ui.lineEdit_11.setText("12")
        self.ui.lineEdit_12.setText("SGD")
        self.ui.lineEdit_13.setText("0.05")
        self.ui.lineEdit_14.setText("0.9")
        self.ui.lineEdit_15.setText("0.00005")
        self.ui.lineEdit_16.clear()


    def quit(self):
        self.reject()

    def get_data(self):
        data = []
        data.append('Total epochs：' + self.ui.lineEdit_11.text())
        data.append('weight_optimizer：' + self.ui.lineEdit_12.text())
        data.append('weight_optimizer lr：' + self.ui.lineEdit_13.text())
        data.append('weight_optimizer momentum：' + self.ui.lineEdit_14.text())
        data.append('weight_optimizer weight_decay：' + self.ui.lineEdit_15.text())
        data.append('output path：' + self.ui.lineEdit_16.text())
        return data

    def valid_check(self):
        def is_float(data):
            try:
                float(data)
            except ValueError:
                return False
            return True

        def is_int(data):
            try:
                int(data)
            except ValueError:
                return False
            return True

        def is_in(data, minn=None, maxx=None, min_bound=True, max_bound=True):
            if minn is not None:
                if data < minn or (not min_bound and data == minn):
                    return False
            if maxx is not None:
                if data > maxx or (not max_bound and data == maxx):
                    return False
            return True

        def is_path(path):
            return os.path.exists(path)

        data = OrderedDict()
        data['Total epochs'] = self.ui.lineEdit_11.text()
        data['weight_optimizer'] = self.ui.lineEdit_12.text()
        data['weight_optimizer lr'] = self.ui.lineEdit_13.text()
        data['weight_optimizer momentum'] = self.ui.lineEdit_14.text()
        data['weight_optimizer weight_decay'] = self.ui.lineEdit_15.text()
        data['output path'] = self.ui.lineEdit_16.text()
        for key in data:
            if key in ['Total epochs']:
                if not is_int(data[key]):
                    return False, '{}应输入整数'.format(key)
                if not is_in(int(data[key]), 0., min_bound=False):
                    return False, '{}应大于0'.format(key)
            if key in ['weight_optimizer']:
                if data[key] != 'SGD' and data[key] != 'Adam':
                    return False, '{}应输入SGD or Adam'.format(key)

            if key in ['weight_optimizer lr', 'weight_optimizer momentum', 'weight_optimizer weight_decay']:
                if not is_float(data[key]):
                    return False, '{}应输入实数'.format(key)
                if not is_in(float(data[key]), 0., min_bound=False):
                    return False, '{}应大于0'.format(key)
            if key in ['output path']:
                if not is_path(data[key]):
                    return False, '{}路径不存在'.format(key)
        return True, 'ok'