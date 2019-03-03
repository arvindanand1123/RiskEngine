from flask import Flask
from flask import request
import os
import json
import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getPrediction', methods=['POST'])
def getPrediction():
    if request.method == 'POST':
        f = request.form
        mock = [70,72]
        return render_template("result.html",result = mock)
    else:
        return "POST Failed"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 2222)
