from flask import Flask
from utils import greetings

app = Flask(__name__)

@app.route("/")
def hello():
    message = 'Hello from Flask Python! ' 
    return message + greetings('main.py')

@app.route("/endpoint")
def hello_endpoint():
    message = 'Hello From Another EndPoint! ' 
    return message + greetings('main.py')
