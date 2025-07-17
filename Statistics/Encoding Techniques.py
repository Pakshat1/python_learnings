# Encoding Techniques


# one-hot encoding 

import pandas as pd

# Recreate the same dataset (or reuse if already defined)
data = {
    'CustomerID': [101, 102, 103, 104, 105],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'City': ['Mumbai', 'Delhi', 'Delhi', 'Bangalore', 'Mumbai'],
    'Product': ['Phone', 'Laptop', 'Tablet', 'Phone', 'Laptop'],
    'Age': [25, 30, 22, 28, 35]
}
df = pd.DataFrame(data)

#  One-Hot Encode 'Gender' and 'City'
df_encoded = pd.get_dummies(df, columns=['Gender', 'City'], drop_first=True)

# Show result
print(df_encoded)
