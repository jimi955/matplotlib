import matplotlib.pyplot as plt

# 使用scatter绘制散点图

# input_x = [1, 2, 3, 4, 5]
# input_y = [1, 4, 9, 16, 25]

input_x = list(range(1, 1001))
input_y = [x ** 2 for x in input_x]

# plt.scatter(input_x, input_y, s=40)
# plt.scatter(input_x, input_y, edgecolor='none', s=40)
# matplotlib 2.0版本后 edgecolor默认为none 当前版本3.1.1(none表示 没有轮廓）

# plt.scatter(input_x, input_y, c='red', edgecolor='none', s=40)  # c  线的color
# plt.scatter(input_x, input_y, c=(0, 0, 0.8), edgecolor='none', s=40)  # c  线的color  RGB表示
plt.scatter(input_x, input_y, c=input_y, cmap=plt.cm.Reds, edgecolor='none', s=40)  # cmap表示颜色图谱  放在plt.cm中

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

# 设置标题
plt.title("square numbers", fontsize=24)
# 设置x轴
plt.xlabel("value", fontsize=14)
# 设置y轴
plt.ylabel("square value", fontsize=14)

plt.show()
# 保存图片  像素设置高
plt.savefig("squares_plot.png", bbox_inches='tight')
