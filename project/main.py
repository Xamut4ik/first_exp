import sqlite3
from flask import Flask, render_template, request, redirect, url_for, make_response, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///news.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "abcefgabcdefg1234567890"
db = SQLAlchemy(app)
way = "C:/Users/leono/PycharmProjects/first_exp/project/instance/news.db"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.Text, nullable=False)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route("/")
@app.route("/index")
def index():
    news = Article.query.all()
    if "username" in session:
        user = User.query.filter_by(username=session["username"]).first()
        if user:
            return render_template("index.html", news=news, user=user)
    return render_template("index.html", news=news)


@app.route("/login",  methods=["GET", "POST"])
def login():
    if "username" in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        if "login" in request.form and "password" in request.form:  # якщо у формі запиту є логін  і пароль
            username = request.form["login"]
            password = request.form["hashedPassword"]
            user = User.query.filter_by(username=username).first()
            if user:
                if password in user.password:  # перевіряємо чи співпадають дані
                    session["username"] = username
                    return redirect(url_for("index"))
            return render_template("login.html", error="Невірний пароль або ім'я користувача")
    return render_template("login.html", error=None)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/new_article", methods=["GET", "POST"])
def new_article():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        th_news = Article(
            title=title,
            content=content,
        )
        db.session.add(th_news)
        db.session.commit()
        return redirect("/")
    return render_template("new_article.html")


@app.route("/delete-article/<int:_id>")
def delete_article(_id):
    print("Видаляємо статтю з ІД", _id)
    conn = sqlite3.connect(way)
    c = conn.cursor()
    c.execute(f'DELETE FROM article WHERE id = {_id}')
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
