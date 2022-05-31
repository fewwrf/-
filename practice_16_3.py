import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime

#设置样式
plt.style.use('seaborn')
#将字体设置为楷体
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']

#文件路径
filename = 'python_practice\\Australia_Norfolk_island_30days.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #从文件中获取日期及每日最高温度
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%d/%m/%Y")
        low = float(row[3])
        high = float(row[2])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)



#根据每日最高温度及最低温度绘图
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)


#设置图形的格式
ax.set_title('2022年诺福克岛五月气温',fontsize=24)
ax.set_xlabel('',fontsize=16)
#x轴标签设置为倾斜的
fig.autofmt_xdate()

ax.set_ylabel('温度(C)',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()