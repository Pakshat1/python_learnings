
#  Categorical = barplot, countplot, boxplot, violinplot, stripplot, swarmplot

# | Chart          | Use Case                               |
# | -------------- | -------------------------------------- |
# | `barplot()`    | Compare average values by category     |
# | `countplot()`  | Frequency of each category             |
# | `boxplot()`    | Show spread, median, outliers          |
# | `violinplot()` | Show KDE + distribution shape          |
# | `stripplot()`  | Individual observations                |
# | `swarmplot()`  | Non-overlapping scatter for small data |

# | Feature                 | Reason it’s called categorical                                                  |
# | ----------------------- | ------------------------------------------------------------------------------- |
# | Grouped by labels       | Plots are grouped **by category names**                                         |
# | No numeric spacing      | X-axis ticks are not spaced by numbers                                          |
# | Summarize each category | Shows **mean, count, or distribution** of numeric data **within each category** |

# |  Use Categorical Plots When…        |
# | ----------------------------------- |
# | You want to **compare groups**      |
# | X or Y axis is a **label/category** |
# | You are **grouping then analyzing** |

# example 
# barplot 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance'],
    'Salary': [40000, 60000, 55000, 42000, 62000, 53000]
})

sns.barplot(data=df, x='Department', y='Salary')
plt.title("Average Salary by Department")
plt.show()

# countplot
df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'IT', 'HR']
})

sns.countplot(data=df, x='Department')
plt.title("Department Frequency Count")
plt.show()

# box plot
df = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Score': [80, 75, 90, 85, 95, 70]
})

sns.boxplot(data=df, x='Gender', y='Score')
plt.title("Score Distribution by Gender")
plt.show()

# violine plot 
sns.violinplot(data=df, x='Gender', y='Score')
plt.title("Score Distribution (Violin Plot)")
plt.show()

# strip plot
sns.stripplot(data=df, x='Gender', y='Score', jitter=True)
plt.title("Score Strip Plot by Gender")
plt.show()

# swarm plot
sns.swarmplot(data=df, x='Gender', y='Score')
plt.title("Score Swarm Plot by Gender")
plt.show()

