import requests

# Make an API call and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f"Satus code: {r.status_code}")
# label API response with a variable
response_dict = r.json()

# Process results
print(response_dict.keys())