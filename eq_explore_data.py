import json
import plotly.express as px
import pandas as pd

# 探索数据的结构
filename = 'C:\\untitled7\\项目二：数据可视化\\data\\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [], [], []  #震级、标题、经度、纬度
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
data.head()
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
)

fig.write_html('global_earthquakes.html')
fig.show()

# readable_file = 'C:\\untitled7\\项目二：数据可视化\\data\\readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)





"""
json.load():将数据转换为Python能够处理的格式.
json.dump():接受一个JSON数据对象和一个文件对象，并将数据写入这个文件中，indent=4让dump()
使用与数据结构匹配的缩进量来设置数据的格式.
"""