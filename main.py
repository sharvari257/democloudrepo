import os

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello from Gcloud Editor'

if __name__ == '_main_':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))