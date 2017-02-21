import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
x2 = [1, 2, 6, 7, 9]
y = [2, 21, 2, 20, 2]
y2 = [5, 4, 3, 2, 1]


plt.bar(x, y, color='m')
plt.plot(x2, y2)

plt.legend()
plt.show()
