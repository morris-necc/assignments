import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

activity_file = os.path.join(sys.path[0], "activity.csv")
data = pd.read_csv(activity_file, delimiter = ',')
data = data.iloc[:, [0, 1]].dropna() #takes only steps and date column

# Calculate the total number of steps per day
data = data.groupby(["date"]).sum() #groups all row with the same date and sums steps

# Make a histogram of the total number of steps each day
plt.hist(data)
plt.ylabel("Frequency")
plt.xlabel("Number of steps in a day")
plt.show()

# Calculate and report mean & median of total steps per day
print(data.mean())
print(data.median())
