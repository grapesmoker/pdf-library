import models

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ui_rename_document_dialog import Ui_RenameDocumentDialog


class RenameDocumentDialog(QDialog):

    def __init__(self, parent):
        super(RenameDocumentDialog, self).__init__(parent)

        self.ui = Ui_RenameDocumentDialog()
        self.ui.setupUi(self)