# 블럭쌓는 명령2

n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr = [0 for _ in range(n)]

for first, second in commands:
    arr[first:second + 1] = [x + 1 for x in arr[first:second + 1]]

print(max(arr))

