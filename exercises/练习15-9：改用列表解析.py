from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die()

# 掷几次骰子并将结果存储到一个列表中
results = [die_1.roll() + die_2.roll() for i in range(1000)]
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# 分析结果
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'结果', 'dtick': 1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷两个D6 1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='../die_images/two_d6_列表解析.html')