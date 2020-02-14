from flask import Flask
import requests

app = Flask(__name__)


# serveur 1 retourne une reponse
# serveur 2 retourne une reponse

@app.route('/serveur')
def sendOne():
    return 'http://127.0.0.1:8000'


@app.route('/client')
def sendTwo():
    return 'http://127.0.0.1:5000'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2000)
