import datetime

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if 1 >= month >= 12:
        print(f'Invalid month {month}')

    if month == 2 and is_leap_year(year):
        return month_days[month] + 1

    return month_days[month]

for month in range(1,13):
    print(days_in_month(2000, month))


num_names = {'one': 1, 'two': 2}
num_names2 = {'three': 3, 'four': 4}

popped = num_names.update(num_names2)

print(num_names)
