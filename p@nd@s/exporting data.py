# 
# Export DataFrames to files for storage, sharing, or further processing (CSV, Excel, etc.)

# After cleaning or analyzing your data, you often want to save the result to a file like:
# .csv for compatibility
# .xlsx for Excel use
# .json for APIs
# .html or .sql for web/databases

# Common Export Methods
# | Format     | Method          |
# | ---------- | --------------- |
# | CSV        | `df.to_csv()`   |
# | Excel      | `df.to_excel()` |
# | JSON       | `df.to_json()`  |
# | HTML Table | `df.to_html()`  |
# | SQL Table  | `df.to_sql()`   |

# 🧪 Scenario:
# You're analyzing employee data, calculating total compensation,
#  and now you want to export the result to different file formats.

import pandas as pd
import os

# Step 1: Define export folder path
export_path = r"C:\Users\patel\OneDrive\Documents\python\python_learnings\p@nd@s"

# Step 2: Make sure the folder exists
if not os.path.exists(export_path):
    os.makedirs(export_path)

# Step 3: Create DataFrame
df = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'HR'],
    'Base Salary': [50000, 60000, 70000, 52000],
    'Bonus': [5000, 7000, 6000, 4000]
})

# Step 4: Calculate Total Pay
df['Total Pay'] = df['Base Salary'] + df['Bonus']

# Step 5: Prepare export file paths
csv_file   = os.path.join(export_path, 'employees.csv')
json_file  = os.path.join(export_path, 'employees.json')
excel_file = os.path.join(export_path, 'employees.xlsx')

# Step 6: Export to CSV
df.to_csv(csv_file, index=False)

# Step 7: Export to Excel with 2 sheets
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='All Data', index=False)

    # Calculate department-wise averages (numeric only)
    dept_avg = df.groupby('Department')[['Base Salary', 'Bonus', 'Total Pay']].mean().reset_index()
    dept_avg.to_excel(writer, sheet_name='Dept Avg', index=False)

# Step 8: Export to JSON
df.to_json(json_file, orient='records', indent=2)

# Step 9: Confirm
print("All files exported to:")
print(export_path)
