# to run this, set up Flask with 
# https://flask.palletsprojects.com/en/stable/installation/
# and then run:
# $ python -m flask run
from flask import Flask

app = Flask(__name__)

@app.route("/")

def main():
    return "<p>Hello World!</p>"