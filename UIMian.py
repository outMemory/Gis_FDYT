# -*- coding: utf-8 -*-
"""
ui界面调用窗口，主程序
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_main import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
