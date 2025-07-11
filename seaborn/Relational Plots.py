# Relational Plots
# These plots are used when you're visualizing the relationship 
# between two or more numeric variables, often grouped by category.

# | Chart           | Purpose                                                              |
# | --------------- | -------------------------------------------------------------------- |
# | `scatterplot()` | Simple relationship between 2 numeric variables                      |
# | `relplot()`     | General-purpose relational plot (supports faceting, hue, size, etc.) |
# | `lmplot()`      | Scatterplot with a **regression line** (best-fit)                    |

# scatterplot() — Basic Relationship
# You want to see correlation between two numeric columns.

# Example: Hours Studied vs Exam Score.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data for regression
df_study = pd.DataFrame({
    'Hours_Studied': [1, 2, 3, 4, 5, 6],
    'Marks': [45, 50, 60, 65, 70, 78]
})

# Scatterplot
sns.scatterplot(data=df_study, x='Hours_Studied', y='Marks')
plt.title("Study Hours vs Marks")
plt.show()

# Relplot (with different dataset)
df_tips = sns.load_dataset('tips')
sns.relplot(data=df_tips, x='total_bill', y='tip', hue='sex')
plt.title("Tip vs Total Bill by Gender")
plt.show()

# lmplot using the original data
sns.lmplot(data=df_study, x='Hours_Studied', y='Marks')
plt.title("Regression: Study Hours vs Marks")
plt.show()

# | Plot            | Use When...                             |
# | --------------- | --------------------------------------- |
# | `scatterplot()` | You want to see relationship (X vs Y)   |
# | `relplot()`     | You want multiple dimensions (hue, col) |
# | `lmplot()`      | You want best-fit (regression) line     |

