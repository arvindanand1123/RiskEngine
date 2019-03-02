from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Prediction'

@app.route('/getPrediction', methods=['POST'])
def getPrediction():
    if request.method == 'POST':
        f = request.form
        return f
    else:
        return "POST Failed"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 2222)
