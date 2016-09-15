# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rename_document_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RenameDocumentDialog(object):
    def setupUi(self, RenameDocumentDialog):
        RenameDocumentDialog.setObjectName("RenameDocumentDialog")
        RenameDocumentDialog.resize(600, 405)
        self.buttonBox = QtWidgets.QDialogButtonBox(RenameDocumentDialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 360, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(RenameDocumentDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 599, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.txtNameFormat = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtNameFormat.setObjectName("txtNameFormat")
        self.gridLayout.addWidget(self.txtNameFormat, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.retranslateUi(RenameDocumentDialog)
        self.buttonBox.accepted.connect(RenameDocumentDialog.accept)
        self.buttonBox.rejected.connect(RenameDocumentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RenameDocumentDialog)

    def retranslateUi(self, RenameDocumentDialog):
        _translate = QtCore.QCoreApplication.translate
        RenameDocumentDialog.setWindowTitle(_translate("RenameDocumentDialog", "Dialog"))
        self.label.setText(_translate("RenameDocumentDialog", "Format string"))
        self.label_8.setText(_translate("RenameDocumentDialog", "{title} - \n"
"document title"))
        self.label_6.setText(_translate("RenameDocumentDialog", "{categories} - \n"
"document categories"))
        self.label_7.setText(_translate("RenameDocumentDialog", "{last_name} - \n"
"first author last name"))
        self.label_3.setText(_translate("RenameDocumentDialog", "{author} - \n"
"first author full name"))
        self.label_4.setText(_translate("RenameDocumentDialog", "{publisher} - \n"
"document publisher"))
        self.label_5.setText(_translate("RenameDocumentDialog", "{first_name} - \n"
"first author first name"))
        self.label_9.setText(_translate("RenameDocumentDialog", "{authors_last_names} -\n"
"all authors\' last names"))
        self.label_10.setText(_translate("RenameDocumentDialog", "{authors} -\n"
"all authors\' full names"))
        self.label_2.setText(_translate("RenameDocumentDialog", "The format string can contain the following symbols that interpolate metadata values into the file name:"))

