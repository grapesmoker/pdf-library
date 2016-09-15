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
        EditDocumentDialog.resize(1072, 608)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditDocumentDialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 540, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(EditDocumentDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(29, 30, 601, 491))
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
        self.authorLayout = QtWidgets.QHBoxLayout()
        self.authorLayout.setObjectName("authorLayout")
        self.authorComboLayout = QtWidgets.QVBoxLayout()
        self.authorComboLayout.setObjectName("authorComboLayout")
        self.cmbAuthor = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbAuthor.sizePolicy().hasHeightForWidth())
        self.cmbAuthor.setSizePolicy(sizePolicy)
        self.cmbAuthor.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbAuthor.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cmbAuthor.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cmbAuthor.setMinimumContentsLength(200)
        self.cmbAuthor.setObjectName("cmbAuthor")
        self.authorComboLayout.addWidget(self.cmbAuthor)
        self.btnAddAuthor = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddAuthor.sizePolicy().hasHeightForWidth())
        self.btnAddAuthor.setSizePolicy(sizePolicy)
        self.btnAddAuthor.setMinimumSize(QtCore.QSize(160, 0))
        self.btnAddAuthor.setObjectName("btnAddAuthor")
        self.authorComboLayout.addWidget(self.btnAddAuthor)
        self.btnCreateNewAuthor = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCreateNewAuthor.sizePolicy().hasHeightForWidth())
        self.btnCreateNewAuthor.setSizePolicy(sizePolicy)
        self.btnCreateNewAuthor.setMinimumSize(QtCore.QSize(160, 0))
        self.btnCreateNewAuthor.setObjectName("btnCreateNewAuthor")
        self.authorComboLayout.addWidget(self.btnCreateNewAuthor)
        self.btnRemoveAuthor = QtWidgets.QPushButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRemoveAuthor.sizePolicy().hasHeightForWidth())
        self.btnRemoveAuthor.setSizePolicy(sizePolicy)
        self.btnRemoveAuthor.setMinimumSize(QtCore.QSize(160, 0))
        self.btnRemoveAuthor.setObjectName("btnRemoveAuthor")
        self.authorComboLayout.addWidget(self.btnRemoveAuthor)
        self.authorLayout.addLayout(self.authorComboLayout)
        self.lstAuthors = QtWidgets.QListView(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstAuthors.sizePolicy().hasHeightForWidth())
        self.lstAuthors.setSizePolicy(sizePolicy)
        self.lstAuthors.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lstAuthors.setObjectName("lstAuthors")
        self.authorLayout.addWidget(self.lstAuthors)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.authorLayout)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPath.setObjectName("txtPath")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtPath)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.categoryLayout = QtWidgets.QHBoxLayout()
        self.categoryLayout.setObjectName("categoryLayout")
        self.lstCategories = QtWidgets.QListView(self.formLayoutWidget)
        self.lstCategories.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.lstCategories.setObjectName("lstCategories")
        self.categoryLayout.addWidget(self.lstCategories)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.categoryLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(EditDocumentDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(640, 30, 421, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.grPreview = QtWidgets.QGraphicsView(self.verticalLayoutWidget_2)
        self.grPreview.setObjectName("grPreview")
        self.verticalLayout.addWidget(self.grPreview)
        self.spinPreview = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinPreview.setObjectName("spinPreview")
        self.verticalLayout.addWidget(self.spinPreview)

        self.retranslateUi(EditDocumentDialog)
        self.buttonBox.accepted.connect(EditDocumentDialog.accept)
        self.buttonBox.rejected.connect(EditDocumentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditDocumentDialog)

    def retranslateUi(self, EditDocumentDialog):
        _translate = QtCore.QCoreApplication.translate
        EditDocumentDialog.setWindowTitle(_translate("EditDocumentDialog", "Dialog"))
        self.label.setText(_translate("EditDocumentDialog", "Title"))
        self.label_2.setText(_translate("EditDocumentDialog", "Author"))
        self.btnAddAuthor.setText(_translate("EditDocumentDialog", "Add author"))
        self.btnCreateNewAuthor.setText(_translate("EditDocumentDialog", "Create and add author"))
        self.btnRemoveAuthor.setText(_translate("EditDocumentDialog", "Remove author"))
        self.label_3.setText(_translate("EditDocumentDialog", "Filename"))
        self.label_5.setText(_translate("EditDocumentDialog", "Categories"))
        self.label_4.setText(_translate("EditDocumentDialog", "Preview"))

