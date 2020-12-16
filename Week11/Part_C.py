import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

activity_file = os.path.join(sys.path[0], "activity.csv")
data = pd.read_csv(activity_file, delimiter = ',')

# Count the number of NaNs
print(data.isnull().sum().sum())

# Devise a strategy for filling in all the missing values
# Create a new dataset that is equal to original dataset but with missing data filled in
# I'll assume NaN = Mean steps
new_dataset = data.fillna(data.steps.mean())

# Make histogram of total steps taken each day
new_dataset = new_dataset.iloc[:, [0, 1]].dropna() #take only date and steps
data_total = new_dataset.groupby(["date"]).sum()
plt.hist(data_total)
plt.ylabel("Total Steps")
plt.xlabel("Date")
plt.show()

# Calculate & report the mean, median of the total steps taken per day
data_total = new_dataset.groupby(["date"]).sum()
print(data_total.mean())
print(data_total.median())
