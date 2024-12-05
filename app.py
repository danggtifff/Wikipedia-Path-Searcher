from flask import Flask, render_template, request, session, jsonify
import time
import algs, db, visualize
import os

DATABASE = 'data/wikilinks.db'
app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config.from_object(__name__)
db.init_app(app)

@app.route("/", methods=["GET"])
def main():
    # Initialize session variables if they don't exist
    if "dfs_result" not in session:
        session["dfs_result"] = ""
    if "bfs_result" not in session:
        session["bfs_result"] = ""

    # renders the website
    return render_template(
        "app.html",
        dfs_result=session.get("dfs_result"),
        bfs_result=session.get("bfs_result")
    )

@app.route("/dfs", methods=["POST"])
def dfs():
    start = request.form.get("dfs_start")
    end = request.form.get("dfs_end")

    # message displays when we get POST
    initial_message = f"Finding a path from {start} to {end}..."
    # update message
    session["dfs_result"] = initial_message

    # run and time the iddfs alg
    start_time = time.time()
    path = algs.iddfs(start, end, 10000)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds

    final_message = f"{initial_message}... took {elapsed_time:.2f} ms\nPath: {path}"
    session["dfs_result"] = final_message

    # Generate the graph and save it as an image
    if path:
        image_filename = "static/graph.png"
        G = visualize.get_graph_with_path(path)
        visualize.visualize_graph_with_path(G, path, image_filename)

        # Return the image URL to the frontend
        return jsonify(result=final_message, image_url=image_filename)
    else:
        return jsonify(result=final_message)

@app.route("/bfs", methods=["POST"])
def bfs():
    start = request.form.get("bfs_start")
    end = request.form.get("bfs_end")

    # Message displayed when POST
    initial_message = f"Finding a path from {start} to {end}..."
    # update message
    session["bfs_result"] = initial_message

    # run and time the bfs alg
    start_time = time.time()
    path = algs.bfs(start, end)
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds

    final_message = f"{initial_message}... took {elapsed_time:.2f} ms\nPath: {path}"
    session["bfs_result"] = final_message

    # Generate the graph and save it as an image
    if path:
        image_filename = "static/graph.png"
        G = visualize.get_graph_with_path(path)
        visualize.visualize_graph_with_path(G, path, image_filename)

        # Return the image URL to the frontend
        return jsonify(result=final_message, image_url=image_filename)
    else:
        return jsonify(result=final_message)

if __name__ == "__main__":
    app.run(debug=True)
