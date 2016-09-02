# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_lib_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_newLibDialog(object):
    def setupUi(self, newLibDialog):
        newLibDialog.setObjectName("newLibDialog")
        newLibDialog.setWindowModality(QtCore.Qt.NonModal)
        newLibDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(newLibDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(newLibDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.selectLibRoot = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectLibRoot.sizePolicy().hasHeightForWidth())
        self.selectLibRoot.setSizePolicy(sizePolicy)
        self.selectLibRoot.setObjectName("selectLibRoot")
        self.gridLayout.addWidget(self.selectLibRoot, 1, 1, 1, 1)
        self.actionSelectLibRoot = QtWidgets.QAction(newLibDialog)
        self.actionSelectLibRoot.setObjectName("actionSelectLibRoot")

        self.retranslateUi(newLibDialog)
        self.buttonBox.accepted.connect(newLibDialog.accept)
        self.buttonBox.rejected.connect(newLibDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newLibDialog)

    def retranslateUi(self, newLibDialog):
        _translate = QtCore.QCoreApplication.translate
        newLibDialog.setWindowTitle(_translate("newLibDialog", "New Library"))
        self.label.setText(_translate("newLibDialog", "Library Name"))
        self.label_2.setText(_translate("newLibDialog", "Root"))
        self.selectLibRoot.setText(_translate("newLibDialog", "Select"))
        self.actionSelectLibRoot.setText(_translate("newLibDialog", "selectLibRoot"))

