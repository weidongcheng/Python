import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'the_csv_file_format/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	heard_row = next(reader)

	# 从文件中获取日期和最高温度。
	dates,highs = [], []
	for row in reader:
		current_date= datetime.strptime(row[2],'%Y-%m-%d')
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)

# 根据最高温度绘制图形。
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,c='red')

# 设置图形的格式。
ax.set_title('2018 年每日最高温度',fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('温度（F）',fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()
	# for index,column_header in enumerate(heard_row):
	# 	print(index,column_header)
