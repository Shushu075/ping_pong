from flask import Flask
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    r = requests.post('http://127.0.0.1:2000/serveur', data="http://127.0.0.1:5000")
    receive = r.text

    if receive is not None:
        request = requests.get(receive)
        print(request.text)
        return "pong"
    else:
        return ""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
