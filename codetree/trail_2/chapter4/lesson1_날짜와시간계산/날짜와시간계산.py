m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day_idx = days.index(A)
month, day = m1, d1
total_date = 0
month_idx = 0
cnt = 0

while True:
    if m2 == month and d2 == day:
        break

    day += 1
    total_date += 1
    month_idx += 1

    if month_idx == 7:
        month_idx = 0

    if month_idx == day_idx:
        cnt += 1

    if day > month_days[month]:
        month += 1
        day = 1

print(cnt)