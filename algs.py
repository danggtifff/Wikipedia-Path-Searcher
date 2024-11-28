# algs.py made for Chris
import sqlite3, ast, json
import db as db
from collections import deque

query = "SELECT * FROM wikilinks WHERE name = 12"

def load_graph():
    my_db = db.get_db()
    graph = {}
    cursor = my_db.cursor()
    cursor.execute("SELECT name, outlinks FROM wikilinks")
    for row in cursor.fetchall():
        graph[row[0]] = ast.literal_eval(row[1])
    print("Graph")
    return graph

# breadth-first search over adjacency list graph of wikipedia links
def bfs(start, end):
    graph = load_graph()
    queue = deque()
    visited = set()
    visited.add(start)
    queue.append([start])

    while queue:
        path = queue.popleft()
        search_value = path[-1]
        if search_value == end:
            return path
        
        neighbors = graph.get(search_value, [])

        print(search_value)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

# depth-first search over adjacency list graph of wikipedia links
def dfs(start, end, graph, depth_limit):
    # start and end node handling
    if start not in graph:
        print(f"Start node, {start}, not in graph.")
        return None

    if end not in graph:
        print(f"End node, {end}, not in graph.")

    if not graph[start]:
        print(f"Start node, {start}, has no connections.")
        return None

    stack = []
    visited = set()
    visited.add(start)
    stack.append([start])

    while stack:
        path = stack.pop()
        depth = len(path)
        node = path[-1]

        if node == end:
            return path

        if depth < depth_limit:
            # node has no connections
            if not graph[node]:
                continue

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(path + [neighbor])

    # no path found within depth limit
    print(f"No path found within depth limit of {depth_limit}.")
    return None