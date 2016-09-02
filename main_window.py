import os
import models

from functools import partial

from PyQt5.QtWidgets import (QMainWindow, QInputDialog, QFileDialog,
                             QApplication, QMenu, QAction, QAbstractItemView,
                             QMessageBox)
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QCursor, QDesktopServices
from PyQt5.QtCore import QModelIndex, Qt, QUrl
from ui_main_window import Ui_MainWindow
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyPDF2 import PdfFileReader
from edit_document import EditDocumentDialog
from edit_author import EditAuthorDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.library_name = ''
        self.library_root = ''
        self.author_model = QStandardItemModel()
        self.categories_model = QStandardItemModel()
        self.documents_model = QStandardItemModel()
        self.left_model = QStandardItemModel()

        self.session_maker = sessionmaker()
        self.session = None
        self.ui.lstLeftPane.setModel(self.left_model)

    def setup_actions(self):

        self.ui.actionNew.triggered.connect(self.create_new_library)
        self.ui.actionOpen.triggered.connect(self.open_library)
        self.ui.actionExit.triggered.connect(QApplication.instance().quit)
        self.ui.tblRightPane.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tblRightPane.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lstLeftPane.clicked[QModelIndex].connect(self.select_left_pane)

        self.ui.actionAdd_author.triggered.connect(self.add_author)

    def create_new_library(self):

        library_name, ok = QInputDialog.getText(self, 'Library name', 'Enter the name of the library:')
        if ok:
            library_root = QFileDialog.getExistingDirectory(self, 'Select library root', '/home')
            if library_root:
                self.library_name = library_name
                self.library_root = library_root

                engine = create_engine('sqlite:///libraries/{}.db'.format(library_name), echo=True)
                engine.connect()

                models.Base.metadata.create_all(engine)
                self.session_maker.configure(bind=engine)
                self.session = self.session_maker()

                self.build_lib_from_root()

                self.left_model.appendRow(QStandardItem('Documents'))
                self.left_model.appendRow(QStandardItem('Authors'))
                self.left_model.appendRow(QStandardItem('Categories'))

    def open_library(self):
        library_path, file_filter = QFileDialog.getOpenFileName(self, 'Select library', './libraries')
        if library_path:
            self.library_name = os.path.split(library_path)[-1]
            self.library_root = os.path.split(library_path)[0]
            engine = create_engine('sqlite:///{}'.format(library_path))
            engine.connect()
            self.session_maker.configure(bind=engine)
            self.session = self.session_maker()

            self.left_model.appendRow(QStandardItem('Documents'))
            self.left_model.appendRow(QStandardItem('Authors'))
            self.left_model.appendRow(QStandardItem('Categories'))

    def build_lib_from_root(self, interactive=True):

        for root, dirs, files in os.walk(self.library_root):
            for f in files:
                if f.endswith('.pdf'):
                    full_path = os.path.join(root, f)
                    pdf = PdfFileReader(open(full_path, 'rb'))
                    meta = pdf.getDocumentInfo()
                    author = str(meta.get('/Author', ''))
                    title = str(meta.get('/Title'))
                    # keywords = str(meta.get('/Keywords')).split(',')

                    new_document = models.Document(name=title, path=full_path)
                    if author != '':
                        author_names = author.split()
                    else:
                        author_names = ['', '']
                    new_author = models.Author(first_name=author_names[0], last_name=author_names[-1])
                    self.session.add(new_document)
                    self.session.add(new_author)
                    self.session.commit()

                    new_document.authors.append(new_author)
                    new_author.documents.append(new_document)

                    self.session.commit()

    def select_left_pane(self, selection):

        if selection.data() == 'Documents':
            self.populate_documents()
        elif selection.data() == 'Authors':
            self.populate_authors()

    def populate_documents(self):

        all_docs = self.session.query(models.Document).all()
        self.documents_model.clear()
        self.documents_model.setHorizontalHeaderLabels(['Title', 'Authors', 'Path'])
        self.ui.tblRightPane.horizontalHeader().setStretchLastSection(True)
        for i, doc in enumerate(all_docs):
            name = QStandardItem(doc.name)
            path = QStandardItem(doc.path)
            authors = [str(author) for author in doc.authors]
            sorted_authors = ';'.join(sorted(authors))
            auth = QStandardItem(sorted_authors)
            name.setData(doc.id)
            self.documents_model.setItem(i, 0, name)
            self.documents_model.setItem(i, 1, auth)
            self.documents_model.setItem(i, 2, path)

        self.ui.tblRightPane.setModel(self.documents_model)
        self.ui.tblRightPane.disconnect()
        self.ui.tblRightPane.customContextMenuRequested.connect(partial(self.table_right_click, 'document'))

    def populate_authors(self):

        all_authors = self.session.query(models.Author).all()
        self.author_model.clear()
        self.author_model.setHorizontalHeaderLabels(['Last name', 'First name', 'Middle name(s)'])
        self.ui.tblRightPane.horizontalHeader().setStretchLastSection(True)
        for i, author in enumerate(all_authors):
            last_name = QStandardItem(author.last_name)
            first_name = QStandardItem(author.first_name)
            middle_name = QStandardItem(author.middle_name)
            last_name.setData(author.id)
            self.author_model.setItem(i, 0, last_name)
            self.author_model.setItem(i, 1, first_name)
            self.author_model.setItem(i, 2, middle_name)

        self.ui.tblRightPane.setModel(self.author_model)
        self.ui.tblRightPane.disconnect()
        self.ui.tblRightPane.customContextMenuRequested.connect(partial(self.table_right_click, 'author'))

    def table_right_click(self, row_type):

        menu = QMenu(self)
        edit_action = QAction('Edit', self)
        edit_action.triggered.connect(partial(self.edit_row, row_type))
        menu.addAction(edit_action)
        delete_action = QAction('Delete', self)
        if row_type == 'document':
            rename_action = QAction('Rename', self)
            rename_action.triggered.connect(self.rename_document)
            open_action = QAction('Open in viewer', self)
            open_action.triggered.connect(self.open_doc_in_viewer)
            menu.addAction(open_action)
            menu.addAction(rename_action)
        if row_type == 'author':
            delete_action.triggered.connect(self.delete_authors)
        menu.addAction(delete_action)
        menu.popup(QCursor.pos())

    def edit_row(self, row_type):

        selection = self.ui.tblRightPane.selectionModel().selectedRows()

        if row_type == 'document':

            for row in selection:
                name = self.documents_model.item(row.row(), 0)
                doc_id = name.data()
                dialog = EditDocumentDialog(doc_id, parent=self)
                result = dialog.exec_()

                if result == 1:
                    #TODO: Don't redraw the whole table, just update the row
                    self.populate_documents()

        elif row_type == 'author':

            for row in selection:
                last_name = self.author_model.item(row.row(), 0)
                author_id = last_name.data()
                dialog = EditAuthorDialog(author_id, parent=self)
                result = dialog.exec_()

                if result:
                    self.populate_authors()

    def rename_document(self):

        print 'rename'

    def open_doc_in_viewer(self):

        selection = self.ui.tblRightPane.selectionModel().selectedRows()
        for row in selection:
            path = self.documents_model.item(row.row(), 2).text()
            if os.path.exists(path):
                QDesktopServices.openUrl(QUrl.fromLocalFile(path))

    def add_author(self):

        dialog = EditAuthorDialog(None, parent=self)
        result = dialog.exec_()

        if result:
            self.populate_authors()

    def delete_authors(self):

        result = QMessageBox.question(self, 'Delete authors',
                                      'Are you sure you want to delete the selected authors from the library?')

        if result == QMessageBox.Yes:
            selection = self.ui.tblRightPane.selectionModel().selectedRows()
            ids_to_delete = [self.author_model.item(row.row(), 0).data() for row in selection]
            authors_to_delete = self.session.query(models.Author).filter(models.Author.id.in_(ids_to_delete))
            for auth in authors_to_delete:
                self.session.delete(auth)
            self.session.commit()
            for row in selection:
                self.author_model.removeRow(row.row())