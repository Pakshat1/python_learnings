# filtering data(boolean conditions)

import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Marks': [88, 92, 85, 90],
        'Age': [23, 22, 24, 23]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Single Condition: Marks > 85
print("\n1. Marks > 85:")
print(df[df['Marks'] > 85])

# 2. Multiple Conditions: Marks > 85 AND Age < 24
print("\n2. Marks > 85 AND Age < 24:")
print(df[(df['Marks'] > 85) & (df['Age'] < 24)])

# 3. OR Condition: Marks > 90 OR Age == 23
print("\n3. Marks > 90 OR Age == 23:")
print(df[(df['Marks'] > 90) | (df['Age'] == 23)])

# 4. Using isin()
print("\n4. Name is Alice or David:")
print(df[df['Name'].isin(['Alice', 'David'])])

# 5. Using between()
print("\n5. Marks between 85 and 90:")
print(df[df['Marks'].between(85, 90)])

# 6. Using query()
print("\n6. Using query() method (Marks > 85 and Age < 24):")
print(df.query("Marks > 85 and Age < 24"))


# # output 
# Original DataFrame:
#       Name  Marks  Age
# 0    Alice     88   23
# 1      Bob     92   22
# 2  Charlie     85   24
# 3    David     90   23

# 1. Marks > 85:
#     Name  Marks  Age
# 0  Alice     88   23
# 1    Bob     92   22
# 3  David     90   23

# 2. Marks > 85 AND Age < 24:
#     Name  Marks  Age
# 0  Alice     88   23
# 1    Bob     92   22
# 3  David     90   23

# 3. Marks > 90 OR Age == 23:
#     Name  Marks  Age
# 0  Alice     88   23
# 1    Bob     92   22
# 3  David     90   23

# 4. Name is Alice or David:
#     Name  Marks  Age
# 0  Alice     88   23
# 3  David     90   23

# 5. Marks between 85 and 90:
#       Name  Marks  Age
# 0    Alice     88   23
# 2  Charlie     85   24
# 3    David     90   23

# 6. Using query() method (Marks > 85 and Age < 24):
#     Name  Marks  Age
# 0  Alice     88   23
# 1    Bob     92   22
# 3  David     90   23