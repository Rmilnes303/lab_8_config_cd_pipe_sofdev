from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Calculator App</h1><p>Try /add/2/3</p>"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return {"operation": "add", "a": a, "b": b, "result": a + b}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
