from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, Table, Date
from sqlalchemy.orm import relationship

Base = declarative_base()


author_documents = Table('author_documents', Base.metadata,
                         Column('author_id', ForeignKey('authors.id'), primary_key=True),
                         Column('document_id', ForeignKey('documents.id'), primary_key=True))

document_categories = Table('document_categories', Base.metadata,
                            Column('document_id', ForeignKey('documents.id'), primary_key=True),
                            Column('category_id', ForeignKey('categories.id'), primary_key=True))

document_publishers = Table('document_publishers', Base.metadata,
                            Column('document_id', ForeignKey('documents.id'), primary_key=True),
                            Column('publisher_id', ForeignKey('publishers.id'), primary_key=True))

document_journals = Table('document_journals', Base.metadata,
                          Column('document_id', ForeignKey('documents.id'), primary_key=True),
                          Column('journal_id', ForeignKey('journals.id'), primary_key=True))


class Document(Base):

    __tablename__ = 'documents'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(500))
    path = Column(String(1000))

    authors = relationship('Author', secondary=author_documents, back_populates='documents')
    categories = relationship('Category', secondary=document_categories, back_populates='documents')
    publisher = relationship('Publisher', secondary=document_publishers, back_populates='documents')


class Author(Base):

    __tablename__ = 'authors'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    middle_name = Column(String(250))

    documents = relationship('Document', secondary=author_documents, back_populates='authors')

    def __str__(self):
        # return '<Author id={}, first_name={}, last_name={}>'.format(self.id, self.first_name, self.last_name)
        return '{}, {} {}'.format(self.last_name or '', self.first_name or '', self.middle_name or '')


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(250))

    documents = relationship('Document', secondary=document_categories, back_populates='categories')

    def __str__(self):
        return self.name


class Publisher(Base):

    __tablename__ = 'publishers'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(250))

    documents = relationship('Document', secondary=document_publishers, back_populates='publisher')

    def __str__(self):
        return self.name


class Journal(Base):

    __tablename__ = 'journals'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(250))

    documents = relationship('Document', secondary=document_publishers, back_populates='publisher')

    def __str__(self):
        return self.name