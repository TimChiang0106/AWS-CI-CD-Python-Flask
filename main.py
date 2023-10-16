import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello Production {}!".format(name)


@app.route("/post", methods=['POST'])
def post_test():
    cookie = request.values['cookie']
    return "Hello Production {}!".format(cookie)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=int(os.environ.get("PORT", 8080)))
