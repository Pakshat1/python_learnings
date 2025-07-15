#  Categorical Feature Engineering
import pandas as pd

# Step 1: Create sample dataset
data = {
    'CustomerID': [101, 102, 103, 104, 105],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'City': ['Mumbai', 'Delhi', 'Delhi', 'Bangalore', 'Mumbai'],
    'Product': ['Phone', 'Laptop', 'Tablet', 'Phone', 'Laptop'],
    'Age': [25, 30, 22, 28, 35]
}

df = pd.DataFrame(data)

# Step 2: Detect data types
print("Original dtypes:\n", df.dtypes)

# Step 3: Identify categorical columns (object dtype)
categorical_cols = df.select_dtypes(include='object').columns.tolist()
print("\nCategorical Columns:", categorical_cols)

# Step 4: Convert object columns to 'category' dtype
for col in categorical_cols:
    df[col] = df[col].astype('category')

# Step 5: Check new data types
print("\nUpdated dtypes:\n", df.dtypes)

# Step 6: Check cardinality of categorical columns
print("\nCardinality of categorical columns:")
for col in categorical_cols:
    print(f"- {col}: {df[col].nunique()} unique values")

# Final preview
print("\nFinal DataFrame:\n", df)
