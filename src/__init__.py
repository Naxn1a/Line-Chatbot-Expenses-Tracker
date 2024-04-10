from flask import Flask, request
from src.bot import bot

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Python"


@app.route("/line-webhook", methods=["POST", "GET"])
def line_webhook():
    if request.method == "POST":
        payload = request.json
        if payload["events"]:
            bot(payload["events"][0])
        return request.json, 200
    elif request.method == "GET":
        return {"msg": "ok"}, 200
