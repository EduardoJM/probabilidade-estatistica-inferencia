import matplotlib.pyplot as plt


values = [1, 2, 2, 3, 4, 4, 5, 8]

fig1, ax1 = plt.subplots()
ax1.boxplot(values)
#ax1.hlines(y=2, xmin=1.1, xmax=1.4, linewidth = 1, linestyle='-')
ax1.arrow(1.1, 2, 0.3, 0, head_width=0.2, head_length=0.02, linewidth=1, color='0', length_includes_head=False)
ax1.annotate("Q", (1.43, 2))
ax1.annotate("1", (1.45, 1.85), size="x-small")

ax1.arrow(1.1, 4.25, 0.3, 0, head_width=0.2, head_length=0.02, linewidth=1, color='0', length_includes_head=False)
ax1.annotate("Q", (1.43, 4.25))
ax1.annotate("3", (1.45, 4.10), size="x-small")

ax1.arrow(1.1, 3.5, 0.3, 0, head_width=0.2, head_length=0.02, linewidth=1, color='0', length_includes_head=False)
ax1.annotate("Md", (1.43, 3.5))

ax1.arrow(1.1, 8, 0.3, 0, head_width=0.2, head_length=0.02, linewidth=1, color='0', length_includes_head=False)
ax1.annotate("outlier", (1.43, 8), size="x-small")

plt.show()
