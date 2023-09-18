import requests
# Make an API call and label the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# label API response with a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories 
rep_dicts = response_dict["items"]
print(f"Repositries returned: {len(rep_dicts)}")
print(f"\n Selected Information about the each repository: ")
for rep_dict in rep_dicts:
    print(f"Name :- {rep_dict['name']}")
    print(f"Owner :- {rep_dict['owner']}")
    print(f"repository URL:- {rep_dict['html_url']}")
    print(f"Stars:- {rep_dict['stargazers_count']}")
    print(f"Created on:- {rep_dict['created_at']}")
    print(f"Updated on:- {rep_dict['updated_at']}")
    print(f"Description :- {rep_dict['description']}")