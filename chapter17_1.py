import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
print(f'Status code:{r.status_code}')

response_dict = r.json()

print(f'Total repositories: {response_dict["total_count"]}')

#探索所有仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")


for repo_dict in repo_dicts:
    print(f"名称:{repo_dict['name']}")
    print(f"项目开发者:{repo_dict['owner']['login']}")
    print(f"stars:{repo_dict['stargazers_count']}")
    print(f"项目的url:{repo_dict['html_url']}")
    print(f"最后一次更新:{repo_dict['updated_at']}")
    print(f"项目简介:{repo_dict['description']}")