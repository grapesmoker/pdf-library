# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_author_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditAuthorDialog(object):
    def setupUi(self, EditAuthorDialog):
        EditAuthorDialog.setObjectName("EditAuthorDialog")
        EditAuthorDialog.resize(385, 203)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditAuthorDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(EditAuthorDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 361, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtFirstName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtFirstName.setObjectName("txtFirstName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtFirstName)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtMiddleName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtMiddleName.setObjectName("txtMiddleName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtMiddleName)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtLastName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtLastName.setObjectName("txtLastName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtLastName)

        self.retranslateUi(EditAuthorDialog)
        self.buttonBox.accepted.connect(EditAuthorDialog.accept)
        self.buttonBox.rejected.connect(EditAuthorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditAuthorDialog)

    def retranslateUi(self, EditAuthorDialog):
        _translate = QtCore.QCoreApplication.translate
        EditAuthorDialog.setWindowTitle(_translate("EditAuthorDialog", "Dialog"))
        self.label.setText(_translate("EditAuthorDialog", "First name"))
        self.label_2.setText(_translate("EditAuthorDialog", "Middle name"))
        self.label_3.setText(_translate("EditAuthorDialog", "Last name"))

