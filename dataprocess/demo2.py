import matplotlib.pyplot as plt

# 使用scatter绘制散点图

plt.scatter(2, 4, s=200)  # s的值 代表使用点的尺寸

# 设置标题
plt.title("square numbers", fontsize=24)
# 设置x轴
plt.xlabel("value", fontsize=14)
# 设置y轴
plt.ylabel("square value", fontsize=14)

plt.show()

