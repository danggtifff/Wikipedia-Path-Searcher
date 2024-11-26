# algs.py made for Chris

# breadth-first search over adjacency list graph of wikipedia links
def bfs(start, end, graph):
    queue = []
    visited = set()
    visited.add(start)
    queue.append([start])

    while queue:
        path = queue.pop(0)
        if path[-1] == end:
            return path

        for neighbor in graph[path[-1]]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

# depth-first search over adjacency list graph of wikipedia links
def dfs(start, end, graph):
    stack = []
    visited = set()
    visited.add(start)
    stack.append([start])

    while stack:
        path = stack.pop()
        if path[-1] == end:
            return path

        for neighbor in graph[path[-1]]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(path + [neighbor])