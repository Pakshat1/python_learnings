# introduction to seaborn
# Seaborn is a high-level Python data visualization library based on Matplotlib.
# It makes beautiful and informative statistical graphics with very little code.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample Data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [120, 135, 150, 160, 170, 190]
})

sns.lineplot(data=data, x='Month', y='Sales')

plt.title("Monthly Sales")
plt.ylabel("Sales ($1000s)")
plt.grid(True)
plt.show()

