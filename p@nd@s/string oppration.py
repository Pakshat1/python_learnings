# string opperations

# common string opperations
# | Operation            | Example Code                          | Purpose             |
# | -------------------- | ------------------------------------- | ------------------- |
# | Convert to lowercase | `df['col'].str.lower()`               | Normalize casing    |
# | Convert to uppercase | `df['col'].str.upper()`               |                     |
# | Strip whitespace     | `df['col'].str.strip()`               | Remove extra spaces |
# | Replace text         | `df['col'].str.replace('old', 'new')` | Text substitution   |
# | Contains pattern     | `df['col'].str.contains('pattern')`   | Boolean filter      |
# | Starts/Ends with     | `df['col'].str.startswith('A')`       | Check prefix/suffix |
# | Extract substrings   | `df['col'].str[0:3]`                  | Slice text          |
# | Split strings        | `df['col'].str.split('-')`            | Convert to list     |
# | Join strings         | `df['col1'] + ' ' + df['col2']`       | Combine columns     |


import pandas as pd

df = pd.DataFrame({
    'Name': ['  alice  ', 'Bob', 'charlie'],
    'Email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@outlook.com']
})

# Convert to lowercase
df['Name_Lower'] = df['Name'].str.lower()

# Convert to uppercase
df['Name_Upper'] = df['Name'].str.upper()

# Strip whitespace
df['Name_Stripped'] = df['Name'].str.strip()

# Replace text (with regex=False to avoid warnings)
df['Email_Replaced'] = df['Email'].str.replace('gmail.com', 'example.com', regex=False)

# Contains pattern
df['Is_Yahoo'] = df['Email'].str.contains('yahoo')

# Starts/Ends with
df['Name_StartsWith_B'] = df['Name'].str.strip().str.startswith('B')

# Extract substrings
df['Name_First3'] = df['Name'].str.strip().str[0:3]

# Split strings
df['Email_Split'] = df['Email'].str.split('@')

# Join strings
df['Name_Email'] = df['Name'].str.strip() + ' <' + df['Email'] + '>'

print(df)

import pandas as pd

df = pd.DataFrame({
    'Name': ['  alice  ', 'Bob', 'charlie'],
    'Email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@outlook.com']
})

# Strip whitespace and convert name to title case
df['Name_Cleaned'] = df['Name'].str.strip().str.title()

# Extract email domain
df['Email_Domain'] = df['Email'].str.split('@').str[1]

# Check if email is Gmail
df['Is_Gmail'] = df['Email'].str.contains('gmail')

# Replace domain
df['Updated_Email'] = df['Email'].str.replace('gmail.com', 'example.com')

# Uppercase entire email
df['Email_Upper'] = df['Email'].str.upper()

print(df)

import pandas as pd

df = pd.DataFrame({
    'Name': ['  alice  ', 'Bob', 'charlie'],
    'Email': ['alice@gmail.com', 'bob@yahoo.com', 'charlie@outlook.com']
})

df['Name_Lower'] = df['Name'].str.lower()
df['Name_Upper'] = df['Name'].str.upper()
df['Name_Stripped'] = df['Name'].str.strip()
df['Email_Replaced'] = df['Email'].str.replace('gmail.com', 'example.com', regex=False)
df['Is_Yahoo'] = df['Email'].str.contains('yahoo')
df['Name_StartsWith_B'] = df['Name'].str.strip().str.startswith('B')
df['Name_First3'] = df['Name'].str.strip().str[0:3]
df['Email_Split'] = df['Email'].str.split('@')
df['Name_Email'] = df['Name'].str.strip() + ' <' + df['Email'] + '>'

# Save to Excel file
df.to_excel("string_operations_output.xlsx", index=False)


########## DateTime Operations  ####################

