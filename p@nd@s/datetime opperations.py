
################################### 
# | Task                                 | Code Example                                    |
# | ------------------------------------ | ----------------------------------------------- |
# | Convert column to datetime           | `pd.to_datetime(df['Date'])`                    |
# | Extract year/month/day               | `df['Date'].dt.year`, `.dt.month`               |
# | Filter by date                       | `df[df['Date'] >= '2024-01-01']`                |
# | Add/subtract time                    | `df['Date'] + pd.Timedelta(days=7)`             |
# | Create range of dates                | `pd.date_range(start, end, freq='D')`           |
# | Set datetime as index                | `df.set_index('Date')`                          |
# | Resample time series (group by time) | `df.resample('M').sum()` (if index is datetime) |

# Example: Create a range of dates
import pandas as pd

# Create a daily date range
date_range = pd.date_range(start='2024-06-01', end='2024-06-10', freq='D')

# Create DataFrame with values from 1 to number of dates
df_range = pd.DataFrame({
    'Date': date_range,
    'Value': range(1, len(date_range) + 1)
})

# Set 'Date' column as index
df_range = df_range.set_index('Date')

# Resample: Sum values by month-end (use 'ME' instead of deprecated 'M')
monthly_sum = df_range.resample('ME').sum()

# Print results
print("Date Range DataFrame:")
print(df_range)

print("\nMonthly Sum (Resampled):")
print(monthly_sum)


import pandas as pd

# Sample DataFrame with date strings
df = pd.DataFrame({
    'Event': ['Exam', 'Seminar', 'Workshop', 'Meeting'],
    'Date': ['2024-05-10', '2024-06-15', '2024-06-25', '2024-07-01']
})

# 1. Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 2. Extract year, month, weekday
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Weekday'] = df['Date'].dt.day_name()

# 3. Filter: Only events after June 2024
filtered = df[df['Date'] > '2024-06-01']

# 4. Add 7 days to each date
df['Date_Plus_7'] = df['Date'] + pd.Timedelta(days=7)

print(df)
print("\nFiltered (After June 1st):")
print(filtered)
