import random

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 521))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 321, 241))
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.tableWidget.setObjectName("发送数据tableWidget")
        self.tableWidget.setColumnCount(3)  # 三列
        self.tableWidget.setRowCount(100)  # 100行
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(140, 290, 111, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 300, 72, 15))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 310, 111, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.generate_data)  # 点击按钮生成数据
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 310, 101, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 390, 641, 121))
        self.groupBox_3.setObjectName("groupBox_3")

        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 30, 321, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(9, 46, 291, 181))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 289, 179))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 291, 181))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.groupBox.setTitle(_translate("MainWindow", "发送数据"))
        self.label.setText(_translate("MainWindow", "数据："))
        self.pushButton.setText(_translate("MainWindow", "计算校验位"))
        self.pushButton_2.setText(_translate("MainWindow", "产生发送数据"))
        self.pushButton_3.setText(_translate("MainWindow", "接收数据"))
        self.groupBox_3.setTitle(_translate("MainWindow", "结果"))
        self.groupBox_2.setTitle(_translate("MainWindow", "发送数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

    def generate_data(self):
        """
        生成100行数据，第一列为1到100，第二列为随机8位数据，第三列为该数据的奇偶校验位。
        """
        for row in range(100):
            # 第一列为1到100的行号
            row_number = row + 1

            # 第二列为随机8位数据
            random_data = random.randint(0, 255)  # 8位数据的范围为0到255
            binary_data = format(random_data, '08b')  # 转为8位二进制字符串

            # 第三列为该数据的奇偶校验位
            parity_bit = self.calculate_parity(binary_data)

            # 在表格中设置数据
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row_number)))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(binary_data))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(parity_bit)))

    def calculate_parity(self, binary_data):
        """
        计算8位数据的奇偶校验位，偶校验（即1的个数为偶数时校验位为0，奇数时校验位为1）。
        """
        ones_count = binary_data.count('1')
        return '1' if ones_count % 2 != 0 else '0'
