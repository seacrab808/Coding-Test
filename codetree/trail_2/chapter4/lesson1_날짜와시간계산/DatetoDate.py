# Time to Time
a, b, c, d = map(int, input().split())

# Please write your code here.

hour, mins = a, b
total_time = 0

while True:
    if hour == c and mins == d:
        break
    
    mins += 1
    total_time += 1

    if mins == 60:
        hour += 1
        mins = 0

print(total_time)


# Date to Date
m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = m1, d1
total_day = 1

while True:
    if month == m2 and day == d2:
        break

    day += 1
    total_day += 1

    if day > month_days[month]:
        month += 1
        day = 1

print(total_day)