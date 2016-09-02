import models

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ui_edit_document_dialog import Ui_EditDocumentDialog


class EditDocumentDialog(QDialog):

    def __init__(self, doc_id, parent=None):
        super(EditDocumentDialog, self).__init__(parent)

        self.ui = Ui_EditDocumentDialog()
        self.ui.setupUi(self)

        self.categories_model = QStandardItemModel()
        self.ui.lstCategories.setModel(self.categories_model)
        self.ui.txtPath.setEnabled(False)
        self.id = doc_id

        self.fetch_from_db()
        self.accepted.connect(self.save_to_db)

    def set_title(self, title):

        self.ui.txtTitle.setText(title)

    def set_author(self, author):

        self.ui.cmbAuthor.setCurrentText(author)

    def set_categories(self, categories):

        for cat in categories:
            item = QStandardItem()
            item.setText(cat)
            item.setCheckable(True)
            self.categories_model.appendRow(item)

    def fetch_from_db(self):

        self.doc = self.parent().session.query(models.Document).filter(models.Document.id == self.id).one()
        self.ui.txtTitle.setText(self.doc.name)
        self.ui.txtPath.setText(self.doc.path)
        self.ui.cmbAuthor.setCurrentText(str(self.doc.authors))

    def save_to_db(self):

        self.doc.name = self.ui.txtTitle.text()

        self.parent().session.commit()
