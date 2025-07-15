
# Data Transformation & Feature Engineering

# | #   | Topic                             | Use Case                                                    |
# | --- | --------------------------------- | ----------------------------------------------------------- |
# | 1️⃣ | Encoding categorical variables    | Convert strings to numbers (for ML models)                  |
# | 2️⃣ | Binning / discretization          | Turn continuous values into ranges (e.g., Age → Age groups) |
# | 3️⃣ | Feature scaling                   | Normalize or standardize numeric values                     |
# | 4️⃣ | Feature extraction from DateTime  | Extract Year, Month, Day, Hour, Weekday from timestamps     |
# | 5️⃣ | Creating new columns              | Combine, subtract, or transform columns for new insight     |
# | 6️⃣ | Log and Box-Cox transformation    | Normalize skewed distributions                              |
# | 7️⃣ | Label encoding / one-hot encoding | Machine-learning-friendly format for text features          |

import pandas as pd

df = pd.DataFrame({
    'Gender': ['Male', 'Female', 'Female', 'Male'],
    'Education': ['High School', 'Bachelors', 'Masters', 'PhD']
})

# Example: Encode Education if it has order
education_order = ['High School', 'Bachelors', 'Masters', 'PhD']
df['Education_encoded'] = df['Education'].astype('category').cat.set_categories(education_order, ordered=True).cat.codes

df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=True)



###########################################4

import pandas as pd
import numpy as np
import os

# Step 1: Create moderate sample data
data = {
    'Name': ['Amit', 'Sara', 'Ravi', 'Meera', 'John', 'Priya', 'Raj', 'Nina', 'Karan', 'Zara',
             'Dev', 'Tina', 'Ali', 'Sneha', 'Tom', 'Riya', 'Parth', 'Isha', 'Kabir', 'Fatima'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female',
               'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Education': ['Bachelors', 'Masters', 'High School', 'PhD', 'Masters', 'High School', 'PhD', 'Bachelors',
                  'Masters', 'PhD', 'Bachelors', 'Masters', 'High School', 'PhD', 'High School', 'Masters',
                  'Bachelors', 'Bachelors', 'PhD', 'Masters'],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT',
                   'Finance', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR', 'IT', 'HR', 'Finance']
}

df = pd.DataFrame(data)

# Save original data to Excel
original_file = "employee_data.xlsx"
df.to_excel(original_file, index=False)
print(f"Sample file '{original_file}' created with {len(df)} rows.")

# Step 2: Label Encoding for Education (ordinal)
education_order = ['High School', 'Bachelors', 'Masters', 'PhD']
df['Education_Encoded'] = df['Education'].astype('category') \
                          .cat.set_categories(education_order, ordered=True) \
                          .cat.codes

# Step 3: One-Hot Encoding for Gender and Department
df_encoded = pd.get_dummies(df, columns=['Gender', 'Department'], drop_first=True)

# Step 4: Save encoded data to new Excel file
encoded_file = "employee_data_encoded.xlsx"
df_encoded.to_excel(encoded_file, index=False)
print(f" Encoded file saved as '{encoded_file}'")