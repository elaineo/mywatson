import os
from flask import Flask
from flask import render_template
from flask import jsonify
#from similarity import find_bot
import json


PORT = int(os.getenv('VCAP_APP_PORT', '8000'))


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('personality.html')


@app.route("/chat")
def chat():
    return render_template('chat.html')

# @app.route("/search")
# def search():
#     data = request.data
#     data = json.loads(data)
#     return find_bot(data.get("personality"))

@app.route("/meet")
def meet():
    return render_template('meet.html')


if __name__ == "__main__":
    app.run(port=PORT)
