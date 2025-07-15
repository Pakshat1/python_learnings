
# Binning / Discretization of Continuous Data

# Binning means converting continuous numeric values into categories (bins).
# | Original Value | Binned Value |
# | -------------- | ------------ |
# | 23             | 20–30        |
# | 51             | 50–60        |
# | 78             | 70–80        |

# uses 
# | Benefit                          | Explanation                                               |
# | -------------------------------- | --------------------------------------------------------- |
# | Simplifies analysis              | Easier to understand groups instead of raw numbers        |
# | Helps in categorical modeling    | Some ML models work better with categorical values        |
# | Handles outliers more robustly   | Values grouped into ranges reduce sensitivity to extremes |
# | Enables frequency-based plotting | Useful for bar plots, stacked plots, etc.                 |

# types of binning
# | Type             | Description                         | Function               |
# | ---------------- | ----------------------------------- | ---------------------- |
# | Fixed-width bins | Equal ranges (e.g., 0–10, 10–20...) | `pd.cut()`             |
# | Quantile bins    | Equal number of records in each bin | `pd.qcut()`            |
# | Custom bins      | Manually define your bin edges      | `bins=[0, 18, 30, 60]` |

# example 
import pandas as pd
import numpy as np
import os

# Step 1: Create sample data
df = pd.DataFrame({
    'Name': ['Amit', 'Sara', 'Ravi', 'Meera', 'John', 'Priya', 'Raj', 'Zara', 'Dev', 'Sneha'],
    'Age': [17, 22, 29, 31, 35, 41, 50, 60, 65, 72],
    'Salary': [15000, 25000, 35000, 42000, 50000, 62000, 75000, 88000, 95000, 100000]
})

# Step 2: Equal-width bins (Age groups of 20)
df['Age_Bin_Cut'] = pd.cut(df['Age'], bins=[0, 20, 40, 60, 80], labels=['Teen', 'Young Adult', 'Adult', 'Senior'])

# Step 3: Quantile-based bins (4 bins with ~equal count)
df['Salary_Bin_Qcut'] = pd.qcut(df['Salary'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])

# Step 4: Custom bins for Salary
salary_bins = [0, 30000, 60000, 90000, 120000]
salary_labels = ['Low', 'Mid', 'High', 'Top']
df['Salary_Bin_Custom'] = pd.cut(df['Salary'], bins=salary_bins, labels=salary_labels)

# Step 5: Save to Excel
output_file = "binned_data.xlsx"
df.to_excel(output_file, index=False)
print(f"Binning complete. File saved as '{output_file}'")
