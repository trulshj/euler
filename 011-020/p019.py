
import datetime
import time
start_time = time.time()

sundays = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.datetime(year, month, 1).weekday() == 6:
            sundays += 1

print(f"{sundays} found in {time.time() - start_time} seconds")
