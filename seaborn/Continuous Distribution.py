# Continuous Distribution\
# These plots help you visualize the distribution (shape, spread, peaks) 
# of numeric columns like age, salary, income, etc.

# These plots are ideal when your column is numeric (not categories), and you want to:
# Understand how your data is spread
# Detect trends, outliers, or skewness
# Summarize large sets of values visually

# | Plot         | Purpose                                  |
# | ------------ | ---------------------------------------- |
# | `histplot()` | Histogram (how many values fall in bins) |
# | `kdeplot()`  | Smooth curve showing probability density |
# | `ecdfplot()` | Cumulative % of data less than or equal  |

# | Plot       | Use When You Want To...                  |
# | ---------- | ---------------------------------------- |
# | `histplot` | Count how many values fall in each bin   |
# | `kdeplot`  | See smooth shape (peaks, spread, skew)   |
# | `ecdfplot` | Know how much of data is ≤ a given value |


# example 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
# histplot
df = pd.DataFrame({'Age': [22, 25, 28, 30, 22, 24, 27, 29, 33, 26, 30, 31]})

sns.histplot(data=df, x='Age', bins=5, kde=False)
plt.title("Age Distribution (Histogram)")
plt.show()

# Kernel Density Estimate
sns.kdeplot(data=df, x='Age', fill=True)
plt.title("Age Distribution (KDE)")
plt.show()

# histplot() with KDE together (best of both)
sns.histplot(data=df, x='Age', bins=5, kde=True)
plt.title("Age Histogram with KDE")
plt.show()

# ecdfplot() — Cumulative distribution
sns.ecdfplot(data=df, x='Age')
plt.title("Age ECDF Plot")
plt.show()


