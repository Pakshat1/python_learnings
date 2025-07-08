# Reading and Writing Data (File I/O)
import pandas as pd

# Step 1: Create sample data
data = {
    'ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [17, 21, 16, 19, 15],
    'Gender': ['F', 'M', 'M', 'M', 'F'],
    'Marks': [88, 76, 95, 67, 90]
}
df = pd.DataFrame(data)

# Step 2: Save to CSV and Excel
df.to_csv('students_data.csv', index=False)
df.to_excel('students_data.xlsx', index=False)

print(" CSV and Excel files saved successfully.")

# Step 3: Read both files back
df_csv = pd.read_csv('students_data.csv')
df_excel = pd.read_excel('students_data.xlsx')

# Step 4: Filter students under 18
filtered_df = df_csv[df_csv['Age'] < 18]

print("\n Students under 18:\n", filtered_df)

# Step 5: Save filtered result
filtered_df.to_csv('students_under_18.csv', index=False)
filtered_df.to_excel('students_under_18.xlsx', index=False)

print("\n Filtered data saved to 'students_under_18.csv' and 'students_under_18.xlsx'")

# output
#  CSV and Excel files saved successfully.

#  Students under 18:
#      ID     Name  Age Gender  Marks
# 0  101    Alice   17      F     88
# 2  103  Charlie   16      M     95
# 4  105      Eva   15      F     90


################################################################

import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv("students_data.csv")
print("🔹 Original Data:\n", df, "\n")

# Step 2: Filter students with Marks > 85
high_scorers = df[df['Marks'] > 85]
print("🔹 Students with Marks > 85:\n", high_scorers, "\n")

# Step 3: Select only 'Name' and 'Marks'
selected_columns = df[['Name', 'Marks']]
print("🔹 Name and Marks Columns:\n", selected_columns, "\n")

# Step 4: Sort by Marks descending
df_sorted = df.sort_values(by='Marks', ascending=False)
print("🔹 Sorted by Marks (High to Low):\n", df_sorted, "\n")

# Step 5: Add 'Grade' column
def assign_grade(m):
    if m >= 90:
        return 'A'
    elif m >= 80:
        return 'B'
    elif m >= 70:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Marks'].apply(assign_grade)
print("🔹 Grade Added:\n", df, "\n")

# Step 6: Group by Gender → average Marks
avg_by_gender = df.groupby('Gender')['Marks'].mean()
print("🔹 Average Marks by Gender:\n", avg_by_gender, "\n")

# Step 7: Rename 'Marks' to 'Score'
df_renamed = df.rename(columns={'Marks': 'Score'})
print("🔹 Renamed 'Marks' to 'Score':\n", df_renamed.head(), "\n")

# Step 8: Drop column 'ID'
df_dropped = df.drop(columns=['ID'])
print("🔹 Dropped 'ID' column:\n", df_dropped.head(), "\n")

# Step 9: Replace Gender codes
df['Gender'] = df['Gender'].replace({'F': 'Female', 'M': 'Male'})
print("🔹 Gender Replaced:\n", df, "\n")

# Step 10: Describe summary stats
print("🔹 Summary Statistics:\n", df.describe(), "\n")

# Step 11: Filter: Female students under 18
fem_kids = df[(df['Gender'] == 'Female') & (df['Age'] < 18)]
print("🔹 Female Students Under 18:\n", fem_kids, "\n")

# output
#  Filtered data saved to 'students_under_18.csv' and 'students_under_18.xlsx'
# 🔹 Original Data:
#      ID     Name  Age Gender  Marks
# 0  101    Alice   17      F     88
# 1  102      Bob   21      M     76
# 2  103  Charlie   16      M     95
# 3  104    David   19      M     67
# 4  105      Eva   15      F     90

# 🔹 Students with Marks > 85:
#      ID     Name  Age Gender  Marks
# 0  101    Alice   17      F     88
# 2  103  Charlie   16      M     95
# 4  105      Eva   15      F     90

# 🔹 Name and Marks Columns:
#        Name  Marks
# 0    Alice     88
# 1      Bob     76
# 2  Charlie     95
# 3    David     67
# 4      Eva     90

# 🔹 Sorted by Marks (High to Low):
#      ID     Name  Age Gender  Marks
# 2  103  Charlie   16      M     95
# 4  105      Eva   15      F     90
# 0  101    Alice   17      F     88
# 1  102      Bob   21      M     76
# 3  104    David   19      M     67

# 🔹 Grade Added:
#      ID     Name  Age Gender  Marks Grade
# 0  101    Alice   17      F     88     B
# 1  102      Bob   21      M     76     C
# 2  103  Charlie   16      M     95     A
# 3  104    David   19      M     67     D
# 4  105      Eva   15      F     90     A

# 🔹 Average Marks by Gender:
#  Gender
# F    89.000000
# M    79.333333
# Name: Marks, dtype: float64

# 🔹 Renamed 'Marks' to 'Score':
#      ID     Name  Age Gender  Score Grade
# 0  101    Alice   17      F     88     B
# 1  102      Bob   21      M     76     C
# 2  103  Charlie   16      M     95     A
# 3  104    David   19      M     67     D
# 4  105      Eva   15      F     90     A

# 🔹 Dropped 'ID' column:
#        Name  Age Gender  Marks Grade
# 0    Alice   17      F     88     B
# 1      Bob   21      M     76     C
# 2  Charlie   16      M     95     A
# 3    David   19      M     67     D
# 4      Eva   15      F     90     A

# 🔹 Gender Replaced:
#      ID     Name  Age  Gender  Marks Grade
# 0  101    Alice   17  Female     88     B
# 1  102      Bob   21    Male     76     C
# 2  103  Charlie   16    Male     95     A
# 3  104    David   19    Male     67     D
# 4  105      Eva   15  Female     90     A

# 🔹 Summary Statistics:
#                 ID        Age     Marks
# count    5.000000   5.000000   5.00000
# mean   103.000000  17.600000  83.20000
# std      1.581139   2.408319  11.43241
# min    101.000000  15.000000  67.00000
# 25%    102.000000  16.000000  76.00000
# 50%    103.000000  17.000000  88.00000
# 75%    104.000000  19.000000  90.00000
# max    105.000000  21.000000  95.00000  

# 🔹 Female Students Under 18:
#      ID   Name  Age  Gender  Marks Grade
# 0  101  Alice   17  Female     88     B
# 4  105    Eva   15  Female     90     A