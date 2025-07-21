from github import Github
import json

# Replace with your GitHub username and token
GITHUB_USERNAME = "us107"
GITHUB_TOKEN = "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"

# Initialize GitHub API client
g = Github(GITHUB_TOKEN)
user = g.get_user(GITHUB_USERNAME)

repos_data = []

print(f"Fetching repositories for user: {GITHUB_USERNAME}...")

for repo in user.get_repos():
    try:
        readme = repo.get_readme().decoded_content.decode()
    except:
        readme = ""
    
    repo_info = {
        "name": repo.name,
        "readme": readme,
        "topics": repo.get_topics(),
        "language": repo.language
    }
    repos_data.append(repo_info)

# Save as JSON
with open("repos_data.json", "w", encoding='utf-8') as f:
    json.dump(repos_data, f, indent=2, ensure_ascii=False)

print("✅ Repository data saved to repos_data.json")
