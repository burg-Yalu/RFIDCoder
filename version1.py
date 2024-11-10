# -*- coding: utf-8 -*-
import random

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.modified_data_H = []  # 保存修改后的数据
        self.generated_data_H = []  # 保存生成的所有数据

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.SD = QtWidgets.QWidget()
        self.SD.setObjectName("SD")
        self.frame = QtWidgets.QFrame(self.SD)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.SendDataBox = QtWidgets.QGroupBox(self.frame)
        self.SendDataBox.setGeometry(QtCore.QRect(20, 30, 321, 241))
        self.SendDataBox.setObjectName("SendDataBox")
        self.SendDataScrollArea = QtWidgets.QScrollArea(self.SendDataBox)
        self.SendDataScrollArea.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.SendDataScrollArea.setWidgetResizable(True)
        self.SendDataScrollArea.setObjectName("SendDataScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.SendDataTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.SendDataTable.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.SendDataTable.setObjectName("SendDataTable")
        self.SendDataTable.setColumnCount(0)
        self.SendDataTable.setRowCount(0)
        self.SendDataScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.InputSingleData = QtWidgets.QTextEdit(self.frame)
        self.InputSingleData.setGeometry(QtCore.QRect(140, 290, 111, 31))
        self.InputSingleData.setObjectName("InputSingleData")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 300, 72, 15))
        self.label.setObjectName("label")
        self.CaculateBitSD = QtWidgets.QPushButton(self.frame)
        self.CaculateBitSD.setGeometry(QtCore.QRect(30, 330, 93, 28))
        self.CaculateBitSD.setObjectName("CaculateBitSD")
        self.CaculateSingleDataBit = QtWidgets.QTextEdit(self.frame)
        self.CaculateSingleDataBit.setGeometry(QtCore.QRect(140, 330, 111, 31))
        self.CaculateSingleDataBit.setObjectName("CaculateSingleDataBit")
        self.GenerateData = QtWidgets.QPushButton(self.frame)
        self.GenerateData.setGeometry(QtCore.QRect(430, 310, 111, 28))
        self.GenerateData.setObjectName("GenerateData")
        self.ReceiveDatalist = QtWidgets.QPushButton(self.frame)
        self.ReceiveDatalist.setGeometry(QtCore.QRect(570, 310, 101, 28))
        self.ReceiveDatalist.setObjectName("ReceiveDatalist")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 390, 641, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(430, 30, 141, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(300, 70, 131, 16))
        self.label_6.setObjectName("label_6")
        self.DataAmount1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.DataAmount1.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.DataAmount1.setObjectName("DataAmount1")
        self.PassedData1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.PassedData1.setGeometry(QtCore.QRect(340, 20, 81, 31))
        self.PassedData1.setObjectName("PassedData1")
        self.WorngDataAmount1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.WorngDataAmount1.setGeometry(QtCore.QRect(510, 20, 81, 31))
        self.WorngDataAmount1.setObjectName("WorngDataAmount1")
        self.UndetectedDataAmount1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.UndetectedDataAmount1.setGeometry(QtCore.QRect(140, 60, 81, 31))
        self.UndetectedDataAmount1.setObjectName("UndetectedDataAmount1")
        self.WrongPercent1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.WrongPercent1.setGeometry(QtCore.QRect(370, 60, 81, 31))
        self.WrongPercent1.setObjectName("WrongPercent1")
        self.ReceiveDataBox = QtWidgets.QGroupBox(self.frame)
        self.ReceiveDataBox.setGeometry(QtCore.QRect(420, 30, 321, 241))
        self.ReceiveDataBox.setObjectName("ReceiveDataBox")
        self.ReceiveDataScrollArea = QtWidgets.QScrollArea(self.ReceiveDataBox)
        self.ReceiveDataScrollArea.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.ReceiveDataScrollArea.setWidgetResizable(True)
        self.ReceiveDataScrollArea.setObjectName("ReceiveDataScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.ReceiveDataTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.ReceiveDataTable.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.ReceiveDataTable.setObjectName("ReceiveDataTable")
        self.ReceiveDataTable.setColumnCount(0)
        self.ReceiveDataTable.setRowCount(0)
        self.ReceiveDataScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.SD, "")


        self.H = QtWidgets.QWidget()
        self.H.setObjectName("H")
        self.frame_2 = QtWidgets.QFrame(self.H)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 791, 521))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.SendDataBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.SendDataBox_2.setGeometry(QtCore.QRect(20, 30, 321, 241))
        self.SendDataBox_2.setObjectName("SendDataBox_2")
        self.SendDataScrollArea_2 = QtWidgets.QScrollArea(self.SendDataBox_2)
        self.SendDataScrollArea_2.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.SendDataScrollArea_2.setWidgetResizable(True)
        self.SendDataScrollArea_2.setObjectName("SendDataScrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.SendDataTable_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.SendDataTable_2.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.SendDataTable_2.setObjectName("SendDataTable_2")
        self.SendDataTable_2.setColumnCount(0)
        self.SendDataTable_2.setRowCount(0)
        self.SendDataScrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.InputSingleData_2 = QtWidgets.QTextEdit(self.frame_2)
        self.InputSingleData_2.setGeometry(QtCore.QRect(140, 290, 111, 31))
        self.InputSingleData_2.setObjectName("InputSingleData_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(60, 300, 72, 15))
        self.label_7.setObjectName("label_7")
        self.CaculateBitSD_2 = QtWidgets.QPushButton(self.frame_2)
        self.CaculateBitSD_2.setGeometry(QtCore.QRect(30, 330, 93, 28))
        self.CaculateBitSD_2.setObjectName("CaculateBitSD_2")
        self.CaculateSingleDataBit_2 = QtWidgets.QTextEdit(self.frame_2)
        self.CaculateSingleDataBit_2.setGeometry(QtCore.QRect(140, 330, 111, 31))
        self.CaculateSingleDataBit_2.setObjectName("CaculateSingleDataBit_2")
        self.GenerateData_2 = QtWidgets.QPushButton(self.frame_2)
        self.GenerateData_2.setGeometry(QtCore.QRect(430, 310, 111, 28))
        self.GenerateData_2.setObjectName("GenerateData_2")
        self.ReceiveDatalist_2 = QtWidgets.QPushButton(self.frame_2)
        self.ReceiveDatalist_2.setGeometry(QtCore.QRect(570, 310, 101, 28))
        self.ReceiveDatalist_2.setObjectName("ReceiveDatalist_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setGeometry(QtCore.QRect(60, 390, 641, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(230, 30, 141, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(430, 30, 141, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(300, 70, 131, 16))
        self.label_12.setObjectName("label_12")
        self.DataAmount1_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.DataAmount1_2.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.DataAmount1_2.setObjectName("DataAmount1_2")
        self.PassedData1_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.PassedData1_2.setGeometry(QtCore.QRect(340, 20, 81, 31))
        self.PassedData1_2.setObjectName("PassedData1_2")
        self.WorngDataAmount1_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.WorngDataAmount1_2.setGeometry(QtCore.QRect(510, 20, 81, 31))
        self.WorngDataAmount1_2.setObjectName("WorngDataAmount1_2")
        self.UndetectedDataAmount1_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.UndetectedDataAmount1_2.setGeometry(QtCore.QRect(140, 60, 81, 31))
        self.UndetectedDataAmount1_2.setObjectName("UndetectedDataAmount1_2")
        self.WrongPercent1_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.WrongPercent1_2.setGeometry(QtCore.QRect(370, 60, 81, 31))
        self.WrongPercent1_2.setObjectName("WrongPercent1_2")
        self.ReceiveDataBox_2 = QtWidgets.QGroupBox(self.frame_2)
        self.ReceiveDataBox_2.setGeometry(QtCore.QRect(420, 30, 321, 241))
        self.ReceiveDataBox_2.setObjectName("ReceiveDataBox_2")
        self.ReceiveDataScrollArea_2 = QtWidgets.QScrollArea(self.ReceiveDataBox_2)
        self.ReceiveDataScrollArea_2.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.ReceiveDataScrollArea_2.setWidgetResizable(True)
        self.ReceiveDataScrollArea_2.setObjectName("ReceiveDataScrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.ReceiveDataTable_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_4)
        self.ReceiveDataTable_2.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.ReceiveDataTable_2.setObjectName("ReceiveDataTable_2")
        self.ReceiveDataTable_2.setColumnCount(0)
        self.ReceiveDataTable_2.setRowCount(0)
        self.ReceiveDataScrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.tabWidget.addTab(self.H, "")



        self.CRC = QtWidgets.QWidget()
        self.CRC.setObjectName("CRC")
        self.frame_3 = QtWidgets.QFrame(self.CRC)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 791, 521))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.SendDataBox_3 = QtWidgets.QGroupBox(self.frame_3)
        self.SendDataBox_3.setGeometry(QtCore.QRect(20, 30, 321, 241))
        self.SendDataBox_3.setObjectName("SendDataBox_3")
        self.SendDataScrollArea_3 = QtWidgets.QScrollArea(self.SendDataBox_3)
        self.SendDataScrollArea_3.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.SendDataScrollArea_3.setWidgetResizable(True)
        self.SendDataScrollArea_3.setObjectName("SendDataScrollArea_3")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.SendDataTable_3 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_5)
        self.SendDataTable_3.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.SendDataTable_3.setObjectName("SendDataTable_3")
        self.SendDataTable_3.setColumnCount(0)
        self.SendDataTable_3.setRowCount(0)
        self.SendDataScrollArea_3.setWidget(self.scrollAreaWidgetContents_5)
        self.InputSingleData_3 = QtWidgets.QTextEdit(self.frame_3)
        self.InputSingleData_3.setGeometry(QtCore.QRect(140, 290, 111, 31))
        self.InputSingleData_3.setObjectName("InputSingleData_3")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(60, 300, 72, 15))
        self.label_13.setObjectName("label_13")
        self.CaculateBitSD_3 = QtWidgets.QPushButton(self.frame_3)
        self.CaculateBitSD_3.setGeometry(QtCore.QRect(30, 330, 93, 28))
        self.CaculateBitSD_3.setObjectName("CaculateBitSD_3")
        self.CaculateSingleDataBit_3 = QtWidgets.QTextEdit(self.frame_3)
        self.CaculateSingleDataBit_3.setGeometry(QtCore.QRect(140, 330, 111, 31))
        self.CaculateSingleDataBit_3.setObjectName("CaculateSingleDataBit_3")
        self.GenerateData_3 = QtWidgets.QPushButton(self.frame_3)
        self.GenerateData_3.setGeometry(QtCore.QRect(430, 310, 111, 28))
        self.GenerateData_3.setObjectName("GenerateData_3")
        self.ReceiveDatalist_3 = QtWidgets.QPushButton(self.frame_3)
        self.ReceiveDatalist_3.setGeometry(QtCore.QRect(570, 310, 101, 28))
        self.ReceiveDatalist_3.setObjectName("ReceiveDatalist_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_5.setGeometry(QtCore.QRect(60, 390, 641, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(230, 30, 141, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(430, 30, 141, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(300, 70, 131, 16))
        self.label_18.setObjectName("label_18")
        self.DataAmount1_3 = QtWidgets.QTextEdit(self.groupBox_5)
        self.DataAmount1_3.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.DataAmount1_3.setObjectName("DataAmount1_3")
        self.PassedData1_3 = QtWidgets.QTextEdit(self.groupBox_5)
        self.PassedData1_3.setGeometry(QtCore.QRect(340, 20, 81, 31))
        self.PassedData1_3.setObjectName("PassedData1_3")
        self.WorngDataAmount1_3 = QtWidgets.QTextEdit(self.groupBox_5)
        self.WorngDataAmount1_3.setGeometry(QtCore.QRect(510, 20, 81, 31))
        self.WorngDataAmount1_3.setObjectName("WorngDataAmount1_3")
        self.UndetectedDataAmount1_3 = QtWidgets.QTextEdit(self.groupBox_5)
        self.UndetectedDataAmount1_3.setGeometry(QtCore.QRect(140, 60, 81, 31))
        self.UndetectedDataAmount1_3.setObjectName("UndetectedDataAmount1_3")
        self.WrongPercent1_3 = QtWidgets.QTextEdit(self.groupBox_5)
        self.WrongPercent1_3.setGeometry(QtCore.QRect(370, 60, 81, 31))
        self.WrongPercent1_3.setObjectName("WrongPercent1_3")
        self.ReceiveDataBox_3 = QtWidgets.QGroupBox(self.frame_3)
        self.ReceiveDataBox_3.setGeometry(QtCore.QRect(420, 30, 321, 241))
        self.ReceiveDataBox_3.setObjectName("ReceiveDataBox_3")
        self.ReceiveDataScrollArea_3 = QtWidgets.QScrollArea(self.ReceiveDataBox_3)
        self.ReceiveDataScrollArea_3.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.ReceiveDataScrollArea_3.setWidgetResizable(True)
        self.ReceiveDataScrollArea_3.setObjectName("ReceiveDataScrollArea_3")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.ReceiveDataTable_3 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_6)
        self.ReceiveDataTable_3.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.ReceiveDataTable_3.setObjectName("ReceiveDataTable_3")
        self.ReceiveDataTable_3.setColumnCount(0)
        self.ReceiveDataTable_3.setRowCount(0)
        self.ReceiveDataScrollArea_3.setWidget(self.scrollAreaWidgetContents_6)
        self.tabWidget.addTab(self.CRC, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.GenerateData.clicked.connect(self.generate_data)
        self.ReceiveDatalist.clicked.connect(self.receive_data)
        self.GenerateData_2.clicked.connect(self.generate_data_H)


    def generate_data(self):
        # 生成长度为100的8位二进制数组
        self.data = []
        for _ in range(100):
            binary_data = ''.join(random.choice('01') for _ in range(8))  # 随机生成8位二进制数据
            parity_bit = self.calculate_parity(binary_data)  # 计算奇偶校验位
            self.data.append((binary_data, parity_bit))

        # 计算校验数据
        self.PassedData1.setText(str(sum(1 for data, parity in self.data if parity == self.calculate_parity(data))))
        self.WorngDataAmount1.setText(
            str(sum(1 for data, parity in self.data if parity != self.calculate_parity(data))))
        self.DataAmount1.setText(str(len(self.data)))  # 总数据量
        self.UndetectedDataAmount1.setText('0')  # 初步设定无异常数据，后面再根据修改情况调整
        wrong_and_undetected = int(self.WorngDataAmount1.toPlainText())  # 错误数据数量
        total_data = int(self.DataAmount1.toPlainText())
        self.WrongPercent1.setText(f"{(wrong_and_undetected / total_data) * 100:.2f}%")  # 错误率

        # 清空表格并填充新的数据
        self.SendDataTable.setRowCount(100)  # 设置100行
        self.SendDataTable.setColumnCount(2)  # 设置2列

        for row, (data, parity) in enumerate(self.data):
            self.SendDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(data))  # 第一列：8位二进制数据
            self.SendDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(parity))  # 第二列：奇偶校验位

        # 调整表格列宽度以适应内容
        self.SendDataTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.SendDataTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def calculate_parity(self, binary_data):
        # 计算奇偶校验位：统计1的个数，如果为偶数则校验位为0，否则为1
        ones_count = binary_data.count('1')
        return '0' if ones_count % 2 == 0 else '1'

    def receive_data(self):
        # 随机修改不超过10个元素，每个元素修改1到2位
        self.modified_data = []
        undetected1=0;

        # 随机选择10个位置进行修改（最多10个元素）
        indices_to_modify = random.sample(range(100), min(10, len(self.data)))  # 随机选择最多10组数据

        for idx in range(100):
            binary_data, original_parity = self.data[idx]

            # 如果当前数据组被选中进行修改
            if idx in indices_to_modify:
                modified_binary = list(binary_data)  # 将字符串转换为列表便于修改
                num_changes = random.randint(1, 2)  # 随机选择修改1到2位

                for _ in range(num_changes):
                    index = random.randint(0, 7)  # 随机选择一个位置
                    modified_binary[index] = '1' if modified_binary[index] == '0' else '0'  # 改变该位

                modified_binary = ''.join(modified_binary)
                modified_parity = self.calculate_parity(modified_binary)
                self.modified_data.append((modified_binary, original_parity, modified_parity))
                if modified_binary != binary_data and original_parity == modified_parity:undetected1+=1
            else:
                # 未被选中的数据保持原样
                self.modified_data.append((binary_data, original_parity, original_parity))

        # 清空接收数据表格并填充新的数据
        self.ReceiveDataTable.setRowCount(len(self.modified_data))  # 设置行数为修改后的数据长度
        self.ReceiveDataTable.setColumnCount(3)  # 设置3列

        for row, (modified_binary, original_parity, modified_parity) in enumerate(self.modified_data):
            self.ReceiveDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(modified_binary))  # 修改后的二进制数据
            self.ReceiveDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(original_parity))  # 原始校验位
            self.ReceiveDataTable.setItem(row, 2, QtWidgets.QTableWidgetItem(modified_parity))  # 新计算的校验位

        # 更新数据统计
        passed = sum(
            1 for data, original_parity, modified_parity in self.modified_data if original_parity == modified_parity)
        wrong = sum(
            1 for data, original_parity, modified_parity in self.modified_data if original_parity != modified_parity)


        # undetected 的计算：修改后的数据与原数据不一致，且原始校验位和修改后的校验位一致

        self.PassedData1.setText(str(passed))
        self.WorngDataAmount1.setText(str(wrong))
        self.UndetectedDataAmount1.setText(str(undetected1))  # 更新 undetected 数据

        # 计算百分比
        total = len(self.modified_data)
        wrong_and_undetected = wrong + undetected1
        self.WrongPercent1.setText(f"{(wrong_and_undetected / total) * 100:.2f}%")

        # 清空接收数据表格并填充新的数据
        self.ReceiveDataTable.setRowCount(len(self.modified_data))  # 设置行数为修改后的数据长度
        self.ReceiveDataTable.setColumnCount(3)  # 设置3列

        for row, (modified_binary, original_parity, modified_parity) in enumerate(self.modified_data):
            # 更新表格内容
            self.ReceiveDataTable.setItem(row, 0, QtWidgets.QTableWidgetItem(modified_binary))  # 第一列：修改后的8位数据
            self.ReceiveDataTable.setItem(row, 1, QtWidgets.QTableWidgetItem(original_parity))  # 第二列：原始数据的奇偶校验位
            self.ReceiveDataTable.setItem(row, 2, QtWidgets.QTableWidgetItem(modified_parity))  # 第三列：修改后的奇偶校验位

            # 判断第二列和第三列的奇偶校验位是否相同
            if original_parity != modified_parity:
                # 如果第二列和第三列不同，设置该行文本为红色
                self.set_row_color(row, "red")
            elif modified_binary != self.data[row][0]:
                # 如果第二列和第三列相同，但修改后的数据与原数据不同，设置该行文本为绿色
                self.set_row_color(row, "green")

        # 调整表格列宽度以适应内容
        self.ReceiveDataTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ReceiveDataTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ReceiveDataTable.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # 获取表格宽度
        table_width = self.ReceiveDataTable.width()

        # 设置三列的宽度比例 2:1:1
        column_0_width = table_width * 2 / 4  # 第1列宽度
        column_1_width = table_width * 1 / 4  # 第2列宽度
        column_2_width = table_width * 1 / 4  # 第3列宽度

        # 设置列宽
        self.ReceiveDataTable.setColumnWidth(0, column_0_width)
        self.ReceiveDataTable.setColumnWidth(1, column_1_width)
        self.ReceiveDataTable.setColumnWidth(2, column_2_width)

    def generate_data_H(self):
        self.generate_data_H_original = []
        self.generate_data_H_originalVerify = []
        self.generate_data_H_SendData = []
        for _ in range(100):
            parity_bits_H_Original = [0] * 4
            temp_data = ''.join(random.choice('01') for _ in range(8))
            for i in range(4):
                parity_bits_H_Original[i] = self.calculate_parity_H(temp_data, i)
            self.generate_data_H_originalVerify.append(parity_bits_H_Original)
            print(parity_bits_H_Original)
            self.generate_data_H_original.append(temp_data)
            print(temp_data)
            full_data = ['0'] * 12
            data_idx = 0
            for i in range(12):
                if i not in [0, 1, 3, 7]:  # 校验位的索引，分别是1, 2, 4, 8
                    full_data[i] = temp_data[data_idx]
                    data_idx += 1
            full_data[0], full_data[1], full_data[3], full_data[7] = parity_bits_H_Original[0], parity_bits_H_Original[1], parity_bits_H_Original[2], parity_bits_H_Original[3]
            send_data = ''.join(map(str, full_data))
            self.generate_data_H_SendData.append(send_data)
            print(send_data)
        self.SendDataTable_2.setRowCount(100)  # 设置100行
        self.SendDataTable_2.setColumnCount(3)  # 设置2列

        for i in range(100):
            # 第一列：原始8位数据
            self.SendDataTable_2.setItem(i, 0, QtWidgets.QTableWidgetItem(self.generate_data_H_original[i]))

            # 第二列：奇偶校验位
            self.SendDataTable_2.setItem(i, 1, QtWidgets.QTableWidgetItem(
                ''.join(map(str, self.generate_data_H_originalVerify[i]))))

            # 第三列：完整的发送数据
            self.SendDataTable_2.setItem(i, 2, QtWidgets.QTableWidgetItem(self.generate_data_H_SendData[i]))

        # 调整表格列宽度以适应内容
        self.SendDataTable_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.SendDataTable_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.SendDataTable_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    #海明校验单个位校验位
    def calculate_parity_H(self,temp_data, index):
        parity = 0
        for i in range(8):
            if ((i >> index) & 1) == 1:  # 按照海明码规则选择对应的位
                parity ^= int(temp_data[i])  # 异或校验
        return parity

    def set_row_color(self, row, color):
        # 设置行的颜色
        for col in range(3):
            item = self.ReceiveDataTable.item(row, col)
            if item:
                item.setForeground(QtGui.QColor(color))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SendDataBox.setTitle(_translate("MainWindow", "发送数据"))
        self.label.setText(_translate("MainWindow", "数据："))
        self.CaculateBitSD.setText(_translate("MainWindow", "计算校验位"))
        self.GenerateData.setText(_translate("MainWindow", "产生发送数据"))
        self.ReceiveDatalist.setText(_translate("MainWindow", "接收数据"))
        self.groupBox_3.setTitle(_translate("MainWindow", "结果"))
        self.label_2.setText(_translate("MainWindow", "共传输数据："))
        self.label_3.setText(_translate("MainWindow", "检验通过数据："))
        self.label_4.setText(_translate("MainWindow", "出错数据："))
        self.label_5.setText(_translate("MainWindow", "未检出错误数据："))
        self.label_6.setText(_translate("MainWindow", "错误率："))
        self.ReceiveDataBox.setTitle(_translate("MainWindow", "发送数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SD), _translate("MainWindow", "Tab 1"))
        self.SendDataBox_2.setTitle(_translate("MainWindow", "发送数据"))
        self.label_7.setText(_translate("MainWindow", "数据："))
        self.CaculateBitSD_2.setText(_translate("MainWindow", "计算校验位"))
        self.GenerateData_2.setText(_translate("MainWindow", "产生发送数据"))
        self.ReceiveDatalist_2.setText(_translate("MainWindow", "接收数据"))
        self.groupBox_4.setTitle(_translate("MainWindow", "结果"))
        self.label_8.setText(_translate("MainWindow", "共传输数据："))
        self.label_9.setText(_translate("MainWindow", "检验通过数据："))
        self.label_10.setText(_translate("MainWindow", "出错数据："))
        self.label_11.setText(_translate("MainWindow", "未检出错误数据："))
        self.label_12.setText(_translate("MainWindow", "错误率："))
        self.ReceiveDataBox_2.setTitle(_translate("MainWindow", "发送数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.H), _translate("MainWindow", "Tab 2"))
        self.SendDataBox_3.setTitle(_translate("MainWindow", "发送数据"))
        self.label_13.setText(_translate("MainWindow", "数据："))
        self.CaculateBitSD_3.setText(_translate("MainWindow", "计算校验位"))
        self.GenerateData_3.setText(_translate("MainWindow", "产生发送数据"))
        self.ReceiveDatalist_3.setText(_translate("MainWindow", "接收数据"))
        self.groupBox_5.setTitle(_translate("MainWindow", "结果"))
        self.label_14.setText(_translate("MainWindow", "共传输数据："))
        self.label_15.setText(_translate("MainWindow", "检验通过数据："))
        self.label_16.setText(_translate("MainWindow", "出错数据："))
        self.label_17.setText(_translate("MainWindow", "未检出错误数据："))
        self.label_18.setText(_translate("MainWindow", "错误率："))
        self.ReceiveDataBox_3.setTitle(_translate("MainWindow", "发送数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CRC), _translate("MainWindow", "页"))
