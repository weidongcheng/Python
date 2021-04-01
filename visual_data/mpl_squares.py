# _*_ coding:utf-8 _*_

import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('Solarize_Light2')
fit,ax = plt.subplots()
ax.plot(input_values,squares,linewidth=3)

# 设置图标标题并给坐标轴加上标签。
ax.set_title("平方数",fontSize=24)
ax.set_xlabel("值",fontSize=14)
ax.set_ylabel("值的平方",fontSize=14)

#设置刻度标尺的大小。
ax.tick_params(axis='both',labelsize=14)

plt.show()