import datetime
test = str(datetime.datetime.now())
extract_time = lambda date: [
    ("Year:", date[:4]),
    ("Month:", date[5:7]),
    ("Date:", date[8:10]),
    ("Time:", date[11:])
]
print(extract_time(test))