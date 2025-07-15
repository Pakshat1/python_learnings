
#  Data Cleaning & Preprocessing
# | Topic                              | Description                                |
# | ---------------------------------- | ------------------------------------------ |
# | Missing values                     | Detect, remove, or fill NaNs               |
# | Duplicates                         | Find and remove duplicates                 |
# | Outlier detection                  | Use IQR or Z-score to remove/fix anomalies |
# | Data type conversion               | Fix wrong types (e.g., object → numeric)   |
# | Scaling / Normalization (optional) | Prepare numeric values for ML              |
# | Encoding categorical variables     | Use label or one-hot encoding              |

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Example DataFrame
df = pd.DataFrame({
    'age': [25, np.nan, 30, 22, 40, 22],
    'salary': [50000, 60000, np.nan, 52000, 58000, 52000],
    'gender': ['M', 'F', 'F', 'M', 'F', 'M'],
    'city': ['NY', 'LA', 'NY', 'NY', 'LA', 'NY']
})

# 1. Missing values: Fill NaNs with mean
df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)

# 2. Duplicates: Remove duplicate rows
df = df.drop_duplicates()

# 3. Outlier detection: Remove outliers in 'age' using IQR
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['age'] >= Q1 - 1.5 * IQR) & (df['age'] <= Q3 + 1.5 * IQR)]

# 4. Data type conversion: Ensure 'salary' is float
df['salary'] = df['salary'].astype(float)

# 5. Scaling / Normalization: Standardize 'salary'
scaler = StandardScaler()
df['salary_scaled'] = scaler.fit_transform(df[['salary']])

# 6. Encoding categorical variables: One-hot encode 'city'
df = pd.get_dummies(df, columns=['city'])

print(df)

##########################################################


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk
import os

# === Step 1: File Selection ===
Tk().withdraw()
file_path = filedialog.askopenfilename(
    title="Select a CSV or Excel file",
    filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xls")]
)

if not file_path:
    print("No file selected.")
    exit()

# === Step 2: Load File ===
if file_path.endswith('.csv'):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

print(f"\nFile loaded: {os.path.basename(file_path)}")

# === Step 3: Clean Column Names (strip spaces) ===
df.columns = df.columns.str.strip()

# === Step 4: Drop Duplicate Rows ===
df.drop_duplicates(inplace=True)

# === Step 5: Strip Whitespace from String Columns ===
str_cols = df.select_dtypes(include='object').columns
df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

# === Step 6: Fix Data Types ===
for col in df.columns:
    # Convert numeric strings to actual numbers
    if df[col].dtype == 'object':
        try:
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except:
            continue

# === Step 7: Handle Missing Values ===
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype in [np.float64, np.int64]:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

# === Step 8: Standardize Categorical Text ===
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col] = df[col].str.lower()

# === Step 9: Remove Outliers (Numeric Columns) ===
num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

# === Step 10: Save Cleaned File ===
cleaned_file = os.path.splitext(file_path)[0] + "_cleaned.xlsx"
df.to_excel(cleaned_file, index=False)

print("\nData cleaning complete.")
print(f"Cleaned file saved as: {cleaned_file}")




