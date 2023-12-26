from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/secret")
def secret():
    return render_template("secret file.html")

if __name__ == "__main__":
    app.run(debug=True)

