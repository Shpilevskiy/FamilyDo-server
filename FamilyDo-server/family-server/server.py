from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "<b>Adventure has <i>begun</i>!</b>"

if __name__ == "__main__":
    app.run()