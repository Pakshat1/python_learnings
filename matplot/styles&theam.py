# style and themes
import matplotlib.pyplot as plt

print(plt.style.available)

# use by style
plt.style.use('ggplot')  # Try 'seaborn', 'dark_background', etc.

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, marker='o')
plt.title("Styled Plot with ggplot")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

# | Style Name          | Description                                      |
# | ------------------- | ------------------------------------------------ |
# | `'ggplot'`          | Mimics R's ggplot2; red grid background          |
# | `'seaborn'`         | Clean, beautiful plots with smooth color palette |
# | `'bmh'`             | Used in Bayesian Methods for Hackers book        |
# | `'fivethirtyeight'` | Similar to plots from FiveThirtyEight.com        |
# | `'dark_background'` | Good for slides/presentations                    |
# | `'classic'`         | The default pre-2.x Matplotlib look              |


import matplotlib.pyplot as plt

# Apply a built-in style
plt.style.use('ggplot')  # Try 'seaborn-v0_8', 'bmh', 'classic', etc.

# Sample data for three years
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue_2023 = [100, 120, 130, 115, 140, 155]
revenue_2024 = [110, 125, 135, 125, 145, 160]
revenue_2025 = [120, 130, 140, 135, 150, 165]

# Set figure size and DPI
plt.figure(figsize=(10, 6), dpi=100)

# Plot 3 lines with styles
plt.plot(months, revenue_2023, label='2023', color='blue', linestyle='--', marker='o', linewidth=2)
plt.plot(months, revenue_2024, label='2024', color='green', linestyle='-', marker='s', linewidth=2)
plt.plot(months, revenue_2025, label='2025', color='orange', linestyle=':', marker='^', linewidth=2)

# Titles and labels
plt.title("Company Revenue Comparison (2023–2025)", fontsize=14)
plt.xlabel("Months")
plt.ylabel("Revenue (in $1000s)")

# Customize ticks
plt.xticks(rotation=45)
plt.yticks([100, 120, 140, 160, 180])

# Add grid
plt.grid(True, linestyle='--', color='gray', alpha=0.7)

# Add annotation (arrow)
plt.annotate('Peak Revenue',
             xy=('Jun', 165),
             xytext=('May', 175),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10)

# Show legend
plt.legend()

# Adjust layout
plt.tight_layout()

# Save the figure (optional)
plt.savefig(r"C:\Users\patel\OneDrive\Documents\python\python_learnings\matplot\customized_revenue_plot.png")

# Show plot
plt.show()
