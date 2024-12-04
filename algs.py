# algs.py made for Chris
import sqlite3, ast, json
import db as db
from collections import deque

import sqlite3
import json
from collections import deque

import time

# breadth-first search over adjacency list graph of wikipedia links
def bfs(start, end):
    print("hi")
    start = db.check_id(start)
    end = db.check_id(end)
    print(start, end)
    if not (start and end):
        print("Start or end node does not exist")
        return
    
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
                name = db.check_name(search_value)
                path.append(name)
                search_value = parent[search_value]
            return path[::-1]

        
        neighbors = db.fetch_neighbors(search_value)
        for neighbor in neighbors:
            if neighbor not in visited:
                print(neighbor)
                visited.add(neighbor)
                parent[neighbor] = search_value
                queue.append(neighbor)

    if not queue:
        print(f"No path found from {start} to {end}.")
        return None

# depth-first search over adjacency list graph of wikipedia links
def dfs(start, end, depth_limit):
    start = db.check_id(start)
    end = db.check_id(end)
    if not start or end:
        print("Start or end node does not exist")
        return

    stack = deque()
    visited = set()
    visited.add(start)
    stack.append((start, 1))
    parent = {start: None}

    print(f"{start}, {end}")

    while stack:
        search_value, depth = stack.pop()


        print(search_value, end)

        print(f"Visiting: {search_value}, Stack Size: {len(stack)}, Visited Nodes: {len(visited)}")

        if int(search_value) == int(end):
            print("hello there!!!")
            path = []
            while search_value is not None:
                name = db.check_name(search_value)
                path.append(name)
                search_value = parent[search_value]
            return path[::-1]

        if depth < depth_limit:
            neighbors = db.fetch_neighbors(search_value)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = search_value
                    stack.append((neighbor, depth+1))

    if not stack:
        print(f"No path found from {start} to {end} within depth limit of {depth_limit}.")
        return None

def iddfs(start, end, max_depth):
    for depth in range(1, max_depth + 1):
        print(f"Searching with max depth: {depth}.")
        path = dfs(start, end, depth)
        if path is not None:
            return path
    return None