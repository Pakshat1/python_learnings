import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

# Descriptive Statistics 
# Descriptive Statistics (with NumPy + Pandas + Seaborn)
# This level focuses on summarizing your data using numbers and charts 
# so you can understand your data before modeling it.

# | Topic              | Description                             |
# | ------------------ | --------------------------------------- |
# | Mean               | Average value                           |
# | Median             | Middle value                            |
# | Mode               | Most frequent value                     |
# | Range              | Max - Min                               |
# | Variance & Std Dev | Spread of data around mean              |
# | Distribution Shape | Skewness, kurtosis, visual distribution |

import matplotlib.pyplot as plt

# Example data
# data = [12, 15, 12, 18, 19, 21, 22, 22, 23, 24, 24, 25, 25, 30]

# # Mean
# mean = np.mean(data)
# print(f"Mean: {mean}")

# # Median
# median = np.median(data)
# print(f"Median: {median}")

# # Mode
# mode = stats.mode(data, keepdims=True)[0][0]
# print(f"Mode: {mode}")

# # Range
# data_range = np.max(data) - np.min(data)
# print(f"Range: {data_range}")

# # Variance & Standard Deviation
# variance = np.var(data)
# std_dev = np.std(data)
# print(f"Variance: {variance}")
# print(f"Standard Deviation: {std_dev}")

# # Distribution Shape: Skewness & Kurtosis
# skewness = stats.skew(data)
# kurtosis = stats.kurtosis(data)
# print(f"Skewness: {skewness}")
# print(f"Kurtosis: {kurtosis}")

# # Visual Distribution
# sns.histplot(data, kde=True, color='skyblue')
# plt.axvline(mean, color='green', linestyle='--', label=f'Mean: {mean:.2f}')
# plt.axvline(median, color='red', linestyle='-', label=f'Median: {median:.2f}')
# plt.title("Distribution of Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.legend()
# plt.show()


###########################################################################
# usung a real use case 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Hide main Tkinter window
root = tk.Tk()
root.withdraw()

# Step 1: File Explorer
file_path = filedialog.askopenfilename(
    title="Select a CSV or Excel File",
    filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xls")]
)

if not file_path:
    print("No file selected.")
    exit()

# Step 2: Load file
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith((".xlsx", ".xls")):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file type.")
    exit()

# Step 3: Select numeric columns
numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

if not numeric_columns:
    messagebox.showinfo("No Numeric Columns", "This file has no numeric columns.")
    exit()

# Step 4: Analyze each numeric column
for column in numeric_columns:
    data = df[column].dropna()

    if data.empty:
        continue

    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data, keepdims=True)[0][0]
    data_range = np.max(data) - np.min(data)
    variance = np.var(data)
    std_dev = np.std(data)
    skewness = stats.skew(data)
    kurtosis = stats.kurtosis(data)

    print(f"\nColumn: {column}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Range: {data_range}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Skewness: {skewness}")
    print(f"Kurtosis: {kurtosis}")

    # Plot distribution
    sns.histplot(data, kde=True, color='skyblue')
    plt.axvline(mean, color='green', linestyle='--', label=f'Mean: {mean:.2f}')
    plt.axvline(median, color='red', linestyle='-', label=f'Median: {median:.2f}')
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()




