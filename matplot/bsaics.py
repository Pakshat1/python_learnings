
# basics
# | Topic        | Function                              |
# | ------------ | ------------------------------------- |
# | Basic Plot   | `plt.plot()`                          |
# | Show Plot    | `plt.show()`                          |
# | Title/Labels | `plt.title()`, `xlabel()`, `ylabel()` |
# | Style        | `color`, `linestyle`, `marker`        |
# | Figure Size  | `plt.figure(figsize, dpi)`            |
# | Save File    | `plt.savefig()`                       |

# 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 4, 8, 6]

plt.plot(x, y)            # Create the line chart
plt.show()                # Show the figure


# creating box plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 14]

plt.plot(x, y)
plt.show()


# adding titles  and lables
plt.plot(x, y)
plt.title("My First Plot")         # Adds title to the chart
plt.xlabel("X Values")             # X-axis label
plt.ylabel("Y Values")             # Y-axis label
plt.show()


