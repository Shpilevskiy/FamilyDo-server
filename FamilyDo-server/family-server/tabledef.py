from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tutorial.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class TODO_List_Entry(Base):
    __tablename__ = "todo_lists_entries"

    id = Column(Integer, primary_key=True)
    author = Column(String)
    note_text = Column(String)

    def __init__(self, author, note_text):
        self.author = author
        self.note_text = note_text


Base.metadata.create_all(engine)