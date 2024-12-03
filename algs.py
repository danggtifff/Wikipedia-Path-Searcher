# algs.py made for Chris
import sqlite3, ast, json
import db as db
from collections import deque

import sqlite3
import json
from collections import deque
from functools import lru_cache
import time

# Load neighbors on demand with caching for repeated access
#@lru_cache(maxsize=100000)  # Cache up to 100,000 nodes
def fetch_neighbors(name):
    conn = db.get_db()
    cursor = conn.cursor()
    query = "SELECT outlinks FROM wikilinks WHERE name = ?"
    cursor.execute(query, (name,))
    row = cursor.fetchone()

    try:
        return json.loads(row[0]) if row else []
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        return []

# breadth-first search over adjacency list graph of wikipedia links
def bfs(start, end):
    queue = deque()
    visited = set()
    visited.add(start)
    queue.append(start)
    parent = {start: None}

    print(f"{start}, {end}")

    while queue:
        search_value = queue.popleft()
        print(search_value, end)
    
        print(f"Visiting: {search_value}, Queue Size: {len(queue)}, Visited Nodes: {len(visited)}")

        if int(search_value) == int(end):
            print("hello!!!!")
            path = []
            while search_value is not None:
                path.append(search_value)
                search_value = parent[search_value]
            return path[::-1]

        
        neighbors = fetch_neighbors(search_value)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = search_value
                queue.append(neighbor)

    if not queue:
        print(f"No path found from {start} to {end}.")
        return None

# depth-first search over adjacency list graph of wikipedia links
def dfs(start, end, depth_limit):

    stack = deque()
    visited = set()
    visited.add(start)
    stack.append([start])
    parent = {start: None}

    while stack:
        search_value = stack.pop()
        depth = len(path)
        node = path[-1]

        if node == end:
            return path

        if depth < depth_limit:
            # node has no connections
            neighbors = fetch_neighbors(search_value)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = search_value
                    queue.append(neighbor)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(path + [neighbor])

    # no path found within depth limit
    print(f"No path found within depth limit of {depth_limit}.")
    return None