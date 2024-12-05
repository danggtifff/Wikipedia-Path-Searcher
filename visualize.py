import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Use Agg backend (no Tkinter)
import matplotlib.pyplot as plt
import db
import os

def get_graph_with_path(path):
    G = nx.Graph()

    # Add the nodes for the path
    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1])

    # Add neighbors for each node in the path
    for node in path:
        neighbors = db.get_a_few_neighbors(node)
        print(f"Neighbors of {node}: {neighbors}")
        if neighbors:
            for neighbor in neighbors:
                if not G.has_edge(node, neighbor):
                    G.add_edge(node, neighbor)

    return G

def visualize_graph_with_path(G, path, image_filename="static/graph.png"):
    # Assign colors to edges
    edge_colors = []
    for u, v in G.edges():
        if u in path and v in path:
            edge_colors.append("red")  # Highlight path edges in red
        else:
            edge_colors.append("gray")  # Other edges in gray

    # Assign colors to nodes
    node_colors = []
    for node in G.nodes():
        if node in path:
            node_colors.append("red")  # Highlight path nodes in red
        else:
            node_colors.append("lightblue")  # Other nodes in light blue

    # Draw the graph with custom colors and save it as an image
    plt.figure(figsize=(5.5, 5.5))
    nx.draw(G, with_labels=True, node_color=node_colors, edge_color=edge_colors,
            font_size=10, node_size=1500, font_weight="bold", width=2)
    plt.savefig(image_filename)
    plt.close()
