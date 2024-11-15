# to run this, set up Flask with 
# https://flask.palletsprojects.com/en/stable/installation/
# and then run:
# $ python -m flask --app hello run
from flask import Flask

# indicates the name of the .py
app = Flask(__name__)

# url of the website is website.com/ <-- / is the same as "/"
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"