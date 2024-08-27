import requests

def github_scraper(search_term):
    url = f"https://github.com/search?q={search_term}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        repos = []

        for result in data['payload']['results']:
            repo_name = result['repo']['repository']['name']
            repo_link = f"https://github.com/{result['repo']['repository']['owner_id']}/{repo_name}"
            repo_description = result['hl_trunc_description']
            repo_stars = result['followers']
            
            repos.append({
                "name": repo_name,
                "link": repo_link,
                "description": repo_description,
                "stars": repo_stars
            })

        return repos
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

# Example Usage
search_term = input("Enter the search term for GitHub repositories: ")
repositories = github_scraper(search_term)

# Print the results
for repo in repositories:
    print(f"Name: {repo['name']}")
    print(f"Link: {repo['link']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stars']}")
    print("-------------------------------")