# Date Time 
# What is DateTime Feature Extraction?
# When you have a datetime column like 2024-06-15 14:30:00, extracting parts of it — like year, month, day,
# weekday, or hour — is called DateTime feature extraction.
# These new parts (features) help you analyze trends over time, detect seasonality, or build better models.

# basics 
import pandas as pd

# Sample datetime data
import pandas as pd
from datetime import datetime

# Get current PC datetime
current_time = datetime.now()

# Create DataFrame with 10 rows of current time (for demo)
df = pd.DataFrame({
    'OrderDate': [current_time for _ in range(10)]
})

print(df)

# DateTime Feature Extraction from Real-Time Data
# Let’s extract the following features:
# Year,Month, Day,Hour,Minute, Second, Day of Week (number and name), Is Weekend  

import pandas as pd
from datetime import datetime, timedelta

# Get current PC time
now = datetime.now()

# Create 10 rows of increasing time (1 min apart)
df = pd.DataFrame({
    'OrderDate': [now + timedelta(minutes=i) for i in range(10)]
})

# Extract features
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month
df['Day'] = df['OrderDate'].dt.day
df['Hour'] = df['OrderDate'].dt.hour
df['Minute'] = df['OrderDate'].dt.minute
df['Second'] = df['OrderDate'].dt.second
df['DayOfWeek'] = df['OrderDate'].dt.dayofweek  # 0 = Monday
df['WeekdayName'] = df['OrderDate'].dt.day_name()
df['IsWeekend'] = df['DayOfWeek'] >= 5  # Saturday & Sunday

# Display the result
print(df)

# Topic: Time Difference Calculation (Time Delta)
# This is useful when you want to:
# Calculate how long something took (e.g., delivery time, login duration)
# Find age, gaps, durations
# Perform time-based filtering (e.g., > 30 days)

import pandas as pd
from datetime import datetime, timedelta

# Simulate start and end times
now = datetime.now()

df = pd.DataFrame({
    'StartTime': [now + timedelta(minutes=i*5) for i in range(10)],
    'EndTime':   [now + timedelta(minutes=i*5 + 10) for i in range(10)]  # 10 minutes after each start
})

# Calculate difference
df['Duration'] = df['EndTime'] - df['StartTime']

print(df)

#  Extract Duration in Minutes or Seconds
# Duration in seconds
df['Duration_Seconds'] = df['Duration'].dt.total_seconds()

# Duration in minutes
df['Duration_Minutes'] = df['Duration_Seconds'] / 60



##########################################################

import pandas as pd

# Load the file
df = pd.read_excel("time_data.xlsx")

# Convert to datetime
df['StartTime'] = pd.to_datetime(df['StartTime'])
df['EndTime'] = pd.to_datetime(df['EndTime'])

# Time difference
df['Duration'] = df['EndTime'] - df['StartTime']
df['Duration_Seconds'] = df['Duration'].dt.total_seconds()
df['Duration_Minutes'] = df['Duration_Seconds'] / 60

print(df)

######################################################
# Topic: Date-Based Sorting and Filtering

import pandas as pd

# Step 1: Load and Prepare the Data
df = pd.read_excel("time_data.xlsx")

# Ensure datetime format
df['StartTime'] = pd.to_datetime(df['StartTime'])
df['EndTime'] = pd.to_datetime(df['EndTime'])

# Step 2: Sorting by Date
# Sort by StartTime (oldest to newest)
df_sorted = df.sort_values(by='StartTime')

# For latest first, use: ascending=False
df_sorted_latest = df.sort_values(by='StartTime', ascending=False)

# Step 3: Filtering Based on Date or Time
df_after = df[df['StartTime'] >= '2025-07-15 14:00:00']
start = '2025-07-15 13:00:00'
end = '2025-07-15 16:00:00'
df_range = df[(df['StartTime'] >= start) & (df['StartTime'] <= end)]
df['Hour'] = df['StartTime'].dt.hour
df_filtered = df[(df['Hour'] >= 14) & (df['Hour'] <= 16)]

df['Weekday'] = df['StartTime'].dt.day_name()
weekends = df[df['Weekday'].isin(['Saturday', 'Sunday'])]


################################################################################################
# Mini Project Goal: "Login Activity Analyzer"
# We’ll simulate a login dataset and:
# Extract datetime features
# Calculate session durations
# Filter & group logins by time
# Apply rolling averages and lag
# Generate insights
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Step 1: Simulate login and logout times
now = datetime.now()
login_times = [now + timedelta(minutes=30 * i) for i in range(30)]
logout_times = [t + timedelta(minutes=np.random.randint(5, 20)) for t in login_times]

# Step 2: Create DataFrame
df = pd.DataFrame({
    'LoginTime': login_times,
    'LogoutTime': logout_times
})

# Step 3: Feature Engineering
df['LoginTime'] = pd.to_datetime(df['LoginTime'])
df['LogoutTime'] = pd.to_datetime(df['LogoutTime'])

df['SessionDuration'] = df['LogoutTime'] - df['LoginTime']
df['DurationMinutes'] = df['SessionDuration'].dt.total_seconds() / 60
df['Hour'] = df['LoginTime'].dt.hour
df['DayOfWeek'] = df['LoginTime'].dt.day_name()
df['Activity'] = 1  # One login per row

# Step 4: Set datetime index
df.set_index('LoginTime', inplace=True)

# Step 5: Resample by hour (using only numeric columns)
df_hourly = df[['Activity', 'DurationMinutes']].resample('h').sum()

# Step 6: Add Rolling and Lag Features
df_hourly['Rolling_Logins_3H'] = df_hourly['Activity'].rolling(window=3).mean()
df_hourly['Lag_1H'] = df_hourly['Activity'].shift(1)

# Step 7: Reset index to display results
df_hourly = df_hourly.reset_index()

# Step 8: Print output
print(df_hourly[['LoginTime', 'Activity', 'DurationMinutes', 'Rolling_Logins_3H', 'Lag_1H']])










