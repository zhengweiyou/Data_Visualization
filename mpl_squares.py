import matplotlib.pyplot as plt

# 在绘图代码中设置全局字体 SimHei（黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

#subplots():在一张图片中绘制一个或多个图表 fig表示整张图片，ax表示图片中的各个图表
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# ax.plot(input_values, squares, linewidth=3)

# 设置图标的标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

#打开Matplotlib查看器并显示绘制的图标
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')


"""
subplots():在一张图片中绘制一个或多个图表 fig表示整张图片，ax表示图片中的各个图表
plot()根据给定数据有意义的方式绘制图标
fontsize指定图表中文字大小
linewidth决定绘制线条的粗细
tick_params()设置刻度的样式
scatter()传递一对坐标（x,y),在指定位置绘制一个点
axis()：指定了每个坐标的取值范围 x和y坐标轴的最大值和最小值
plt.savefig('文件名'):让程序自动将图表保存到文件中
"""