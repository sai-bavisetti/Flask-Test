from flask import Flask

app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def hello_world():
    return "Its Working do next !!"