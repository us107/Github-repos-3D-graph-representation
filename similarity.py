import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load your repo data
with open("repos_data.json", "r", encoding='utf-8') as f:
    repos = json.load(f)

# Extract README text
readmes = [repo["readme"] for repo in repos]
repo_names = [repo["name"] for repo in repos]

# Load the embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

print("🔄 Generating embeddings...")
embeddings = model.encode(readmes)

# Compute cosine similarity matrix
print("📏 Computing cosine similarity...")
similarity_matrix = cosine_similarity(embeddings)

# Save matrix and names
np.save("similarity_matrix.npy", similarity_matrix)
with open("repo_names.json", "w") as f:
    json.dump(repo_names, f)

print("✅ Saved similarity_matrix.npy and repo_names.json")
