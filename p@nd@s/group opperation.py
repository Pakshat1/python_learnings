import pandas as pd

# The groupby() function in Pandas lets you group rows by a column value,
#  then perform aggregations like sum, mean, count, min, max,

# Sample DataFrame| Task                          | Code Example                              |
# | ----------------------------- | ----------------------------------------- |
# | Group by one column           | `df.groupby('Department')`                |
# | Aggregate with mean/sum/count | `df.groupby('Dept')['Salary'].mean()`     |
# | Multiple aggregations         | `df.groupby('Dept').agg(['mean', 'max'])` |
# | Group by multiple columns     | `df.groupby(['Dept', 'Gender'])`          |
# | Reset index after groupby     | `grouped.reset_index()`                   |

data = {
    'Dept': ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance', 'IT'],
    'Gender': ['F', 'M', 'M', 'F', 'F', 'M', 'M'],
    'Salary': [50000, 60000, 52000, 61000, 70000, 72000, 63000]
}
df = pd.DataFrame(data)

# Group by one column
grouped_dept = df.groupby('Dept')
print("Group by Dept:\n", grouped_dept.size())

# Aggregate with mean
mean_salary = df.groupby('Dept')['Salary'].mean()
print("\nMean Salary by Dept:\n", mean_salary)

# Multiple aggregations
agg_salary = df.groupby('Dept')['Salary'].agg(['mean', 'max'])
print("\nMean and Max Salary by Dept:\n", agg_salary)

# Group by multiple columns
grouped_multi = df.groupby(['Dept', 'Gender'])['Salary'].mean()
print("\nMean Salary by Dept and Gender:\n", grouped_multi)

# Reset index after groupby
reset_df = grouped_multi.reset_index()
print("\nReset index:\n", reset_df)


# output
# Group by Dept:
#  Dept
# Finance    2
# HR         2
# IT         3
# dtype: int64

# Mean Salary by Dept:
#  Dept
# Finance    71000.000000
# HR         51000.000000
# IT         61333.333333
# Name: Salary, dtype: float64

# Mean and Max Salary by Dept:
#                   mean    max
# Dept
# Finance  71000.000000  72000
# HR       51000.000000  52000
# IT       61333.333333  63000

# Mean Salary by Dept and Gender:
#  Dept     Gender
# Finance  F         70000.0
#          M         72000.0
# HR       F         50000.0
#          M         52000.0
# IT       F         61000.0
#          M         61500.0
# Name: Salary, dtype: float64

# Reset index:
#        Dept Gender   Salary
# 0  Finance      F  70000.0
# 1  Finance      M  72000.0
# 2       HR      F  50000.0
# 3       HR      M  52000.0
# 4       IT      F  61000.0
# 5       IT      M  61500.0  
