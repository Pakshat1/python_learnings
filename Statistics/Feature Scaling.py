#  Feature Scaling
 
# | Type            | Use Case                      |
# | --------------- | ----------------------------- |
# | Min-Max Scaling | Brings values between 0 and 1 |
# | Standardization | Mean = 0, Std Dev = 1         |
# | Robust Scaling  | For data with many outliers   |

# | Method           | Description                                          | When to Use                   |
# | ---------------- | ---------------------------------------------------- | ----------------------------- |
# | Min-Max Scaling  | Rescales values to **0–1**                           | When you need bounded scale   |
# | Standard Scaling | Transforms to **mean=0, std=1**                      | Works well with Gaussian data |
# | Robust Scaling   | Scales using **median and IQR**                      | Best when outliers exist      |
# | MaxAbs Scaling   | Scales between **-1 and 1** using max absolute value | For sparse data               |

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
import os

# Step 1: Create numeric dataset
df = pd.DataFrame({
    'Salary': [30000, 45000, 50000, 52000, 75000, 100000, 120000, 250000],
    'Experience': [1, 3, 4, 6, 8, 12, 20, 25],
    'Age': [22, 25, 28, 30, 35, 40, 50, 60]
})

# Step 2: Apply Scaling
scalers = {
    'MinMax': MinMaxScaler(),
    'Standard': StandardScaler(),
    'Robust': RobustScaler()
}

# Store scaled data
scaled_dfs = {}

for name, scaler in scalers.items():
    scaled = scaler.fit_transform(df)
    scaled_dfs[name] = pd.DataFrame(scaled, columns=[f'{col}_{name}' for col in df.columns])

# Step 3: Combine all into one DataFrame
combined_df = df.copy()
for name in scaled_dfs:
    combined_df = pd.concat([combined_df, scaled_dfs[name]], axis=1)

# Step 4: Save to Excel
output_file = "scaled_data.xlsx"
combined_df.to_excel(output_file, index=False)

print(f" Scaling complete. File saved as '{output_file}'")


