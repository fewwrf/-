from turtle import width
import requests

from plotly.graph_objs import bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f'Status code:{r.status_code}')

response_dict = r.json()

#探索所有仓库的信息
repo_dicts = response_dict['items']
repo_links,stars,labels = [],[],[]

for repo_dict in repo_dicts:

    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)


data = [{
    'type':'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6}]

my_layout = {
    'title':'GitHub上最受欢迎的JAVA项目',
    'xaxis':{
        'title':'Repository',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
        },
    'yaxis':{
        'title':'stars',
        'titlefont':{'size':24},
        'tickfont':{'size':14}
        },
        }

fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_practice\\java_repos.html')