import csv
from datetime import datetime
import matplotlib.pyplot as plt


plt.style.use('seaborn')
# 在绘图代码中设置全局字体 SimHei（黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']

filename = 'C:\\untitled7\\项目二：数据可视化\\data_download\\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期和最高温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# 根据最高温度和最低温度绘制图形
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
ax.set_title('2018年每日最高温度', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('温度(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

"""
画布(Figure)  坐标轴(Axes)  子图(Subplots)
plt.tick_params()
enumerate():获取每个元素的索引及其值
fig.autofmt_xdate():绘制倾斜的日期标签
strptime():第二个实参设置日期的格式 %Y 四位的年份（2022）  %m 用数表示月份（0~12）  %d 用数表示月份中的一天（01~31）
alpha指定颜色的透明度。alpha为0完全透明，为1完全不透明
"""