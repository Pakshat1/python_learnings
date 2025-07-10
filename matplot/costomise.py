# | Feature         | What It Does                               |
# | --------------- | ------------------------------------------ |
# | Axes Ticks      | Customize values on X and Y axes           |
# | Grid Lines      | Add background grid for better readability |
# | Annotations     | Add custom text or labels on plots         |
# | Multiple Plots  | Plot multiple lines in one chart           |
# | Styles & Themes | Use predefined plot styles                 |


import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Use a predefined style
plt.style.use('ggplot')

# Plot multiple lines
plt.plot(x, y1, label='Prime Numbers', marker='o')
plt.plot(x, y2, label='Other Numbers', marker='s')

# Customize axes ticks
plt.xticks([1, 2, 3, 4, 5], ['A', 'B', 'C', 'D', 'E'])
plt.yticks(range(0, 13, 2))

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.7)

# Add annotations
plt.annotate('Highest Prime', xy=(5, 11), xytext=(3, 11),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Customized Plot Example')
plt.legend()

plt.show()



