# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_document_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditDocumentDialog(object):
    def setupUi(self, EditDocumentDialog):
        EditDocumentDialog.setObjectName("EditDocumentDialog")
        EditDocumentDialog.resize(661, 608)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditDocumentDialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 540, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(EditDocumentDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(29, 30, 601, 471))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtTitle = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtTitle.setObjectName("txtTitle")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtTitle)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cmbAuthor = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cmbAuthor.setObjectName("cmbAuthor")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbAuthor)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lstCategories = QtWidgets.QListView(self.formLayoutWidget)
        self.lstCategories.setObjectName("lstCategories")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lstCategories)
        self.txtPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPath.setObjectName("txtPath")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtPath)

        self.retranslateUi(EditDocumentDialog)
        self.buttonBox.accepted.connect(EditDocumentDialog.accept)
        self.buttonBox.rejected.connect(EditDocumentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditDocumentDialog)

    def retranslateUi(self, EditDocumentDialog):
        _translate = QtCore.QCoreApplication.translate
        EditDocumentDialog.setWindowTitle(_translate("EditDocumentDialog", "Dialog"))
        self.label.setText(_translate("EditDocumentDialog", "Title"))
        self.label_2.setText(_translate("EditDocumentDialog", "Author"))
        self.label_3.setText(_translate("EditDocumentDialog", "Filename"))
        self.label_5.setText(_translate("EditDocumentDialog", "Categories"))

