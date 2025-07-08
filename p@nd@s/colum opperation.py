#colum operations

# | No. | Subtopic                            | Method / Function                |
# | --- | ----------------------------------- | -------------------------------- |
# | 1️⃣ | Create a new column                 | `df['NewCol'] = ...`             |
# | 2️⃣ | Modify existing column              | `df['Marks'] = df['Marks'] + 10` |
# | 3️⃣ | Apply function to column            | `.apply()`, `.map()`, `lambda`   |
# | 4️⃣ | Rename columns                      | `df.rename(columns={...})`       |
# | 5️⃣ | Delete a column                     | `df.drop('ColName', axis=1)`     |
# | 6️⃣ | Reorder or select multiple columns  | `df[['col1', 'col2']]`           |
# | 7️⃣ | Insert a column at a specific index | `df.insert(loc, 'Col', value)`   |

# example
import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Marks': [88, 92, 85, 90],
        'Age': [23, 22, 24, 23]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Create new column from existing columns
df['Status'] = df['Marks'] > 90
print("\n1. New column 'Status' (Marks > 90):")
print(df)

# 2. Modify existing column
df['Marks'] = df['Marks'] + 5
print("\n2. Modified 'Marks' column (add 5):")
print(df)

# 3. Apply function to column (using apply + lambda)
df['Grade'] = df['Marks'].apply(lambda x: 'A' if x >= 95 else 'B')
print("\n3. Apply function to 'Marks' to get 'Grade':")
print(df)

# 4. Rename columns
df = df.rename(columns={'Name': 'StudentName', 'Marks': 'Score'})
print("\n4. Renamed columns:")
print(df)

# 5. Delete a column
df = df.drop('Status', axis=1)
print("\n5. Dropped column 'Status':")
print(df)

# 6. Reorder/select specific columns
df = df[['StudentName', 'Score', 'Age', 'Grade']]
print("\n6. Reordered columns:")
print(df)

# 7. Insert a column at position 1
df.insert(1, 'City', ['Delhi', 'Mumbai', 'Pune', 'Chennai'])
print("\n7. Inserted column 'City' at position 1:")
print(df)

# output
# Original DataFrame:
#       Name  Marks  Age
# 0    Alice     88   23
# 1      Bob     92   22
# 2  Charlie     85   24
# 3    David     90   23

# 1. New column 'Status' (Marks > 90):
#       Name  Marks  Age  Status
# 0    Alice     88   23   False
# 1      Bob     92   22    True
# 2  Charlie     85   24   False
# 3    David     90   23   False

# 2. Modified 'Marks' column (add 5):
#       Name  Marks  Age  Status
# 0    Alice     93   23   False
# 1      Bob     97   22    True
# 2  Charlie     90   24   False
# 3    David     95   23   False

# 3. Apply function to 'Marks' to get 'Grade':
#       Name  Marks  Age  Status Grade
# 0    Alice     93   23   False     B
# 1      Bob     97   22    True     A
# 2  Charlie     90   24   False     B
# 3    David     95   23   False     A

# 4. Renamed columns:
#   StudentName  Score  Age  Status Grade
# 0       Alice     93   23   False     B
# 1         Bob     97   22    True     A
# 2     Charlie     90   24   False     B
# 3       David     95   23   False     A

# 5. Dropped column 'Status':
#   StudentName  Score  Age Grade
# 0       Alice     93   23     B
# 1         Bob     97   22     A
# 2     Charlie     90   24     B
# 3       David     95   23     A

# 6. Reordered columns:
#   StudentName  Score  Age Grade
# 0       Alice     93   23     B
# 1         Bob     97   22     A
# 2     Charlie     90   24     B
# 3       David     95   23     A

# 7. Inserted column 'City' at position 1:
#   StudentName     City  Score  Age Grade
# 0       Alice    Delhi     93   23     B
# 1         Bob   Mumbai     97   22     A
# 2     Charlie     Pune     90   24     B
# 3       David  Chennai     95   23     A
