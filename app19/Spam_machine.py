from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/spam/<string:text>/<int:count>")
def spam(text="spam ", count=10):
    x = text * count
    return x

#def
if __name__ == "__main__":
    app.run(debug=True)