from flask import Flask
import requests
from flask import request

app = Flask(__name__)

adressOne = None
adressTwo = None


@app.route('/serveur', methods=['GET', 'POST'])
def receiveOne():
    global adressOne
    adressOne = request.data.decode('utf-8')
    return adressTwo


@app.route('/client', methods=['GET', 'POST'])
def receiveTwo():
    global adressTwo
    adressTwo = request.data.decode('utf-8')
    return adressOne


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2000)
