import networkx as nx
import matplotlib.pyplot as plt
import os
from matplotlib.patches import FancyArrowPatch, Circle

os.makedirs("figures", exist_ok=True)

def save_graph(G, title, filename, directed=False):
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G, seed=42)

    if directed:
        nx.draw(
            G, pos, with_labels=True,
            node_color="lightblue",
            node_size=1200,
            arrows=True,
            font_weight="bold"
        )
    else:
        nx.draw(
            G, pos, with_labels=True,
            node_color="lightblue",
            node_size=1200,
            font_weight="bold"
        )

    plt.title(title)
    plt.savefig(f"figures/{filename}.png", dpi=300, bbox_inches="tight")
    plt.close()


# 1. Simple Graph
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
save_graph(G1, "Simple Graph", "simple_graph")


# 2. Multigraph (contains parallel edges)

G2 = nx.MultiGraph()
G2.add_edges_from([(1, 2), (1, 2), (2, 3), (3, 1)])

plt.figure(figsize=(6, 4))

pos = {1: (0, 1), 2: (2, 1), 3: (1, 0)}

nx.draw_networkx_nodes(
    G2, pos, node_color="lightblue", node_size=1200
)

nx.draw_networkx_labels(G2, pos, font_weight="bold")

# Two parallel edges between vertices 1 and 2
edge1 = FancyArrowPatch(
    pos[1], pos[2],
    connectionstyle="arc3,rad=0.25",
    arrowstyle="-",
    linewidth=2
)

edge2 = FancyArrowPatch(
    pos[1], pos[2],
    connectionstyle="arc3,rad=-0.25",
    arrowstyle="-",
    linewidth=2
)

ax = plt.gca()
ax.add_patch(edge1)
ax.add_patch(edge2)

# Remaining edges
nx.draw_networkx_edges(
    G2, pos, edgelist=[(2, 3), (3, 1)]
)

plt.title("Multigraph - Parallel Edges")
plt.axis("off")
plt.savefig("figures/multigraph.png", dpi=300, bbox_inches="tight")
plt.close()


# 3. Pseudograph (contains a self-loop)

G3 = nx.MultiGraph()
G3.add_edges_from([(1, 1), (1, 2), (2, 3), (3, 1)])

plt.figure(figsize=(6, 4))

pos = {1: (0, 1), 2: (2, 1), 3: (1, 0)}

nx.draw_networkx_nodes(
    G3, pos, node_color="lightblue", node_size=1200
)

nx.draw_networkx_labels(G3, pos, font_weight="bold")

# Draw normal edges
nx.draw_networkx_edges(
    G3, pos, edgelist=[(1, 2), (2, 3), (3, 1)]
)

# Draw a clearly visible self-loop at vertex 1
loop = Circle(
    (-0.12, 1.22),
    radius=0.22,
    fill=False,
    linewidth=2
)

plt.gca().add_patch(loop)

plt.title("Pseudograph - Self Loop")
plt.axis("off")
plt.savefig("figures/pseudograph.png", dpi=300, bbox_inches="tight")
plt.close()

# 4. Directed Graph
G4 = nx.DiGraph()
G4.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4)])
save_graph(G4, "Directed Graph (Digraph)", "directed_graph", True)


# 5. Weighted Graph
G5 = nx.Graph()
G5.add_weighted_edges_from([
    (1, 2, 5), (2, 3, 3), (3, 4, 7),
    (4, 1, 2), (1, 3, 4)
])

plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G5, seed=42)
nx.draw(G5, pos, with_labels=True, node_color="lightblue",
        node_size=1200, font_weight="bold")
nx.draw_networkx_edge_labels(
    G5, pos, edge_labels=nx.get_edge_attributes(G5, "weight")
)
plt.title("Weighted Graph")
plt.savefig("figures/weighted_graph.png", dpi=300, bbox_inches="tight")
plt.close()


# 6. Mixed Graph (directed and undirected edges)
G6 = nx.Graph()
G6.add_edges_from([(1, 2), (2, 3), (3, 4)])

plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G6, seed=42)
nx.draw(G6, pos, with_labels=True, node_color="lightblue",
        node_size=1200, font_weight="bold")
nx.draw_networkx_edges(
    G6, pos, edgelist=[(1, 2), (2, 3)], arrows=True,
    connectionstyle="arc3,rad=0.15"
)
plt.title("Mixed Graph (Illustrative)")
plt.savefig("figures/mixed_graph.png", dpi=300, bbox_inches="tight")
plt.close()

print("All six graph visualisations saved in the figures folder!")