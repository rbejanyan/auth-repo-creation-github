import requests
import json
import os

# Please use your environment variables
token = os.getenv('GITHUB_TOKEN_R')
username = os.getenv('GITHUB_USERNAME_R')


# Safety check to ensure environment variables are set
if not token or not username:
    raise ValueError("Environment variables for GitHub token and/or username are not set.")

# Set the name for your new repository
repo_name = 'test-repo2'
# Set the description for your new repository
description = 'This is a test repository created using the GitHub REST API'

url = f'https://api.github.com/user/repos'
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}
data = {
    'name': repo_name,
    'description': description,
    'private': False  # Set to True if you want to create a private repository
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 201:
    print(f'Repository "{repo_name}" created successfully.')
    print(f'URL: {response.json()["html_url"]}')
else:
    print('Failed to create repository')
    print('Response:', response.content)
