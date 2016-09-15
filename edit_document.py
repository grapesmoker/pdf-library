import models
import os
import shutil
import hashlib

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QGraphicsScene
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap

from ui_edit_document_dialog import Ui_EditDocumentDialog
from edit_author import EditAuthorDialog
from wand.image import Image


class EditDocumentDialog(QDialog):

    def __init__(self, doc_id, parent=None):
        super(EditDocumentDialog, self).__init__(parent)

        self.ui = Ui_EditDocumentDialog()
        self.ui.setupUi(self)
        self.ui.authorComboLayout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        self.categories_model = QStandardItemModel()
        self.ui.lstCategories.setModel(self.categories_model)
        self.ui.txtPath.setEnabled(False)
        self.id = doc_id
        self.author_model = QStandardItemModel()
        self.ui.lstAuthors.setModel(self.author_model)
        self.ui.lstCategories.setModel(self.categories_model)

        self.doc = None
        self.fetch_from_db()
        self.accepted.connect(self.save_to_db)
        self.finished.connect(self.cleanup_temp_files)
        self.generated_preview_files = set()

        self.ui.btnAddAuthor.clicked.connect(self.add_author)
        self.ui.btnRemoveAuthor.clicked.connect(self.remove_author)
        self.ui.btnCreateNewAuthor.clicked.connect(self.create_new_author)
        self.ui.spinPreview.valueChanged.connect(self.generate_preview)
        self.preview = QGraphicsScene(self)
        self.ui.grPreview.setScene(self.preview)
        self.generate_preview()

    def set_categories(self, categories):

        for cat in categories:
            item = QStandardItem(str(cat))
            item.setData(cat)
            item.setCheckable(True)
            if cat in self.doc.categories:
                item.setCheckState(Qt.Checked)
            self.categories_model.appendRow(item)

    def set_authors(self, authors):

        for author in authors:
            self.ui.cmbAuthor.addItem(str(author), author)
            if author in self.doc.authors:
                author_item = QStandardItem(str(author))
                author_item.setData(author)
                self.author_model.appendRow(author_item)

    def fetch_from_db(self):

        self.doc = self.parent().session.query(models.Document).filter(models.Document.id == self.id).one()
        self.ui.txtTitle.setText(self.doc.name)
        self.ui.txtPath.setText(self.doc.path)
        # self.ui.cmbAuthor.setCurrentText(str(self.doc.authors))
        authors = self.parent().session.query(models.Author).order_by(models.Author.last_name.asc())
        categories = self.parent().session.query(models.Category).order_by(models.Category.name.asc())

        self.set_categories(categories)
        self.set_authors(authors)

    def generate_preview(self):

        if self.doc:
            self.preview.clear()
            page = self.ui.spinPreview.value()
            doc_hash = hashlib.md5(self.doc.path).hexdigest()
            tmp_pdf_file = os.path.abspath(os.path.join('./tmp', doc_hash + '-{}'.format(page) + '.pdf'))
            tmp_img_file = os.path.abspath(os.path.join('./tmp', doc_hash + '-{}'.format(page) + '.png'))
            if not os.path.exists(tmp_pdf_file):
                shutil.copy(self.doc.path, tmp_pdf_file)
            if not os.path.exists(tmp_img_file):
                img = Image(filename=tmp_pdf_file + '[{}]'.format(page))
                img.save(filename=tmp_img_file)
            pixmap = QPixmap()
            pixmap.load(tmp_img_file)
            self.preview.addPixmap(pixmap)
            self.generated_preview_files.add(tmp_pdf_file)
            self.generated_preview_files.add(tmp_img_file)

    def save_to_db(self):

        self.doc.name = self.ui.txtTitle.text()
        self.doc.authors = []
        self.doc.categories = []

        for row in range(self.author_model.rowCount()):
            author_item = self.author_model.item(row)
            author = author_item.data()
            self.doc.authors.append(author)

        for row in range(self.categories_model.rowCount()):
            cat_item = self.categories_model.item(row)
            if cat_item.checkState() == Qt.Checked:
                self.doc.categories.append(cat_item.data())

        self.parent().session.commit()

    def cleanup_temp_files(self):

        for f in self.generated_preview_files:
            os.unlink(f)

    def add_author(self):

        author = self.ui.cmbAuthor.currentData()
        author_name = self.ui.cmbAuthor.currentText()
        author_item = QStandardItem(author_name)
        author_item.setData(author)

        self.author_model.appendRow(author_item)

    def remove_author(self):

        selection = self.ui.lstAuthors.selectionModel().selectedRows()

        for row in selection:
            self.author_model.removeRow(row.row())

    def create_new_author(self):

        dialog = EditAuthorDialog(None, parent=self.parent())
        result = dialog.exec_()

        if result:
            author = dialog.author
            self.parent().populate_author_row(self.parent().author_model.rowCount(), author)
            authors = self.parent().session.query(models.Author).order_by(models.Author.last_name.asc())
            self.set_authors(authors)
            author_item = QStandardItem(str(author))
            author_item.setData(author)
            self.author_model.appendRow(author_item)