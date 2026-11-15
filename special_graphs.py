
import networkx as nx
import matplotlib.pyplot as plt
import os

os.makedirs("figures", exist_ok=True)

graphs = {
    "complete_graph": nx.complete_graph(5),
    "bipartite_graph": nx.complete_bipartite_graph(3, 3),
    "regular_graph": nx.cycle_graph(6),
    "tree_graph": nx.balanced_tree(2, 2),
    "cycle_graph": nx.cycle_graph(6),
    "wheel_graph": nx.wheel_graph(6)
}

for name, G in graphs.items():
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color="skyblue",
        node_size=900,
        edge_color="gray",
        font_weight="bold"
    )

    plt.title(name.replace("_", " ").title())
    plt.savefig(f"figures/{name}.png", dpi=300, bbox_inches="tight")
    plt.close()

print("All six additional graph visualisations saved!")
