import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 21, 2, 20, 2]
y2 = [5, 4, 3, 2, 1]

plt.plot(x, y, label='Initial line')
plt.plot(x, y2, label='Fhuhfuh')

plt.xlabel('Plot Number')
plt.ylabel('Value')
plt.title('Epic Graph tutorial for data viz with Mathplotlib\ntotorial showing labels and titles')

plt.legend()
plt.show()
