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
    # print(header_row)

    # 从文件中获取每日降雨量
    prcps = []
    for row in reader:
        prcp = float(row[3])
        prcps.append(prcp)

# 根据每日降雨量绘制图形
fig, ax = plt.subplots()
ax.plot(prcps, c='red')

# 设置图形的格式
ax.set_title('2018年每日降雨量', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('PRCP', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()


