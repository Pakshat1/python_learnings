# common plotes 
# | Plot Type    | Function        | Use Case                               |
# | ------------ | --------------- | -------------------------------------- |
# | Bar Chart    | `plt.bar()`     | Compare categories                     |
# | Histogram    | `plt.hist()`    | Show data distribution                 |
# | Pie Chart    | `plt.pie()`     | Show parts of a whole                  |
# | Scatter Plot | `plt.scatter()` | Show correlation between two variables |
# | Box Plot     | `plt.boxplot()` | Show spread and outliers               |
# | Subplots     | `plt.subplot()` | Show multiple plots in one figure      |

# BAR CHART
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 12]

plt.bar(categories, values, color='teal')
plt.title("Category Comparison")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# HISTOGTAM CHART
import matplotlib.pyplot as plt

data = [10, 12, 13, 14, 15, 13, 12, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26]

plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title("Data Distribution")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()


# PIE CHART
labels = ['Python', 'Java', 'C++', 'C#']
sizes = [40, 25, 20, 15]
colors = ['gold', 'lightblue', 'lightgreen', 'pink']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("Programming Language Popularity")
plt.axis('equal')  # Makes it a perfect circle
plt.show()

# SCATTAR PLOT
x = [1, 2, 3, 4, 5]
y = [5, 7, 4, 8, 6]

plt.scatter(x, y, color='red', marker='x')
plt.title("Scatter Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# BOX PLOT
data = [20, 21, 19, 22, 24, 25, 30, 15, 14, 22, 24, 26, 28, 30]

plt.boxplot(data)
plt.title("Box Plot Example")
plt.ylabel("Values")
plt.show()

# SUBPLOTS
x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [30, 25, 20, 10]

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.plot(x, y2)
plt.title("Plot 2")

plt.tight_layout()  # Fix overlap
plt.show()


