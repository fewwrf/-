import json
import plotly.express as px
import pandas as pd

#从json文件中读取数据
file_name = 'book\\readable_eq_data_30.json'
with open(file_name) as f:
    s = f.read()
    all_eq_data = json.loads(s)

all_eq_dicts = all_eq_data['features']

#震级,位置，经度，纬度
mags,titles,lons,lats = [],[],[],[]
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])


data = pd.DataFrame(
    data = zip(lons,lats,titles,mags),columns= ['经度','纬度','位置','震级']
)

#绘图
fig = px.scatter(data,x="经度",y="纬度",range_x=[-200,200],range_y=[-90,90],width=800,height=800,title='全球散点图',
    size='震级',size_max=10,color='震级',hover_name='位置')

fig.write_html('python_practice\\global_earthquakes.html')
fig.show()

