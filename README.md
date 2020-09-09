### 1.文件结构

- document - 文档信息
- html - 针对各自模块添加对应的html文件
- modelcompress - 模型压缩对应的代码文件夹
- nas - 模型搜索对应的代码文件夹
- qtui - qt对应的ui文件
- tools - 共用的一些小函数

### 2. 环境配置

- python3.6以上版本

- pyqt5 统一使用5.12版本，安装如下


```shell
	pip install pyqt5==5.12
	pip install PyQtWebEngine==5.12	
```

### 3. 运行

​	以模型压缩为例，进入modelcompress目录	

```shell
	python modelcomp.py
```

### 4. 使用qtcreator打开qtui下的ui文件即可编辑界面

- 安装qtcreator，Ubuntu系统可直接使用如下命令：

```
	sudo apt install qtcreator
```

- 其他操作系统对应的版本下载链接：<http://download.qt.io/archive/qtcreator/4.4/4.4.1/>

### 5. ui文件转py文件

​	进入ui文件所在的文件夹，打开命令行运行：

```
	pyuic5 -o modelcomp_ui.py modelcompress.ui
```

​	注意第一个参数是需要创建的py文件名，第二参数是ui文件

​	

​	

