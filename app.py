from flask import Flask, render_template, request
import time
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
            start_time = time.time()
            path = algs.iddfs(start, end, 10000)
            elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            dfs_result = f"{dfs_result}... took {elapsed_time:.2f} ms"
            print(path)
        elif "bfs_submit" in request.form:
            start = request.form.get("bfs_start")
            end = request.form.get("bfs_end")
            bfs_result = f"Finding a path from {start} to {end}..."
            start_time = time.time()
            path = algs.bfs(start, end)
            elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            bfs_result = f"{bfs_result}... took {elapsed_time:.2f} ms"
            print(path)
    
    return render_template("app.html", dfs_result=dfs_result, bfs_result=bfs_result)

if __name__ == "__main__":
    app.run(debug=True)
