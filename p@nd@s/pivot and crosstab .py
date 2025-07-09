
import pandas as pd

# Sample employee dataset
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'HR'],
    'Gender': ['F', 'M', 'M', 'F', 'F', 'F'],
    'Salary': [50000, 60000, 52000, 62000, 70000, 51000]
}

df = pd.DataFrame(data)
print(" Original DataFrame:")
print(df)

# pivot 
pivot = pd.pivot_table(df,
                       index='Department',     # rows
                       columns='Gender',       # columns
                       values='Salary',        # what to calculate
                       aggfunc='mean')         # how to calculate

print("\n Pivot Table: Average Salary by Department & Gender")
print(pivot)

# crosstab
cross = pd.crosstab(df['Department'], df['Gender'])

print("\n Crosstab: Employee Count by Department & Gender")
print(cross)

# output
#  Original DataFrame:
#   Employee Department Gender  Salary
# 0    Alice         HR      F   50000
# 1      Bob         IT      M   60000
# 2  Charlie         HR      M   52000
# 3    David         IT      F   62000
# 4      Eva    Finance      F   70000
# 5    Frank         HR      F   51000

#  Pivot Table: Average Salary by Department & Gender
# Gender            F        M
# Department
# Finance     70000.0      NaN
# HR          50500.0  52000.0
# IT          62000.0  60000.0

#  Crosstab: Employee Count by Department & Gender
# Gender      F  M
# Department
# Finance     1  0
# HR          2  1

# multiple pivot 
import pandas as pd

# Sample data
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'Finance', 'HR'],
    'Gender': ['F', 'M', 'M', 'F', 'F', 'F'],
    'Salary': [50000, 60000, 52000, 62000, 70000, 51000]
}
df = pd.DataFrame(data)

# Pivot with multiple aggregations
pivot_multi = pd.pivot_table(df,
                              index='Department',
                              columns='Gender',
                              values='Salary',
                              aggfunc=['mean', 'min', 'max'])   #  Multiple stats

# Display results
print(" Pivot Table with Mean, Min, and Max Salary:")
print(pivot_multi)
