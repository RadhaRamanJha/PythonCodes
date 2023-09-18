# using for loop to generate visal indicating
# popularity of projects on git hub for following languages
# "JavaScript","Ruby","C","Java","Perl","Haskell","Go"

import requests
from plotly.graph_objs import Bar
from plotly import offline

languages = ["JavaScript","Ruby","C","Java","Perl","Haskell","Go"]
for language in languages:
    # Make API call and store response
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
    headers = {'Accept':'application/vnd.github+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    # Process results
    if r.status_code == 200:
        response_dict = r.json()
        rep_dicts = response_dict["items"]
        repo_links, stars, labels = [],[],[]
        for rep_dict in rep_dicts:
            repo_name =  rep_dict['name']
            repo_url = rep_dict['html_url']
            repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
            repo_links.append(repo_link)
            stars.append(rep_dict['stargazers_count'])
        
            owner = rep_dict['owner']['login']
            description = rep_dict['description']
            label = f"{owner}<br />{description}"
            labels.append(label)
        
        # Make vizualization.
        data = [{
            'type':'bar',
            'x': repo_links,
            'y': stars,
            'hovertext':labels,
            'marker':{
                'color': 'rgb(60,100,150)',
                'line':{'width':1.5,'color':'rgb(25,25,25)'}
            },
            'opacity':0.6,
        }]
        
        my_layout = {
            'title':f'Most-Starred {language} Projects on GitHub',
            'titlefont':{'size':28},
            'xaxis':{
                'title':'Repository',
                'titlefont':{'size':25},
                'tickfont':{'size':15},
                },
            'yaxis':{
                'title':'Stars',
                'titlefont':{'size':25},
                'tickfont':{'size':15},
                },
        }
        
        fig = {'data':data, 'layout':my_layout}
        offline.plot(fig,filename=f'{language}_repos.html')