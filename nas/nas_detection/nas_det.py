import sys,os,time, random
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl, QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QMainWindow, QSlider, QLabel, 
                             QHBoxLayout, QPushButton, QApplication, QLineEdit, QDialog,
                             QMessageBox, QGraphicsPixmapItem, QGraphicsScene)
from PyQt5.QtWebEngineWidgets import QWebEngineView

sys.path.append("../")
print(sys.path)
from qtui.nas_ui import  *
from tools.utils import *
from nas_model_vis import plot_model
from hyperparamsetting_search import Hyperparamesetting_search_Window
from hyperparamsetting_train import Hyperparamesetting_train_Window
from quiver_engine import server
from quiver_engine.model_utils import register_hook
import threading
import numpy as np
from torchvision import models

import os.path as osp
sys.path.append(osp.join(sys.path[0], '..'))
import mmcv
import models
from mmdet.models import build_detector, detectors


rootPath = os.path.abspath(os.path.dirname(os.getcwd()))
htmlFolder = os.path.join(rootPath ,"../html","nas")
print(rootPath)
#用于数据交互的全局变量
counter = 0
uiData = 0

#model_choice = ['k3_e1', 'k3_e3', 'k3_e6', 'k5_e3', 'k5_e6', 'k7_e3', 'k7_e6']
model_search=[['k3_e1',
        'k5_e6', 'skip', 'skip', 'k3_e3',
        'k7_e6', 'skip', 'k3_e6', 'k3_e6',
        'k7_e6', 'k7_e6', 'k5_e6', 'k3_e6',
        'k5_e6', 'skip', 'skip', 'k5_e3',
        'k5_e3', 'k7_e6', 'k7_e6', 'k7_e6',
        'k7_e6'],
       ['k3_e1',
        'k3_e3', 'k3_e6', 'skip', 'skip',
        'k5_e3', 'k3_e3', 'k5_e3', 'k7_e3',
        'k3_e6', 'k3_e6', 'skip', 'k3_e3',
        'k5_e3', 'k3_e6', 'k7_e6', 'k3_e3',
        'k3_e3', 'k5_e6', 'k3_e6', 'k5_e3',
        'k5_e6'],
      ['k3_e1',
        'k3_e3', 'k3_e6', 'skip', 'skip',
        'k5_e3', 'k3_e3', 'k5_e3', 'k7_e3',
        'k3_e6', 'k3_e6', 'skip', 'k3_e3',
        'k5_e3', 'k3_e6', 'k7_e6', 'k3_e3',
        'k3_e3', 'k5_e6', 'k3_e6', 'k5_e3',
        'k5_e6'],
      ['k3_e1',
        'k3_e3', 'k3_e6', 'skip', 'skip',
        'k5_e3', 'k3_e3', 'k5_e3', 'k7_e3',
        'k3_e6', 'k3_e6', 'skip', 'k3_e3',
        'k5_e3', 'k3_e6', 'k7_e6', 'k3_e3',
        'k3_e3', 'k5_e6', 'k3_e6', 'k5_e3',
        'k5_e6'],
      ['k3_e1',
        'k3_e3', 'k3_e6', 'skip', 'skip',
        'k5_e3', 'k3_e3', 'k5_e3', 'k7_e3',
        'k3_e6', 'k3_e6', 'skip', 'k3_e3',
        'k5_e3', 'k3_e6', 'k7_e6', 'k3_e3',
        'k3_e3', 'k5_e6', 'k3_e6', 'k5_e3',
        'k5_e6'],
      ['k3_e1',
        'k3_e3', 'k3_e6', 'skip', 'skip',
        'k5_e3', 'k3_e3', 'k5_e3', 'k7_e3',
        'k3_e6', 'k3_e6', 'skip', 'k3_e3',
        'k5_e3', 'k3_e6', 'k7_e6', 'k3_e3',
        'k3_e3', 'k5_e6', 'k3_e6', 'k5_e3',
       'k5_e6'],
      ['k3_e1',
        'k3_e3', 'k3_e6', 'skip', 'skip',
        'k5_e3', 'k3_e3', 'k5_e3', 'k7_e3',
        'k3_e6', 'k3_e6', 'skip', 'k3_e3',
        'k5_e3', 'k3_e6', 'k7_e6', 'k3_e3',
        'k3_e3', 'k5_e6', 'k3_e6', 'k5_e3',
       'k5_e6'],
      ['k3_e1',
        'k5_e6', 'k3_e6', 'skip', 'skip',
        'k5_e3', 'skip', 'k5_e3', 'k7_e3',
        'k5_e6', 'k3_e6', 'skip', 'k5_e3',
        'k5_e3', 'skip', 'k7_e3', 'k3_e3',
        'k3_e3', 'k7_e6', 'k3_e6', 'k5_e3',
        'k5_e6'],
      ['k3_e1',
        'k5_e6', 'skip', 'skip', 'k3_e3',
        'k7_e6', 'skip', 'skip', 'k3_e6',
        'k7_e6', 'k5_e6', 'k7_e6', 'k7_e6',
        'k3_e6', 'skip', 'k7_e6', 'skip',
        'k3_e6', 'skip', 'k7_e6', 'k7_e6',
        'k7_e6'],
      ['k3_e1',
        'k5_e6', 'skip', 'skip', 'k3_e6',
        'k7_e6', 'skip', 'skip', 'k3_e6',
        'k7_e6', 'k5_e6', 'k7_e6', 'k3_e6',
        'k3_e6', 'skip', 'skip', 'skip',
        'k7_e6', 'k7_e6', 'k7_e6', 'k7_e3',
        'k7_e6'],
      ['k3_e1',
        'k5_e6', 'skip', 'skip', 'k3_e6',
        'k7_e6', 'skip', 'skip', 'k5_e6',
        'k7_e6', 'k7_e6', 'k7_e6', 'k3_e6',
        'k3_e6', 'skip', 'skip', 'k5_e3',
        'k5_e6', 'k7_e6', 'k7_e6', 'k7_e6',
        'k7_e6'],
      ['k3_e1',
        'k5_e6', 'skip', 'skip', 'k3_e6',
        'k7_e6', 'skip', 'k3_e6', 'k5_e6',
        'k7_e6', 'k5_e6', 'k3_e6', 'k3_e6',
        'k3_e6', 'skip', 'skip', 'k5_e3',
        'k5_e6', 'k7_e6', 'k7_e6', 'k7_e6',
        'k7_e6'],
      ['k3_e1',
        'k5_e6', 'skip', 'skip', 'k3_e6',
        'k7_e6', 'skip', 'k5_e6', 'k5_e6',
        'k7_e6', 'k7_e6', 'k3_e6', 'k3_e6',
        'k3_e6', 'skip', 'skip', 'k5_e3',
        'k5_e6', 'k7_e6', 'k7_e6', 'k7_e6',
        'k7_e6'],
      ['k3_e1',
        'k5_e6', 'skip', 'skip', 'k3_e3',
        'k7_e6', 'skip', 'k3_e6', 'k3_e6',
        'k7_e6', 'k7_e6', 'k5_e6', 'k3_e6',
        'k5_e6', 'skip', 'skip', 'k5_e3',
        'k5_e3', 'k7_e6', 'k7_e6', 'k7_e6',
        'k7_e6']
    ]
searchloss_cls_list=[0.8169, 0.7239, 0.6695, 0.6271, 0.6031, 0.5830, 0.5640, 0.5612, 0.4516, 0.4398, 0.4404, 0.4351, 0.4353, 0.4272]
searchloss_reg_list=[0.3439, 0.3044, 0.2833, 0.2699, 0.2584, 0.2548, 0.2473, 0.2467, 0.2059, 0.1989, 0.1997, 0.1964, 0.2001, 0.1928]
searchloss_total_list=[1.1609, 1.0283, 0.9529, 0.8970, 0.8615, 0.8377, 0.8113, 0.8079, 0.6575, 0.6387, 0.6401, 0.6314, 0.6353, 0.6199]

trainloss_cls_list=[0.4608, 0.3960, 0.3748, 0.3514, 0.3462, 0.3373, 0.3242, 0.3250, 0.2717, 0.2553, 0.2563, 0.2525]
trainloss_reg_list=[0.227, 0.2039, 0.1944, 0.1881, 0.1818, 0.1790, 0.1699, 0.1712, 0.1547, 0.1397, 0.1462, 0.1375]
trainloss_total_list=[0.6878, 0.5999, 0.5692, 0.5395, 0.5281, 0.5163, 0.4942, 0.4962, 0.4264, 0.3950, 0.4025, 0.3900]

acc_mAP_list=['0.117', '0.186', '0.209', '0.225', '0.245', '0.254', '0.257', '0.261', '0.322', '0.327', '0.331', '0.334']

infertime_list = [0.5671, 0.8545, 0.9193, 1.1581, 0.9614, 0.9224, 1.2183, 1.3629, 0.9755, 1.0109, 0.9835, 1.3884, 1.1824, 0.9641]


config_file = './fna_retinanet_fpn_retrain.py'
cfg = mmcv.Config.fromfile(config_file)
cfg.model.pretrained = None
model = build_detector(cfg.model, train_cfg=None, test_cfg=cfg.test_cfg)
class modelVisTask(QThread):
    signalUpdateUi = pyqtSignal()  # 定义更新UI信号

    def __init__(self, mainW):
        super().__init__()
        self.signalUpdateUi.connect(mainW.modelVisLoad)
        self.sign = True

        #self.model = models.resnet18()
        self.model = model

        self.hook_list = register_hook(self.model)

    def stop(self):
        self.http_server.stop()

    def run(self):
        thread = threading.Thread(target=self.load)
        thread.start()
        self.http_server = server.get_server(
            self.model,
            self.hook_list,
            os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'Cat'),
        )
        self.http_server.serve_forever()

    def load(self):
        self.signalUpdateUi.emit()
        time.sleep(3)
        self.signalUpdateUi.emit()


#任务线程
class MyTask(QThread):
    signalUpdateUi =pyqtSignal() #定义更新UI信号
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            global counter
            global uiData
            global searchloss_cls
            global searchloss_reg
            global searchloss_total
            global trainloss_cls
            global trainloss_reg
            global trainloss_total
            global acc_mAP
            global infertime

            self.sleep(1)

            #if counter % 1 == 0:
            if counter < 14:
                #model = [model_choice[random.randint(0, 3)] for _ in range(20)]
                model=model_search[counter]
                model_name = 'model_epoch{}'.format(counter+1)
                plot_model(model, model_name=model_name)

                searchloss_cls=searchloss_cls_list[counter]
                searchloss_reg=searchloss_reg_list[counter]
                searchloss_total=searchloss_total_list[counter]
                infertime=infertime_list[counter]

                if counter < 12:
                    trainloss_cls=trainloss_cls_list[counter]
                    trainloss_reg=trainloss_reg_list[counter]
                    trainloss_total=trainloss_total_list[counter]

                    acc_mAP = acc_mAP_list[counter]

                counter += 1

            #if counter > 100: #处理完成，退出线程
            else:
                break

            uiData = np.random.randint(20,40)

            self.signalUpdateUi.emit() #在需要更新Ui的时候发送

#主界面
class MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(MainWindow, self).__init__(parent=parent, flags=flags)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_start.clicked.connect(self.startBtnCallback)

        self.ui.pushButton_modelcheck.clicked.connect(self.model_check)

        self.ui.pushButton_2.clicked.connect(self.hyperparamsetting_search)
        self.ui.pushButton_3.clicked.connect(self.hyperparamsetting_train)

        self.ui.pushButton_vis.clicked.connect(self.modelVisBtnCallback)

        ###############  model Vis  ###############
        self.modelVisHtml = QWebEngineView()
        self.ui.scrollArea_6.setWidget(self.modelVisHtml)
        self.modelVishtmlFilename = "http://localhost:5000"

        self.searchLossHtml = QWebEngineView()
        self.ui.scrollArea.setWidget(self.searchLossHtml)
        htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "search_loss.html"))
        self.searchLossHtml.load(QUrl(convertPath(htmlFilename)))

        # self.resPieHtml = QWebEngineView()
        # self.ui.scrollArea_4.setWidget(self.resPieHtml)
        # htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "pietemplate.html"))
        # self.resPieHtml.load(QUrl(convertPath(htmlFilename)))

        self.trainLossHtml = QWebEngineView()
        self.ui.scrollArea_9.setWidget(self.trainLossHtml)
        htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "train_loss.html"))
        self.trainLossHtml.load(QUrl(convertPath(htmlFilename)))

        self.trainAccHtml = QWebEngineView()
        self.ui.scrollArea_3.setWidget(self.trainAccHtml)
        htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "train_acc.html"))
        self.trainAccHtml.load(QUrl(convertPath(htmlFilename)))

        # self.resBarHtml = QWebEngineView()
        # self.ui.scrollArea_8.setWidget(self.resBarHtml)
        # htmlFilename = "file:///{}".format(os.path.join(htmlFolder, "resbar.html"))
        # self.resBarHtml.load(QUrl(convertPath(htmlFilename)))

        self.htmlLoadFinished = False #指示是否已经创建Echarts

        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(100)

        # self.ui.leftFrame.setFixedWidth(200)
        self.ui.tabWidget.tabBarClicked.connect(self.tabWidgetClickedCallback)

        self.modelVisTask = None
        self.myTask = MyTask()
        self.myTask.signalUpdateUi.connect(self.updateUiCallback) #关联数据处理线程和可视化线程
        
        self.show() #QMainWindow必须调用该函数，但QDialog不用

    def tabWidgetClickedCallback(self, index):
        self.resizeEvent(None)

    def model_check(self):
        # model
        #self.modelLabel = QLabel(self)
        #modelImg = QPixmap("figure/{}.jpg".format(self.ui.comboBox_9.currentText()))
        #modelImg = QPixmap.scaled(modelImg,1000,250)
        #self.modelLabel.setPixmap(modelImg)
        #self.ui.scrollArea_7.setWidget(self.modelLabel)
        self.inputImgShow = QPixmap()
        self.inputImgShow.load("figure/{}.jpg".format(self.ui.comboBox_9.currentText()))
        self.inputImgShowItem = QGraphicsPixmapItem()
        self.inputImgShowItem.setPixmap(QPixmap(self.inputImgShow))
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.inputImgShowItem)
        self.ui.graphicsView.setScene(self.scene)  # 将场景添加至视图
        self.ui.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.inputImgShow)))  # 图像自适应大小

    def hyperparamsetting_search(self):
        dialog = Hyperparamesetting_search_Window()
        if dialog.exec_():
            data = dialog.get_data()
            #self.ui.textBrowser.setText(data)
            datastr = ''
            for d in data:
                datastr += d + '\n'
            self.ui.textBrowser.setText(datastr)
            self.path = data[-1]
        #self.ui.textBrowser.setReadOnly(False)

    def hyperparamsetting_train(self):
        #self.ui.textBrowser_2.setReadOnly(False)
        dialog = Hyperparamesetting_train_Window()
        if dialog.exec_():
            data = dialog.get_data()
            #self.ui.textBrowser.setText(data)
            datastr = ''
            for d in data:
                datastr += d + '\n'
            self.ui.textBrowser_2.setText(datastr)

    #开始按钮回调函数
    def startBtnCallback(self):

        self.buildChart(self.searchLossHtml, self.ui.scrollArea)
        # self.buildChart(self.resPieHtml, self.ui.scrollArea_4)
        self.buildChart(self.trainLossHtml, self.ui.scrollArea_9)
        self.buildChart(self.trainAccHtml, self.ui.scrollArea_3)
        # self.buildChart(self.resBarHtml, self.ui.scrollArea_8)
        self.buildChart(self.modelVisHtml, self.ui.scrollArea_6)


        self.htmlLoadFinished = True

        #开启数据处理线程
        self.myTask.start()

    def modelVisBtnCallback(self):
        if self.modelVisTask is not None:
            self.modelVisTask.stop()
            self.modelVisTask.exit()
            del self.modelVisTask
        #dataset = self.ui.comboBox.currentText()
        #model = self.ui.comboBox_2.currentText()
        self.modelVisTask = modelVisTask(self)
        self.modelVisTask.start()

    def modelVisLoad(self):
        self.modelVisHtml.load(QUrl(convertPath(self.modelVishtmlFilename)))

    def buildChart(self, htmlViewer, container):
        htmlViewer.page().runJavaScript(
            "buildChart('{}', '{}'); ".
                format(int(container.width()), int(container.height()))           
        )

    def resizeEvent(self, a0):
        num = self.ui.tabWidget.count()
        cur_indx = self.ui.tabWidget.currentIndex()
        for i in range(num):
            self.ui.tabWidget.setCurrentIndex(i)
        self.ui.tabWidget.setCurrentIndex(cur_indx)

        if self.htmlLoadFinished:
            self.buildChart(self.searchLossHtml, self.ui.scrollArea)
            # self.buildChart(self.resPieHtml, self.ui.scrollArea_4)
            self.buildChart(self.trainLossHtml, self.ui.scrollArea_9)
            self.buildChart(self.trainAccHtml, self.ui.scrollArea_3)
            # self.buildChart(self.resBarHtml, self.ui.scrollArea_8)
            self.buildChart(self.modelVisHtml, self.ui.scrollArea_6)


        return super().resizeEvent(a0)

    def updateUiCallback(self):

        global counter
        global uiData

        xValue = counter
        yValue = uiData

        # model可视化
        #self.modelLabel = QLabel(self)
        #modelImg = QPixmap("figure/model_epoch{}.png".format(counter))
        #print(QPixmap.size(modelImg))
        #modelImg = QPixmap.scaled(modelImg,1000,250)
        #print(QPixmap.size(modelImg))
        #self.modelLabel.setPixmap(modelImg)
        #self.ui.scrollArea_7.setWidget(self.modelLabel)

        self.inputImgShow = QPixmap()
        self.inputImgShow.load("figure/model_epoch{}.jpg".format(counter))
        self.inputImgShowItem = QGraphicsPixmapItem()
        self.inputImgShowItem.setPixmap(QPixmap(self.inputImgShow))
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.inputImgShowItem)
        self.ui.graphicsView.setScene(self.scene)  # 将场景添加至视图
        self.ui.graphicsView.fitInView(QGraphicsPixmapItem(QPixmap(self.inputImgShow)))  # 图像自适应大小

        #推断原始图片
        self.inputImgShow = QPixmap()
        self.inputImgShow.load("imgs_test/imgs_raw/{}.jpg".format(counter))
        self.inputImgShowItem = QGraphicsPixmapItem()
        self.inputImgShowItem.setPixmap(QPixmap(self.inputImgShow))
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.inputImgShowItem)
        self.ui.graphicsView_2.setScene(self.scene)  # 将场景添加至视图
        self.ui.graphicsView_2.fitInView(QGraphicsPixmapItem(QPixmap(self.inputImgShow)))  # 图像自适应大小

        # 推断输出检测图片bbox
        self.inputImgShow = QPixmap()
        self.inputImgShow.load("imgs_test/imgs_bbox/{}.jpg".format(counter))
        self.inputImgShowItem = QGraphicsPixmapItem()
        self.inputImgShowItem.setPixmap(QPixmap(self.inputImgShow))
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.inputImgShowItem)
        self.ui.graphicsView_3.setScene(self.scene)  # 将场景添加至视图
        self.ui.graphicsView_3.fitInView(QGraphicsPixmapItem(QPixmap(self.inputImgShow)))  # 图像自适应大小

        #推断时间
        self.ui.label_5.setText('The image infer time is {}s'.format(infertime))

        # 动态更新方式，每次传输单个数据
        self.searchLossHtml.page().runJavaScript(
                '''
                index_data.push({})
                searchloss_cls.push({})
                searchloss_reg.push({})
                searchloss_total.push({})
                '''
                .format(xValue, searchloss_cls,searchloss_reg,searchloss_total)
        )
        if xValue < 13:
            self.trainLossHtml.page().runJavaScript(
                    '''
                    index_data.push({})
                    trainloss_cls.push({})
                    trainloss_reg.push({})
                    trainloss_total.push({})
                    '''
                    .format(xValue, trainloss_cls,trainloss_reg,trainloss_total)
            )
            self.trainAccHtml.page().runJavaScript(
                    '''
                    index_data.push({})
                    acc_mAP.push({})
                    '''
                    .format(xValue, acc_mAP)
            )

        """
        #一次更新多个数据
        ids = [i for i in range(0,300)]
        vals = [np.random.randint(0,40) for i in range(0,300)]
        self.resLineHtml.page().runJavaScript(
            '''
                index_data={}
                loss_data={}
            '''.format(ids, vals)
        )
        """
        self.ui.progressBar.setValue(xValue) #更新progressBar

        if self.ui.progressBar.value() >= 14:
            if hasattr(self, 'path'):
                info = os.path.join(self.path, 'model.pt')
            else:
                info = '请设置存储路径'
            QMessageBox.about(self, "模型路径位置", info)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainW = MainWindow()

    sys.exit(app.exec_())
