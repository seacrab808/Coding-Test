# 첫 시도
a, b, c = map(int, input().split())

# Please write your code here.

day, hour, min = 11, 11, 11
total_min = 0


while True:
    if day == a and hour == b and min == c:
        break

    if day > a:
        print(-1)
        break

    else:
        min += 1
        total_min += 1

        if min == 60:
            hour += 1
            min = 0
        
        elif hour == 24:
            day += 1
            hour = 0

if not day > a:
    print(total_min)



# 정답
a, b, c = tuple(map(int, input().split()))

diff = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

if diff < 0:
    print(-1)
else:
    print(diff)