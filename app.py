# to run this, set up Flask with 
# https://flask.palletsprojects.com/en/stable/installation/
# and then run:
# $ python -m flask run
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    dfs_result = bfs_result = None
    if request.method == "POST":
        if "dfs_submit" in request.form:
            start = request.form.get("dfs_start")
            end = request.form.get("dfs_end")
            dfs_result = f"Finding a path from {start} to {end}..."
        elif "bfs_submit" in request.form:
            start = request.form.get("bfs_start")
            end = request.form.get("bfs_end")
            bfs_result = f"Finding a path from {start} to {end}..."
    return render_template("app.html", dfs_result=dfs_result, bfs_result=bfs_result)

if __name__ == "__main__":
    app.run(debug=True)
