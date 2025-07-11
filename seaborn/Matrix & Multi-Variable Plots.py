# Matrix & Multi-Variable Plots
# | Plot Type      | Purpose                                    |
# | -------------- | ------------------------------------------ |
# | `heatmap()`    | Show correlation or matrix values visually |
# | `pairplot()`   | All pairwise relationships in a dataset    |
# | `clustermap()` | Cluster rows/cols based on similarity      |

# | Plot           | Use Case                                   |
# | -------------- | ------------------------------------------ |
# | `heatmap()`    | Show correlation or 2D matrix              |
# | `pairplot()`   | Explore all numeric relationships in 1 go  |
# | `clustermap()` | Cluster variables by similarity (advanced) |

# real time use 
# | Use Case                              | Recommended Plot |
# | ------------------------------------- | ---------------- |
# | See how features relate to each other | `heatmap()`      |
# | Quickly understand data distributions | `pairplot()`     |
# | Group similar features automatically  | `clustermap()`   |

# heatmap() — Colorful grid of values (usually correlation)
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = sns.load_dataset('iris')

# Compute correlation matrix
corr = df.corr(numeric_only=True)

# Plot heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap (Iris Dataset)")
plt.show()

# You want to see correlation between numeric columns
# Each cell shows how strongly two columns are related (+1 = strong positive, -1 = strong negative)

# pairplot() — All variable combinations (scatter + histograms)
sns.pairplot(df, hue='species')
plt.suptitle("Pairplot of Iris Data", y=1.02)
plt.show()

# You want to see all numeric relationships at once
# Also shows distribution on diagonal
# Supports hue for coloring by category

# clustermap() — Clustered heatmap (advanced)
sns.clustermap(corr, annot=True, cmap="coolwarm")
plt.title("Clustered Correlation Heatmap")
plt.show()

# You want to group similar columns/rows based on patterns
# Helps in feature selection or pattern detection

