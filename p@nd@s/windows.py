# 
# | Type          | Window Style      | What it Does                       |
# | ------------- | ----------------- | ---------------------------------- |
# | `rolling()`   | Fixed-size window | e.g. moving average of last 3 rows |
# | `expanding()` | Expanding window  | Grows from start to current row    |
# | `cumsum()`    | Cumulative total  | Adds values from start till now    |

import pandas as pd

df = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [100, 200, 150, 300, 250]
})

# Apply all three window functions
df['Rolling_3'] = df['Sales'].rolling(window=3).mean()
df['ExpandingMean'] = df['Sales'].expanding().mean()
df['CumSum'] = df['Sales'].cumsum()

print(df)
