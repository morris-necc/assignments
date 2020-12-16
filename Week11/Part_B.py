import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import datetime as dt

activity_file = os.path.join(sys.path[0], "activity.csv")
data = pd.read_csv(activity_file, delimiter = ',')
#it's 2am and i can't figure out how to change interval into proper time my bad
#data["interval"] = dt.datetime.strptime(data["interval"], '%H%M')
data = data.iloc[:, [0, 2]].dropna() #takes only the steps and interval column

# Make a time series plot
# x-axis = 5-minute interval
# y-axis = average number of steps taken per days
data = data.groupby(["interval"]).mean() #groups all row with the same interval and averages steps
plt.plot(data)
plt.ylabel("Average steps")
plt.xlabel("5-min interval")
plt.show()

# Which 5-minute interval, on average across all days in the dataset
# Contains the max number of steps
print(data.nlargest(1, "steps"))
