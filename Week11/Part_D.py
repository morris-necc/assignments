import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

activity_file = os.path.join(sys.path[0], "activity.csv")
data = pd.read_csv(activity_file, delimiter = ',')
data = data.fillna(0)

#Create new factor variable
#Indicates whether given date is weekday or weekend
def check_weekday(date):
    """ checks if a given date is a weekday/weekend """
    date = datetime.strptime(date, "%Y-%m-%d")
    if date.weekday() <= 4:
        return "weekday"
    else:
        return "weekend"

data["weekday"] = pd.Series([check_weekday(x) for x in data["date"]], dtype="category")

# Time plot
# 5-minute interval (x)
# avg steps taken over weekdays/weekends (y-axis)
data = data.iloc[:, [0, 2, 3]]
data = data.groupby(["interval","weekday"]).mean()

#split data over weekday and weekend
data_weekday = data.xs('weekday', level = "weekday")
data_weekend = data.xs('weekend', level = "weekday")

#plots 2 graphs based on the data above
plt.subplot(2, 1, 1)
plt.plot(data_weekday)
plt.ylabel("Avg. steps over weekdays")
plt.xlabel("5-min intervals")
plt.subplot(2, 1, 2)
plt.plot(data_weekend)
plt.ylabel("Avg. steps over weekends")
plt.xlabel("5-min intervals")
plt.tight_layout()
plt.show()