import models

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from ui_edit_author_dialog import Ui_EditAuthorDialog


class EditAuthorDialog(QDialog):

    def __init__(self, author_id, parent=None):
        super(EditAuthorDialog, self).__init__(parent)

        self.ui = Ui_EditAuthorDialog()
        self.ui.setupUi(self)

        if author_id:
            self.id = author_id
            self.fetch_from_db()
        else:
            self.id = None
            self.author = models.Author()

        self.accepted.connect(self.save_to_db)

    def fetch_from_db(self):

        self.author = self.parent().session.query(models.Author).filter(models.Author.id == self.id).one()
        self.ui.txtFirstName.setText(self.author.first_name)
        self.ui.txtMiddleName.setText(self.author.middle_name)
        self.ui.txtLastName.setText(self.author.last_name)

    def save_to_db(self):

        if not self.id:
            self.parent().session.add(self.author)

        self.author.first_name = self.ui.txtFirstName.text()
        self.author.middle_name = self.ui.txtMiddleName.text()
        self.author.last_name = self.ui.txtLastName.text()

        self.parent().session.commit()
