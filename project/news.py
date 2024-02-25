import sqlite3
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///news.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


@app.route("/add_news", methods=["POST"])
def add_news():
    title = request.form["title"]
    content = request.form["content"]
    th_news = Article(
        title=title,
        content=content,
        )
    db.session.add(th_news)
    db.session.commit()
    return redirect("/")

@app.route("/")
@app.route("/main")
def main():
    news = Article.query.all()
    print(news)
    return render_template("main.html", news=news)

@app.route("/add_news")
def new_article():
    return render_template("add_news.html")

@app.route("/admin_menu")
def admin_menu():
    return render_template("admin.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)