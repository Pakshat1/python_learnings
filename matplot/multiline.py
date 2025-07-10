#  Multiple Lines on the Same Plot

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 15, 13, 18, 14]
y2 = [5, 7, 10, 9, 12]

# Plot both lines
plt.plot(x, y1, label="Sales in 2024", marker='o')
plt.plot(x, y2, label="Sales in 2025", marker='s')

plt.title("Comparison of Sales Over Years")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()  # Show legend
plt.grid(True)
plt.show()

########################
# ccostimsze eaxh line 
plt.plot(x, y1, label="2024", color='blue', linestyle='--', marker='o')
plt.plot(x, y2, label="2025", color='green', linestyle='-', marker='s')

plt.title("Styled Comparison")
plt.legend()
plt.show()

