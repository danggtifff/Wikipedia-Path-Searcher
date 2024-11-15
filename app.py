# to run this, set up Flask with 
# https://flask.palletsprojects.com/en/stable/installation/
# and then run:
# $ python -m flask run
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        start = request.form.get("start")
        end = request.form.get("end")
        # Add code here to perform the "degrees of separation" calculation.
        result = f"Finding shortest paths from {start} to {end}..."
        return render_template("index.html", result=result, start=start, end=end)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
