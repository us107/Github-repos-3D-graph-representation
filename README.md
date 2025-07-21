
# GitHub Repositories 3D Graph Visualization

A visual map of your GitHub repositories — clustered by topic, labeled by language, and linked by cosine similarity.  
This interactive graph reveals how your ideas connect and evolve across projects.

---

## Features

- Extracts metadata from your GitHub repos (topics, languages, README keywords)
- Generates vector embeddings using `text-embedding-3-small`
- Calculates cosine similarity between all repos
- Builds a similarity graph using NetworkX
- Visualizes it interactively using Sigma.js with curved edges and repo labels

---

## Folder Structure

```
Github-repos-3D-graph-representation/
├── data/
│   └── github_metadata.json         
├── graph/
│   ├── graph_matrix.npy             
│   └── sigma_graph.json             
├── web/
│   ├── index.html                   
│   └── graph-data.js               
├── scripts/
│   ├── 1_fetch_github_data.py       
│   ├── 2_generate_embeddings.py     
│   ├── 3_build_graph.py             
│   └── 4_convert_to_sigma.py        
└── README.md
```

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install numpy pandas openai networkx scikit-learn tiktoken
```

### 2. Set your GitHub and OpenAI API keys

```bash
export GITHUB_TOKEN=your_token
export OPENAI_API_KEY=your_key
```

### 3. Run the pipeline

```bash
python scripts/1_fetch_github_data.py        
python scripts/2_generate_embeddings.py      
python scripts/3_build_graph.py              
python scripts/4_convert_to_sigma.py         
```

---

## How It Works

| Step         | Description                                        |
|--------------|----------------------------------------------------|
| Metadata     | Collects repo name, topics, README, and language   |
| Embedding    | Uses OpenAI to embed combined text into vectors    |
| Similarity   | Computes cosine distance for each repo pair        |
| Graph        | Creates a graph (nodes = repos, edges = similar)   |
| Visualization| Interactive graph rendered via Sigma.js            |

---

## How to Visualize

### Option A: Run with Python

```bash
cd web/
python -m http.server 5500
```

Then visit: `http://localhost:5500/index.html`

### Option B: VS Code Live Server

1. Open `index.html` in the editor
2. Right-click → "Open with Live Server"
3. Ensure `graph-data.js` is in the same folder

---

## Sample Output

- Common README keywords and topics
- Repository clusters by domain (e.g., AI, Web, Analytics)
- Cosine similarity edges labeled with strength

---


## Author

**Trisha Sharma**  
Data Science and Engineering Graduate
---


