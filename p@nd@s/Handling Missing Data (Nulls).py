# Handling Missing Data (Nulls)

import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [17, np.nan, 16, 19, 15],
    'Gender': ['F', 'M', None, 'M', 'F'],
    'Marks': [88, 76, np.nan, 67, 90]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df, "\n")

# 1. Detect missing values
print("Missing value map (True means missing):\n", df.isnull(), "\n")
print("Count of missing values per column:\n", df.isnull().sum(), "\n")

# 2. Drop rows with any missing values
df_dropped = df.dropna()
print("After dropping rows with any missing values:\n", df_dropped, "\n")

# 3. Fill missing values with fixed values
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': 0,
    'Gender': 'Unknown',
    'Marks': df['Marks'].mean()
})
print("After filling missing values:\n", df_filled, "\n")

# 4. Forward Fill (no warning)
df_ffill = df.ffill()
print("Forward fill (propagate previous value):\n", df_ffill, "\n")

# 5. Backward Fill (no warning)
df_bfill = df.bfill()
print("Backward fill (use next value):\n", df_bfill, "\n")

# 6. Interpolation (numeric columns only)
df_interpolated = df.copy()
df_interpolated['Marks'] = df_interpolated['Marks'].interpolate()
df_interpolated['Age'] = df_interpolated['Age'].interpolate()
print("Interpolated DataFrame:\n", df_interpolated, "\n")
