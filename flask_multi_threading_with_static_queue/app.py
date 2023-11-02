from flask import Flask, make_response, request
from store_messages import StoreMessages
from datetime import datetime


app = Flask(__name__)


@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def printmessage():
    req_data = request.data.decode("utf-8")

    storeMessages = StoreMessages()
    storeMessages.add_message(req_data)

    resp = make_response("", 200)
    return resp
