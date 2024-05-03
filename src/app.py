import os
from flask import Flask, render_template, send_file, request
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Serve on localhost, forward traffic with nginx
    serve(app, host='127.0.0.1', port=8000)
