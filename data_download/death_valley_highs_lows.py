import csv
from datetime import datetime
from matplotlib import pyplot as plt

plt.style.use('seaborn')
# 在绘图代码中设置全局字体 SimHei（黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']

filename = 'C:\\untitled7\项目二：数据可视化\\data_download\\death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 从文件中获取日期，最高温度和最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据最高温度和最低温度绘制图形
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
title = "2018年每日最高温度和最低温度\n 美国加利福尼亚死亡谷"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('温度(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
