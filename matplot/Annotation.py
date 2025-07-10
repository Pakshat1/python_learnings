# Annotations
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker='o')
plt.title("Add Text Annotations")

# Add text at a point (x=3, y=15)
plt.text(3, 15, "This point ", fontsize=10, color='red')

plt.grid(True)
plt.show()

##################################################################

plt.plot(x, y, marker='o')
plt.title("Arrow Annotation")

# Highlight the peak point
plt.annotate("Peak", 
             xy=(4, 30),                # Point to annotate
             xytext=(3, 35),            # Location of text
             arrowprops=dict(facecolor='green', shrink=0.05),
             fontsize=10, color='green')

plt.grid(True)
plt.show()

