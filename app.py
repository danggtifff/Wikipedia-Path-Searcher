# to run this, set up Flask with 
# https://flask.palletsprojects.com/en/stable/installation/
# and then run:
# $ python -m flask run
from flask import Flask, render_template, request
#from waitress import serve
import algs, db

DATABASE = 'data/wikilinks.db'
app = Flask(__name__)
app.config.from_object(__name__)
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def main():
    dfs_result = bfs_result = None
    if request.method == "POST":
        if "dfs_submit" in request.form:
            start = request.form.get("dfs_start")
            end = request.form.get("dfs_end")
            dfs_result = f"Finding a path from {start} to {end}..."
            path = algs.iddfs(start, end, 10000)
            print(path)
        elif "bfs_submit" in request.form:
            start = request.form.get("bfs_start")
            end = request.form.get("bfs_end")
            bfs_result = f"Finding a path from {start} to {end}..."
            path = algs.bfs(start, end)
            print(path)
    return render_template("app.html", dfs_result=dfs_result, bfs_result=bfs_result)

if __name__ == "__main__":
    app.run(debug=True)
   
