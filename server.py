from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get('http://127.0.0.1:8000')
    print(r.text)
    return "pong"

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5000)

