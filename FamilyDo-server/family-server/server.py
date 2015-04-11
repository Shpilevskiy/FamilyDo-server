from flask import Flask, render_template, url_for, flash, redirect, request, session, abort
from sqlalchemy.orm import sessionmaker
from tabledef import *
from collections import namedtuple
import os

engine = create_engine("sqlite:///tutorial.db", echo=True)
app = Flask(__name__)


class Notebook(object):

    def __init__(self):
        self.notes = []
        self.last_id = 0

    def add_note(self, note):
        self.notes.append(note)
        note.id = self.last_id
        self.last_id += 1

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        raise ValueError("No note with id {}!".format(note_id))


class Note(object):

    def __init__(self, text, author):
        self.text = text
        self.author = author

    def render_to_html(self):
        return """
<b>Author: </b> {name} 
<br>
<b>Text: </b>{text}
""".format(name=self.author, text=self.text)


@app.route("/note/<int:note_id>")
def show_note(note_id):
    note = notebook.get_note_by_id(note_id)
    return render_template("note.html", author=note.author, text=note.text)


@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return "Hello, user.<a href='/logout'>Logout</a>"


class Test:
    def __init__(self, name, text):
        self.name = name
        self.text = text


@app.route("/notes")
def show_notes_page():
    print("Check!")
    Note_Test = namedtuple('Note_Test', ['author', 'note_text'])
    print(Note_Test("Andrew", "Some random note.").author)
    Session = sessionmaker(bind=engine)
    s = Session()
    print(s.query(TODO_List_Entry))
    notes = [Note_Test(note.author, note.note_text) for note in s.query(TODO_List_Entry).order_by(TODO_List_Entry.id)]
    
    print(notes)
    return render_template("notes.html", notes=notes)


@app.route("/login", methods=['POST'])
def do_admin_login():
    print("TEST_DEBUG!")
    POST_USERNAME = str(request.form["username"])
    POST_PASSWORD = str(request.form["password"])
    print("Login is here!")
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    print(result)
    if result:
        session["logged_in"] = True
    else:
        print("Wrong pass")
        flash("Wrong password.")

    return home()


@app.route("/test_post", methods=['POST', 'GET'])
def test_post():
    note_text = request.args.get("note_text")
    author = request.args.get("author")
    Session = sessionmaker(bind=engine)
    s = Session()
    note = TODO_List_Entry(author, note_text)
    s.add(note)
    s.commit()
    # print(note)


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    # notebook = Notebook()
    # notebook.add_note(Note("Some text", "MrLokans"))
    # notebook.add_note(Note("Another text", "Arararat"))

    app.run()
