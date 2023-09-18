from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

# Making an API call sand storing the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(r)
print(f"Status Code: {r.status_code}")
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make seperate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title':response_dict['title'],
            'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
            'comments':response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except(KeyError):
        print("Mapping Key not Found")
