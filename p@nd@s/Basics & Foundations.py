import pandas as pd

# Basics & Foundations

# example of serise

import pandas as pd

# 1. Series from a list
data_list = [10, 20, 30, 40]
s1 = pd.Series(data_list)
print("🔹 Series from list:\n", s1, "\n")

# 2. Series with custom index
s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print("🔹 Series with custom index:\n", s2, "\n")

# 3. Series from a dictionary
fruit_dict = {'apple': 5, 'banana': 3, 'mango': 8}
s3 = pd.Series(fruit_dict)
print("🔹 Series from dictionary:\n", s3, "\n")

# 4. Series Attributes
print("🔹 Attributes of fruit Series:")
print("Index labels:", s3.index)
print("Values:", s3.values)
print("Data type:", s3.dtype)
print("Shape:", s3.shape, "\n")

# 5. Vectorized operations
print("🔹 Vectorized Operations:")
print("Multiply by 2:\n", s3 * 2)
print("Add 10:\n", s3 + 10)
print("Greater than 5:\n", s3 > 5)


# Data frames
# Creating a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Accessing a column
print(df['Name'])

# Basic statistics
print(df.describe())

# Adding a new column
df['Country'] = ['USA', 'France', 'UK']
print(df)

# Filtering rows where Age > 28
filtered_df = df[df['Age'] > 28]
print(filtered_df)

import pandas as pd

# 1. Create DataFrame from dictionary of lists
data1 = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'math': [85, 90, 78],
    'science': [92, 88, 75]
}
df1 = pd.DataFrame(data1)
print("🔹 DataFrame from dict of lists:\n", df1, "\n")

# 2. Create DataFrame from list of dictionaries
data2 = [
    {'name': 'David', 'math': 82},
    {'name': 'Eve', 'math': 95, 'science': 91}
]
df2 = pd.DataFrame(data2)
print("🔹 DataFrame from list of dicts:\n", df2, "\n")

# 3. Accessing Columns
print("🔹 Math column:\n", df1['math'], "\n")

# 4. Accessing Rows
print("🔹 First row using loc:\n", df1.loc[0], "\n")
print("🔹 Second row using iloc:\n", df1.iloc[1], "\n")

# 5. Access single value
print("🔹 Access cell [1, 'science'] using at:\n", df1.at[1, 'science'])
print("🔹 Access same using iat:\n", df1.iat[1, 2], "\n")

# 6. Modify Data
df1['total'] = df1['math'] + df1['science']  # Add new column
df1.loc[2, 'math'] = 80                      # Update Charlie's math
print("🔹 Modified DataFrame:\n", df1, "\n")

# 7. Attributes and Summary
print("🔹 Shape:", df1.shape)
print("🔹 Columns:", df1.columns)
print("🔹 Dtypes:\n", df1.dtypes)
print("🔹 Info:")
df1.info()
print("\n🔹 Description:\n", df1.describe())

