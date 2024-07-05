from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/person', methods=['POST'])
def create_person():
    body = request.get_json()
    return body


app.run(host='0.0.0.0', port=8080)