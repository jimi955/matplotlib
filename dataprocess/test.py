import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
# 设置线宽
plt.plot(squares, linewidth=5)
# 设置标题
plt.title("square numbers", fontsize=24)
# 设置x轴
plt.xlabel("value", fontsize=14)
# 设置y轴
plt.ylabel("square value", fontsize=14)
# 设置刻度标记的大小  axis='both'  表示影响两个轴  labelsize  刻度标记的字号
plt.tick_params(axis='both', labelsize=14)
plt.show()


#如何绘制一系列的点