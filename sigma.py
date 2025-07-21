import json
import numpy as np

# Load your cosine similarity matrix and repo list
with open("repo_names.json", "r") as f:
    repo_list = json.load(f)

cosine_matrix = np.load("similarity_matrix.npy")  # or whatever filename you saved

nodes = []
edges = []
threshold = 0.75  # Only connect if cosine similarity > threshold

for i, repo in enumerate(repo_list):
    nodes.append({
        "id": f"repo{i}",
        "label": repo,
        "x": np.cos(i),
        "y": np.sin(i),
        "size": 2,
        "color": "#0099FF"
    })

for i in range(len(repo_list)):
    for j in range(i + 1, len(repo_list)):
        sim = cosine_matrix[i][j]
        if sim > threshold:
            edges.append({
                "id": f"e{i}-{j}",
                "source": f"repo{i}",
                "target": f"repo{j}",
                "label": f"cosine: {sim:.2f}",
                "color": "#AAAAAA"
            })

# Save to Sigma-compatible JSON
graph_data = {"nodes": nodes, "edges": edges}
with open("sigma_graph.json", "w") as f:
    json.dump(graph_data, f, indent=2)

print("✅ sigma_graph.json generated!")
