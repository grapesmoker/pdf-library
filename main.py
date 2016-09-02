#!/usr/bin/env python

import sys

from main_window import MainWindow
from new_lib_dialog import Ui_newLibDialog

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QInputDialog
from PyQt5.QtCore import QCoreApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setup_actions()
    window.show()

    sys.exit(app.exec_())