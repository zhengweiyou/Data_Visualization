from random import randint
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from die import Die

plt.style.use('classic')
plt.rcParams['font.sans-serif'] = ['SimHei']

# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷1000次骰子并将结果存储到一个列表中
results = [die_1.roll() + die_2.roll() for i in range(1000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# 对结果进行可视化
fig, ax = plt.subplots()
ax.bar(range(2, max_result+1), frequencies)
ax.set_title("掷两个D6 1000次的结果")
ax.set_xlabel("结果")
ax.set_ylabel("结果的频率")

# 设置x轴的间隔为1
xmajorLocator = MultipleLocator(1)
ax.xaxis.set_major_locator(xmajorLocator)
plt.show()
# plt.savefig('两个D6_1000次的结果1.png', bbox_inches='tight')
