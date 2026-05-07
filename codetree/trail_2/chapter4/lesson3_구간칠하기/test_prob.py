# 신기한 타일 뒤집기 

n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
dict = {}
ans_dict = {}
index = 0

for i in range(n):
    if dir[i] == "L":
        for j in range(index, index - x[i], -1):
            dict[j] = dict.get(j, "") + "W"
        index -= (x[i] - 1)
        
    elif dir[i] == "R":
        for j in range(index, index + x[i]):
            dict[j] = dict.get(j, "") + "B"
        index += (x[i] - 1)

W_cnt = 0
B_cnt = 0
G_cnt = 0

for colors in dict.values():
    if colors[-1] == "W":
        W_cnt += 1
    elif colors[-1] == "B":
        B_cnt += 1

print(W_cnt, B_cnt)