import matplotlib.pyplot as plt

values1 = [22.02, 23.83, 26.67, 25.38, 25.80, 23.58, 25.90, 24.98]
values2 = [21.49, 22.67, 24.62, 24.39, 22.78, 22.59, 24.46, 23.79]
values3 = [20.33, 21.67, 24.67, 22.45, 22.41, 21.95, 20.79, 21.81]

fig1, ax1 = plt.subplots()
ax1.boxplot([values1, values2, values3])
ax1.set_xticklabels(['Mistura 1', 'Mistura 2', 'Mistura 3'])

plt.show()