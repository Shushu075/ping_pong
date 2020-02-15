from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    r = requests.get('http://127.0.0.1:2000/client', data="http://127.0.0.1:8000")
    receive = r.text

    if receive is not None:
        request = requests.get(receive)
        print(request.text)
        return "ping"
    else:
        return ""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
