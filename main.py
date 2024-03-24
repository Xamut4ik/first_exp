from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///forum.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    posts = db.relationship("Post", backref="author")  # uselist=False потрібен для One-to-One


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))


@app.route("/")
def index():
    return "Зроз"

def fill_database():
    data = [
        {"name": "Anotoliy Vasormanovich", "text": "said right foot creep, ooh, I'm walking with that heater",},
        {"name": "Alexandr Bebrosovich", "text": "Kirill is finding boyfriend"},
        {"name": "Artur Neptunov ", "text": "Why are bulling little bober"},
    ]
    for pair in data:
        user = User(name=pair["name"])
        db.session.add(user)
        post = Post(text=pair["text"], author=user)
        db.session.add(post)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # fill_database()
    app.run(debug=True)