# 30분 걸림 ㅜ

m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Sun", "Sat", "Fri", "Thu", "Wed", "Tue"]

month, day = m1, d1

def get_total_days(m, d, month_days):
    return sum(month_days[1:m]) + d

day_1 = get_total_days(m1, d1, month_days)
day_2 = get_total_days(m2, d2, month_days)

diff = day_1 - day_2
 
if diff > 0:
    # 양수일 때
    print(days[diff % 7])
else:
    # 음수일 때
    print(days[diff % 7])