import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['x', 'y', 'z']
})

# Insert a new row
new_row = {'A': 4, 'B': 'w'}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Update a row (e.g., set B='updated' where A==2)
df.loc[df['A'] == 2, 'B'] = 'updated'

# Drop a row (e.g., drop row where A==3)
df = df[df['A'] != 3]

print(df)


# | No. | Subtopic                    | Method / Example                                 |
# | --- | --------------------------- | ------------------------------------------------ |
# | 1️⃣ | Select row by index/label   | `df.loc[2]`, `df.iloc[0]`                        |
# | 2️⃣ | Add a new row (dict or loc) | `df.loc[len(df)] = {...}`                        |
# | 3️⃣ | Modify existing row         | `df.loc[1, 'Marks'] = 95`                        |
# | 4️⃣ | Drop a row                  | `df.drop(index)`                                 |
# | 5️⃣ | Filter out multiple rows    | `df.drop([1, 2])`                                |
# | 6️⃣ | Reset row index             | `df.reset_index(drop=True)`                      |
# | 7️⃣ | Append row (deprecated)     | Use `pd.concat([df, new_df], ignore_index=True)` |

# Examples of common row operations in pandas

# 1️⃣ Select row by index/label
print("Select row by label (A==4):")
print(df.loc[df['A'] == 4])
print("Select row by integer index (first row):")
print(df.iloc[0])

# 2️⃣ Add a new row using loc
df.loc[len(df)] = {'A': 5, 'B': 'new'}
print("\nAfter adding a new row:")
print(df)

# 3️⃣ Modify existing row
df.loc[df['A'] == 4, 'B'] = 'modified'
print("\nAfter modifying row where A==4:")
print(df)

# 4️⃣ Drop a row by index
df = df.drop(df.index[0])
print("\nAfter dropping the first row:")
print(df)

# 5️⃣ Filter out multiple rows by index
df = df.drop(df.index[[0, 1]])
print("\nAfter dropping multiple rows (by index):")
print(df)

# 6️⃣ Reset row index
df = df.reset_index(drop=True)
print("\nAfter resetting index:")
print(df)

# 7️⃣ Append row (using pd.concat, since append is deprecated)
new_row_df = pd.DataFrame([{'A': 6, 'B': 'concat'}])
df = pd.concat([df, new_row_df], ignore_index=True)
print("\nAfter appending a row using concat:")
print(df)


