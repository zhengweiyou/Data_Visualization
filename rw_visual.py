import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例
rw = RandomWalk(5000)
rw.fill_walk()
# 将所有的点都绘制出来
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.scatter(rw.x_values, rw.y_values, s=15)

# 突出起点和终点
ax.scatter(0, 0, c='green', edgecolor='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
plt.show()
# plt.savefig('rw_visual.png', bbox_inches='tight')