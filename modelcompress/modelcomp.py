import sys,os,time
from PyQt5.QtCore import Qt, QUrl, QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QMainWindow, QSlider, QLabel, 
                             QHBoxLayout, QPushButton, QApplication, QLineEdit, QDialog)
from PyQt5.QtWebEngineWidgets import QWebEngineView

sys.path.append("../")
from qtui.modelcomp_ui import  *
from tools.utils import *

import numpy as np

rootPath = os.path.abspath(os.path.dirname(os.getcwd()))
htmlFolder = os.path.join(rootPath ,"html","modelcompress")

#用于数据交互的全局变量
counter = 0
uiData = 0

#任务线程
class MyTask(QThread):
    signalUpdateUi =pyqtSignal() #定义更新UI信号
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            global counter
            global uiData

            self.sleep(1)

            counter += 1
            uiData = np.random.randint(20,40)

            if counter > 100: #处理完成，退出线程 
                break
            
            self.signalUpdateUi.emit() #在需要更新Ui的时候发送

#主界面
class MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(MainWindow, self).__init__(parent=parent, flags=flags)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_start.clicked.connect(self.startBtnCallback)

        self.lossLineHtml = QWebEngineView()
        self.ui.scrollArea.setWidget(self.lossLineHtml)
        htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "linetemplate.html"))
        self.lossLineHtml.load(QUrl(convertPath(htmlFilename)))


        self.resPieHtml = QWebEngineView()
        self.ui.scrollArea_4.setWidget(self.resPieHtml)
        htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "pietemplate.html"))
        self.resPieHtml.load(QUrl(convertPath(htmlFilename)))


        self.resLineHtml = QWebEngineView()
        self.ui.scrollArea_3.setWidget(self.resLineHtml)
        htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "resline.html"))
        self.resLineHtml.load(QUrl(convertPath(htmlFilename)))

        self.resBarHtml = QWebEngineView()
        self.ui.scrollArea_8.setWidget(self.resBarHtml)
        htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "resbar.html"))
        self.resBarHtml.load(QUrl(convertPath(htmlFilename)))

        self.htmlLoadFinished = False #指示是否已经创建Echarts

        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(100)

        # self.ui.leftFrame.setFixedWidth(200)

        self.myTask = MyTask()
        self.myTask.signalUpdateUi.connect(self.updateUiCallback) #关联数据处理线程和可视化线程
        
        self.show() #QMainWindow必须调用该函数，但QDialog不用

    #开始按钮回调函数
    def startBtnCallback(self):

        self.buildChart(self.resLineHtml, self.ui.scrollArea_3)
        self.buildChart(self.resPieHtml, self.ui.scrollArea_4)
        self.buildChart(self.lossLineHtml, self.ui.scrollArea)
        self.buildChart(self.resBarHtml, self.ui.scrollArea_8)

        self.htmlLoadFinished = True

        #开启数据处理线程
        self.myTask.start()


    def buildChart(self, htmlViewer, container):
        htmlViewer.page().runJavaScript(
            "buildChart('{}', '{}'); ".
                format(int(container.width()), int(container.height()))           
        )

    def resizeEvent(self, a0):
        if self.htmlLoadFinished:
            self.buildChart(self.resLineHtml, self.ui.scrollArea_3)
            self.buildChart(self.resPieHtml, self.ui.scrollArea_4)
            self.buildChart(self.lossLineHtml, self.ui.scrollArea)
            self.buildChart(self.resBarHtml, self.ui.scrollArea_8)      

        return super().resizeEvent(a0)

    def updateUiCallback(self):

        global counter
        global uiData

        xValue = counter
        yValue = uiData

        # 动态更新方式，每次传输单个数据
        self.lossLineHtml.page().runJavaScript(
            '''
                index_data.push({})
                loss_data.push({})
            '''.format(xValue, yValue)
        )

        #一次更新多个数据
        ids = [i for i in range(0,300)]
        vals = [np.random.randint(0,40) for i in range(0,300)]
        self.resLineHtml.page().runJavaScript(
            '''
                index_data={}
                loss_data={}
            '''.format(ids, vals)
        )

        self.ui.progressBar.setValue(xValue) #更新progressBar

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainW = MainWindow()

    sys.exit(app.exec_())