import json
import requests
import plotly

url='https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"status code:{r.status_code}")

response_dict = r.json()
readable_file = 'python_practice\\readable_hn_data.json'
with open(readable_file,'w') as f:
    json.dump(response_dict,f,indent=4)