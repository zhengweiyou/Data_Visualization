import csv
from datetime import datetime
import matplotlib.pyplot as plt


plt.style.use('seaborn')
# 在绘图代码中设置全局字体 SimHei（黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']

def weather_data(filename, dates, highs, lows, t_date, t_high, t_low):
    """获取某个城市的日期、最高温度和最低温度"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # 从文件中获取日期、最高温度和最低温度
        for row in reader:
            current_date = datetime.strptime(row[t_date], '%Y-%m-%d')
            try:
                high = int(row[t_high])
                low = int(row[t_low])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# 获得锡特卡的温度
filename = 'C:\\untitled7\\项目二：数据可视化\\data_download\\sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
weather_data(filename, dates, highs, lows, t_date=2, t_high=5, t_low=6)

# 根据锡特卡的数据绘制图形
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.7)
ax.plot(dates, lows, c='green', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# 获得死亡谷的温度
filename = 'C:\\untitled7\\项目二：数据可视化\\data_download\\death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
weather_data(filename, dates, highs, lows, t_date=2, t_high=4, t_low=5)

# 根据死亡谷的数据绘制图形
ax.plot(dates, highs, c='black', alpha=0.7)
ax.plot(dates, lows, c='yellow', alpha=0.7)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)

# 设置图形的格式
ax.set_title('比较锡特卡和死亡谷的温度', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('温度(F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

# 显示表格
plt.show()
