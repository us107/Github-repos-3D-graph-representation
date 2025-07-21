import json
from collections import Counter
import re
import string
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords (only the first time)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load the repos data
with open("repos_data.json", "r", encoding='utf-8') as f:
    repos = json.load(f)

topics = []
languages = []
readme_text = ""

for repo in repos:
    topics.extend(repo.get("topics", []))
    if repo.get("language"):
        languages.append(repo["language"])
    readme_text += " " + repo.get("readme", "")

# Count topics
topic_counts = Counter(topics)
language_counts = Counter(languages)

# Process README text
def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words and len(word) > 3]
    return tokens

readme_tokens = clean_text(readme_text)
keyword_counts = Counter(readme_tokens)

# Top N results
TOP_N = 15

print("\n🔖 Most Common Topics:")
for topic, count in topic_counts.most_common(TOP_N):
    print(f"{topic}: {count}")

print("\n🗣️ Most Common Languages:")
for lang, count in language_counts.most_common(TOP_N):
    print(f"{lang}: {count}")

print("\n🧠 Top README Keywords:")
for word, count in keyword_counts.most_common(TOP_N):
    print(f"{word}: {count}")
