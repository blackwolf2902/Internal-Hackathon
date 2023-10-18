from flask import Flask, render_template, request, jsonify
from train import train_model
from chat import get_input
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_input(input)


def build():
    print("initailize model")
    train_model()

if __name__ == '__main__':
    build()
    app.run()