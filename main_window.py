import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import models

from functools import partial

from PyQt5.QtWidgets import (QMainWindow, QInputDialog, QFileDialog, QProgressDialog,
                             QApplication, QMenu, QAction, QAbstractItemView,
                             QMessageBox)
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QCursor, QDesktopServices
from PyQt5.QtCore import QModelIndex, Qt, QUrl
from ui_main_window import Ui_MainWindow
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from PyPDF2 import PdfFileReader
from PyPDF2.utils import PdfReadError
from edit_document import EditDocumentDialog
from edit_author import EditAuthorDialog
from rename_document import RenameDocumentDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.library_name = None
        self.library_root = None
        self.author_model = QStandardItemModel()
        self.categories_model = QStandardItemModel()
        self.documents_model = QStandardItemModel()
        self.left_model = QStandardItemModel()

        self.session_maker = sessionmaker()
        self.session = None
        self.ui.lstLeftPane.setModel(self.left_model)

        if not os.path.exists(os.path.abspath('./tmp')):
            os.mkdir(os.path.abspath('./tmp'))

    def setup_actions(self):

        self.ui.actionNew.triggered.connect(self.create_new_library)
        self.ui.actionOpen.triggered.connect(self.open_library)
        self.ui.actionExit.triggered.connect(QApplication.instance().quit)
        self.ui.tblRightPane.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tblRightPane.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.lstLeftPane.clicked[QModelIndex].connect(self.select_left_pane)

        self.ui.actionAdd_author.triggered.connect(self.add_author)
        self.ui.actionAdd_category.triggered.connect(self.add_category)
        # self.ui.actionAdd_paper.triggered.connect(self.add)
        self.ui.actionEdit_paper.triggered.connect(partial(self.edit_row, 'document'))
        self.ui.actionEdit_category.triggered.connect(partial(self.edit_row, 'category'))
        self.ui.actionEdit_author.triggered.connect(partial(self.edit_row, 'author'))

    def create_new_library(self):

        library_name, ok = QInputDialog.getText(self, 'Library name', 'Enter the name of the library:')
        if ok:
            library_root = QFileDialog.getExistingDirectory(self, 'Select library root', '/home')
            if library_root:
                self.library_name = library_name
                self.library_root = library_root

                if not os.path.exists(os.path.abspath('./libraries')):
                    os.mkdir(os.path.abspath('./libraries'))

                engine = create_engine('sqlite:///libraries/{}.db'.format(library_name), echo=False)
                engine.connect()

                models.Base.metadata.create_all(engine)
                self.session_maker.configure(bind=engine)
                self.session = self.session_maker()

                self.build_lib_from_root()

                self.left_model.clear()
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

            self.left_model.clear()
            self.left_model.appendRow(QStandardItem('Documents'))
            self.left_model.appendRow(QStandardItem('Authors'))
            self.left_model.appendRow(QStandardItem('Categories'))
            self.documents_model.clear()
            self.author_model.clear()
            self.categories_model.clear()

    def build_lib_from_root(self, interactive=True):

        total_files = 0
        for root, dirs, files in os.walk(self.library_root):
            total_files += len([f for f in files if f.endswith('.pdf')])

        process_files = True
        if total_files > 100:
            result = QMessageBox.question(self, 'Import files',
                                          'This will import {} files into the library, '
                                          'which can take a long time. Are you sure?'.format(total_files))
            if result:
                process_files = True
            else:
                process_files = False

        if process_files:
            progress = QProgressDialog('Importing files', 'Abort import', 0, total_files)
            progress.setWindowModality(Qt.WindowModal)
            current_file = 0
            # progress.show()
            for root, dirs, files in os.walk(self.library_root):
                if progress.wasCanceled():
                    break
                for f in files:
                    if f.endswith('.pdf'):
                        full_path = os.path.join(root, f)
                        try:
                            pdf = PdfFileReader(open(full_path, 'rb'))
                            meta = pdf.getDocumentInfo()
                            if meta:
                                author = unicode(meta.get('/Author', ''))
                                title = unicode(meta.get('/Title'))
                            else:
                                author = ''
                                title = None
                        except PdfReadError:
                            author = ''
                            title = None
                        except Exception:
                            author = ''
                            title = None
                        # keywords = str(meta.get('/Keywords')).split(',')

                        new_document = models.Document(name=title, path=full_path)
                        if author != '':
                            author_names = author.split()
                            if len(author_names) == 0:
                                author_names = ['', '']
                            existing_author = self.session.query(models.Author).filter(
                                    models.Author.first_name == author_names[0]
                                    and models.Author.last_name == author_names[-1]
                            ).first()
                            if existing_author:
                                new_author = existing_author
                            else:
                                new_author = models.Author(first_name=author_names[0], last_name=author_names[-1])
                        else:
                            new_author = None

                        self.session.add(new_document)
                        if new_author:

                            self.session.add(new_author)
                        self.session.commit()

                        if new_author:
                            new_document.authors.append(new_author)
                            new_author.documents.append(new_document)

                        self.session.commit()
                        current_file += 1
                        progress.setValue(current_file)

    def select_left_pane(self, selection):

        if selection.data() == 'Documents':
            self.populate_documents()
        elif selection.data() == 'Authors':
            self.populate_authors()
        elif selection.data() == 'Categories':
            self.populate_categories()

    def populate_documents(self):

        all_docs = self.session.query(models.Document).all()
        self.documents_model.clear()
        self.documents_model.setHorizontalHeaderLabels(['Title', 'Authors', 'Categories', 'Path'])
        self.ui.tblRightPane.horizontalHeader().setStretchLastSection(True)
        for i, doc in enumerate(all_docs):
            self.populate_document_row(i, doc)

        self.ui.tblRightPane.setModel(self.documents_model)
        self.ui.tblRightPane.disconnect()
        self.ui.tblRightPane.customContextMenuRequested.connect(partial(self.table_right_click, 'document'))
        self.ui.tblRightPane.resizeRowsToContents()

    def populate_document_row(self, row, doc):
        name = QStandardItem(doc.name)
        path = QStandardItem(doc.path)
        authors = [str(author) for author in doc.authors]
        sorted_authors = '\n'.join(sorted(authors))
        auth = QStandardItem(sorted_authors)
        categories = [str(cat) for cat in doc.categories]
        sorted_cat = ', '.join(sorted(categories))
        cats = QStandardItem(sorted_cat)
        name.setData(doc.id)
        self.documents_model.setItem(row, 0, name)
        self.documents_model.setItem(row, 1, auth)
        self.documents_model.setItem(row, 2, cats)
        self.documents_model.setItem(row, 3, path)

    def populate_authors(self):

        all_authors = self.session.query(models.Author).order_by(models.Author.last_name.asc())
        self.author_model.clear()
        self.author_model.setHorizontalHeaderLabels(['Last name', 'First name', 'Middle name(s)'])
        self.ui.tblRightPane.horizontalHeader().setStretchLastSection(True)
        for i, author in enumerate(all_authors):
            self.populate_author_row(i, author)

        self.ui.tblRightPane.setModel(self.author_model)
        self.ui.tblRightPane.disconnect()
        self.ui.tblRightPane.customContextMenuRequested.connect(partial(self.table_right_click, 'author'))
        self.ui.tblRightPane.resizeRowsToContents()

    def populate_author_row(self, row, author):

        last_name = QStandardItem(author.last_name)
        first_name = QStandardItem(author.first_name)
        middle_name = QStandardItem(author.middle_name)
        last_name.setData(author.id)
        self.author_model.setItem(row, 0, last_name)
        self.author_model.setItem(row, 1, first_name)
        self.author_model.setItem(row, 2, middle_name)

    def populate_categories(self):

        all_categories = self.session.query(models.Category).all()
        self.categories_model.clear()
        self.categories_model.setHorizontalHeaderLabels(['Category'])
        self.ui.tblRightPane.horizontalHeader().setStretchLastSection(True)
        for i, cat in enumerate(all_categories):
            cat_item = QStandardItem(str(cat))
            cat_item.setData(cat)
            self.categories_model.appendRow(cat_item)

        self.ui.tblRightPane.setModel(self.categories_model)
        self.ui.tblRightPane.disconnect()
        self.ui.tblRightPane.customContextMenuRequested.connect(partial(self.table_right_click, 'category'))
        self.ui.tblRightPane.resizeRowsToContents()

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
        elif row_type == 'author':
            delete_action.triggered.connect(self.delete_authors)
        elif row_type == 'category':
            delete_action.triggered.connect(self.delete_categories)

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

                if result:
                    # doc = self.session.query(models.Document).filter(models.Document.id == doc_id).one()
                    self.populate_document_row(row.row(), dialog.doc)

        elif row_type == 'author':

            for row in selection:
                last_name = self.author_model.item(row.row(), 0)
                author_id = last_name.data()
                dialog = EditAuthorDialog(author_id, parent=self)
                result = dialog.exec_()

                if result:
                    self.populate_author_row(row.row(), dialog.author)

        elif row_type == 'category':

            for row in selection:
                cat_item = self.categories_model.item(row.row())
                cat = cat_item.data()
                new_cat_name, ok = QInputDialog.getText(self, 'Category name',
                                                        'Enter the new name of the category', text=str(cat))
                if ok:
                    cat.name = new_cat_name
                    self.session.add(cat)

            self.session.commit()
            self.populate_categories()

    def rename_document(self):

        selection = self.ui.tblRightPane.selectionModel().selectedRows()
        dialog = RenameDocumentDialog(self)
        result = dialog.exec_()
        if result:
            format_string = dialog.ui.txtNameFormat.text()
            try:
                for row in selection:
                    doc_id = self.documents_model.item(row.row(), 0).data()
                    doc = self.session.query(models.Document).filter(models.Document.id == doc_id).one()
                    path = doc.path
                    format_dict = {}
                    if '{last_name}' in format_string and len(doc.authors) > 0:
                        format_dict['last_name'] = doc.authors[0].last_name
                    if '{first_name}' in format_string and len(doc.authors) > 0:
                        format_dict['first_name'] = doc.authors[0].first_name
                    if '{author}' in format_string and len(doc.authors) > 0:
                        format_dict['author'] = str(doc.authors[0])
                    if '{authors_last_names}' in format_string:
                        format_dict['authors_last_names'] = ', '.join([auth.last_name for auth in doc.authors])
                    if '{authors}' in format_string:
                        format_dict['authors'] = '; '.join([str(auth).strip() for auth in doc.authors])
                    if '{title}' in format_string:
                        format_dict['title'] = doc.name
                    if '{categories}' in format_string:
                        format_dict['categories'] = ', '.join([str(cat).strip() for cat in doc.categories])

                    new_file_name = format_string.format(**format_dict)
                    articles = ['The ', 'the ', 'a ', 'A ', 'an ', 'An ']
                    for article in articles:
                        if new_file_name.startswith(article):
                            rest = new_file_name[:len(article)]
                            new_file_name = rest + ', ' + article

                    location = os.path.split(path)[0]
                    new_location = os.path.join(location, new_file_name)
                    if not new_location.endswith('.pdf') or new_location.endswith('.PDF'):
                        new_location += '.pdf'
                    if os.path.exists(new_location):
                        result = QMessageBox.question(self, 'File exists', 'A file named {} already exists. Overwrite?'.format(new_location))
                        if result:
                            os.rename(path, new_location)
                    else:
                        os.rename(path, new_location)
                    doc.path = new_location
                    self.session.add(doc)
                    self.session.commit()
                    self.populate_document_row(row.row(), doc)

            except KeyError as ex:
                QMessageBox.warning(self, 'Error!', '{} is not a valid interpolation term!'.format(ex.message))

    def open_doc_in_viewer(self):

        selection = self.ui.tblRightPane.selectionModel().selectedRows()
        for row in selection:
            path = self.documents_model.item(row.row(), 3).text()
            #print path
            if os.path.exists(path):
                QDesktopServices.openUrl(QUrl.fromLocalFile(path))

    def add_author(self):

        dialog = EditAuthorDialog(None, parent=self)
        result = dialog.exec_()

        if result:
            self.populate_author_row(self.author_model.rowCount(), dialog.author)

    def add_category(self):

        category, ok = QInputDialog.getText(self, 'Category name', 'Enter the name of the category:')
        if ok:
            cat = models.Category()
            cat.name = category
            self.session.add(cat)
            self.session.commit()

            self.populate_categories()

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

    def delete_categories(self):

        result = QMessageBox.question(self, 'Delete categories',
                                      'Are you sure you want to delete the selected categories from the library?')

        if result == QMessageBox.Yes:
            selection = self.ui.tblRightPane.selectionModel().selectedRows()
            ids_to_delete = [self.categories_model.item(row.row(), 0).data().id for row in selection]
            categories_to_delete = self.session.query(models.Category).filter(models.Category.id.in_(ids_to_delete))
            for cat in categories_to_delete:
                self.session.delete(cat)
            self.session.commit()
            for row in selection:
                self.categories_model.removeRow(row.row())