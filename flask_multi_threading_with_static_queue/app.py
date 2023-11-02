from flask import Flask, make_response, request
from store_messages import StoreMessages
from datetime import datetime


app = Flask(__name__)


@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def printmessage():
    # now = datetime.now()
    # start_time = now.strftime("%m/%d/%Y, %H:%M:%S.%f")
    # print(start_time)
    req_data = request.data.decode("utf-8")

    storeMessages = StoreMessages()
    storeMessages.add_message(req_data)

    # print(request.args.get("a"))

    # now = datetime.now()
    # end_time = now.strftime("%m/%d/%Y, %H:%M:%S.%f")
    # print(f"end: {end_time}")

    resp = make_response("hello world\n", 200)
    return resp
