

# | Operation  | Purpose                                         |
# | ---------- | ----------------------------------------------- |
# | `concat()` | Stack DataFrames **vertically or horizontally** |
# | `merge()`  | Combine DataFrames **like SQL joins** (on keys) |
# | `join()`   | Join DataFrames using index or key column       |

import pandas as pd

# DataFrames for demo
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Marks': [88, 92, 85]
})

df3 = pd.DataFrame({
    'Age': [21, 22, 23]
}, index=[0, 1, 2])

# 1. Merge → Join on 'ID'
merged = pd.merge(df1, df2, on='ID', how='inner')  # common rows only

# 2. Concat → Stack vertically (add more rows)
concat_vertical = pd.concat([df1, df2], axis=0, ignore_index=True)

# 3. Concat → Stack side-by-side (add more columns)
concat_horizontal = pd.concat([df1, df3], axis=1)

print("🔹 Merge (inner join on ID):")
print(merged)

print("\n🔹 Concat Vertical:")
print(concat_vertical)

print("\n🔹 Concat Horizontal:")
print(concat_horizontal)



#######################

# Other how= Join Types (Context)
# | `how` type | Description                                    | Result Includes                |
# | ---------- | ---------------------------------------------- | ------------------------------ |
# | `'inner'`  | Only keys common to both DataFrames            | Intersect of keys              |
# | `'left'`   | All keys from left DataFrame, match from right | Left full, right partial       |
# | `'right'`  | All keys from right DataFrame, match from left | Right full, left partial       |
# | `'outer'`  | All keys from both DataFrames                  | Union of keys, unmatched → NaN |

# 1. Inner Join – Only matching IDs
inner = pd.merge(df1, df2, on='ID', how='inner')

# 2. Left Join – All from df1, match from df2
left = pd.merge(df1, df2, on='ID', how='left')

# 3. Right Join – All from df2, match from df1
right = pd.merge(df1, df2, on='ID', how='right')

# 4. Outer Join – All IDs from both, NaN where missing
outer = pd.merge(df1, df2, on='ID', how='outer')

# Print all results
print("🔸 Inner Join:")
print(inner)
print("\n🔸 Left Join:")
print(left)
print("\n🔸 Right Join:")
print(right)
print("\n🔸 Outer Join:")
print(outer)
