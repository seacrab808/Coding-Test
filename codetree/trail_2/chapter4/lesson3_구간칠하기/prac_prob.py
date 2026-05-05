# 최대로 겹치는 지점

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = [0 for _ in range(101)]

for start, end in segments:
    for x in range(start, end +1):
        arr[x] += 1

print(max(arr))