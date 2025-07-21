import json
import numpy as np
import networkx as nx

# === Load Data ===
with open("repos_data.json", "r", encoding='utf-8') as f:
    repos = json.load(f)

with open("repo_names.json", "r") as f:
    repo_names = json.load(f)

similarity_matrix = np.load("similarity_matrix.npy")

# === Graph Init ===
G = nx.Graph()
SIMILARITY_THRESHOLD = 0.6

# === Add Nodes ===
for idx, repo in enumerate(repos):
    G.add_node(idx, 
               label=repo["name"],
               language=repo["language"],
               topics=repo["topics"],
               readme_length=len(repo["readme"]))

# === Add Edges ===
for i in range(len(repos)):
    for j in range(i + 1, len(repos)):
        weight = 0

        # Rule 1: Cosine similarity
        if similarity_matrix[i][j] > SIMILARITY_THRESHOLD:
            weight += 1

        # Rule 2: Shared topics
        topics_i = set(repos[i].get("topics", []))
        topics_j = set(repos[j].get("topics", []))
        if topics_i.intersection(topics_j):
            weight += 1

        # Rule 3: Same language
        if repos[i].get("language") == repos[j].get("language"):
            weight += 1

        # Add edge if at least one rule matched
        if weight > 0:
            G.add_edge(i, j, weight=weight)

# === Export to D3/3D JSON format ===
graph_json = {
    "nodes": [
        {
            "id": str(i),
            "label": data["label"],
            "language": data["language"],
            "topics": data["topics"],
            "size": data["readme_length"]
        }
        for i, data in G.nodes(data=True)
    ],
    "links": [
        {
            "source": str(u),
            "target": str(v),
            "value": d["weight"]
        }
        for u, v, d in G.edges(data=True)
    ]
}

with open("graph.json", "w", encoding='utf-8') as f:
    json.dump(graph_json, f, indent=2, ensure_ascii=False)

print("✅ Graph data saved to graph.json")
print(f"📊 Total nodes: {len(G.nodes())}, Total edges: {len(G.edges())}")
