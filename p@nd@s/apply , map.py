# 
# | Method        | Use Case                                            | Applies To         |
# | ------------- | --------------------------------------------------- | ------------------ |
# | `.map()`      | Element-wise operations on a **Series**             | Series only        |
# | `.apply()`    | Row-wise or column-wise operations on **DataFrame** | Series & DataFrame |
# | `.applymap()` | Element-wise operation on **entire DataFrame**      | DataFrame only     |

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [88, 92, 85],
    'Age': [23, 22, 24]
})

# map: uppercase names
df['Name'] = df['Name'].map(str.upper)

# apply: add 5 to each mark
df['Updated_Marks'] = df['Marks'].apply(lambda x: x + 5)

# apply: status based on marks
df['Status'] = df.apply(lambda row: 'Pass' if row['Marks'] >= 90 else 'Fail', axis=1)

# deprecated: df_numeric.applymap(...)
# FIXED: use .map() on each column
df_numeric = df[['Marks', 'Age']].copy()
df_numeric['Marks'] = df_numeric['Marks'].map(lambda x: x * 2)
df_numeric['Age'] = df_numeric['Age'].map(lambda x: x * 2)

print(df)
print("\nNumeric columns doubled:")
print(df_numeric)

# output 
#       Name  Marks  Age  Updated_Marks Status
# 0    ALICE     88   23             93   Fail
# 1      BOB     92   22             97   Pass
# 2  CHARLIE     85   24             90   Fail

# Numeric columns doubled:
#    Marks  Age
# 0    176   46
# 1    184   44
# 2    170   48  

