from datetime import datetime # module that works with date and time


# get current date
now = datetime.now()
print(f'current date and time is: {now}')

year = now.year
month = now.month
day = now.day
print(f'Current date is: {day}-{month}-{year}')