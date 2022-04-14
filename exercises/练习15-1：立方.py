import matplotlib.pyplot as plt

plt.style.use('seaborn')

plt.rcParams['font.sans-serif'] = ['SimHei']

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

# 设置图表标题并给坐标轴加上标签
ax.set_title("立方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的立方", fontsize=14)

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)

# plt.show()
plt.savefig('color_cubes_plot.png', bbox_inches='tight')