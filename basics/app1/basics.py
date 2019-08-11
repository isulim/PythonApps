import time
import os
import pandas

while True:
    if os.path.exists("basics/app1/files/temps_today.csv"):
        data = pandas.read_csv("basics/app1/files/temps_today.csv")
        print(data.mean())
    else:
        print('File does not exist')

    time.sleep(10)