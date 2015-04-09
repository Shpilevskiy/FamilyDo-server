from flask import Flask, render_template, url_for
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
def hello():
    pass
    # return a1.render_to_html()

if __name__ == "__main__":
    notebook = Notebook()
    notebook.add_note(Note("Some text", "MrLokans"))
    notebook.add_note(Note("Another text", "Arararat"))

    app.run()
