# sorthing and ranking

import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Marks': [88, 92, 85, 90],
        'Age': [23, 22, 24, 23]}
df = pd.DataFrame(data, index=[3, 1, 4, 2])
print("Original DataFrame:")
print(df)

# 1. Sort by Index (rows)
sorted_index = df.sort_index()
print("\n1. Sorted by Index (rows):")
print(sorted_index)

# 2. Sort by Index (columns)
sorted_col = df.sort_index(axis=1)
print("\n2. Sorted by Index (columns):")
print(sorted_col)

# 3. Sort by a single column (Marks)
sorted_marks = df.sort_values(by='Marks')
print("\n3. Sorted by Marks (ascending):")
print(sorted_marks)

# 4. Sort by Marks (descending)
sorted_marks_desc = df.sort_values(by='Marks', ascending=False)
print("\n4. Sorted by Marks (descending):")
print(sorted_marks_desc)

# 5. Multi-column sort: by Marks (asc), then Age (desc)
multi_sort = df.sort_values(by=['Marks', 'Age'], ascending=[True, False])
print("\n5. Sorted by Marks (asc), then Age (desc):")
print(multi_sort)

# 6. Ranking: Assign rank to Marks
df['Marks_Rank'] = df['Marks'].rank()
print("\n6. Rank based on Marks (default: average rank):")
print(df)

# output
# Original DataFrame:
#       Name  Marks  Age
# 3    Alice     88   23
# 1      Bob     92   22
# 4  Charlie     85   24
# 2    David     90   23

# 1. Sorted by Index (rows):
#       Name  Marks  Age
# 1      Bob     92   22
# 2    David     90   23
# 3    Alice     88   23
# 4  Charlie     85   24

# 2. Sorted by Index (columns):
#    Age  Marks     Name
# 3   23     88    Alice
# 1   22     92      Bob
# 4   24     85  Charlie
# 2   23     90    David

# 3. Sorted by Marks (ascending):
#       Name  Marks  Age
# 4  Charlie     85   24
# 3    Alice     88   23
# 2    David     90   23
# 1      Bob     92   22

# 4. Sorted by Marks (descending):
#       Name  Marks  Age
# 1      Bob     92   22
# 2    David     90   23
# 3    Alice     88   23
# 4  Charlie     85   24

# 5. Sorted by Marks (asc), then Age (desc):
#       Name  Marks  Age
# 4  Charlie     85   24
# 3    Alice     88   23
# 2    David     90   23
# 1      Bob     92   22

# 6. Rank based on Marks (default: average rank):
#       Name  Marks  Age  Marks_Rank
# 3    Alice     88   23         2.0
# 1      Bob     92   22         4.0
# 4  Charlie     85   24         1.0
# 2    David     90   23         3.0

# Rank_average: Ties get the average of their rank positions.
# Rank_min: Ties get the lowest rank in the group.
# Rank_max: Ties get the highest rank in the group.
# Rank_first: Ranks based on first appearance in the DataFrame.
# Rank_dense: Like min, but doesn’t skip ranks after ties.

import pandas as pd

# Sample data: Student scores
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Score': [95, 85, 85, 80, 75, 75]
}
df = pd.DataFrame(data)

# Apply different ranking methods
df['Rank_average'] = df['Score'].rank(method='average', ascending=True)
df['Rank_min'] = df['Score'].rank(method='min', ascending=True)
df['Rank_max'] = df['Score'].rank(method='max', ascending=True)
df['Rank_first'] = df['Score'].rank(method='first', ascending=True)
df['Rank_dense'] = df['Score'].rank(method='dense', ascending=True)

# Display result
print(df)


# output
#   Student  Score  Rank_average  Rank_min  Rank_max  Rank_first  Rank_dense
# 0   Alice     95           6.0       6.0       6.0         6.0         5.0
# 1     Bob     85           4.5       4.0       5.0         4.0         4.0
# 2 Charlie     85           4.5       4.0       5.0         5.0         4.0
# 3   David     80           3.0       3.0       3.0         3.0         3.0
# 4     Eva     75           1.5       1.0       2.0         1.0         2.0
# 5   Frank     75           1.5       1.0       2.0         2.0         2.0

