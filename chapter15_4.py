from random import randint
from plotly.graph_objs import Bar,Layout
from plotly import offline

class Die:
    def __init__(self,num_sides=6) -> None:
        self.num_sides = num_sides


    def roll(self):
        return randint(1,self.num_sides)


#创建一个D6和D10
D6 = Die()
D10 = Die(10)

#将投掷出来结果存储在列表中
results = []
for _ in range(50000):
    result = D6.roll() + D10.roll()
    results.append(result)

#获得结果的次数并存储
frequencies = []
for value in range(2,D6.num_sides+D10.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#将结果可视化
x_values = list(range(2,D6.num_sides+D10.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷一个D6和一个D10 50000次',xaxis=x_axis_config,yaxis=y_axis_config)

#将结果存储
offline.plot({'data':data,'layout':my_layout},filename='python_practice\\d6_d10.html')