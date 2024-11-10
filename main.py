import sys
from PyQt5 import QtWidgets
from version3 import Ui_MainWindow  # 假设你的 UI 代码是保存为 test_ui.py


def main():
    app = QtWidgets.QApplication(sys.argv)  # 创建一个应用程序实例
    MainWindow = QtWidgets.QMainWindow()  # 创建主窗口实例

    ui = Ui_MainWindow()  # 创建 UI 实例
    ui.setupUi(MainWindow)  # 设置 UI 到主窗口

    MainWindow.show()  # 显示窗口
    sys.exit(app.exec_())  # 进入应用程序主循环


if __name__ == "__main__":
    main()
