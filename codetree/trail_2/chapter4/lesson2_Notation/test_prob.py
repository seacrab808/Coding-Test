a, b = map(int, input().split())
n = input()

# Please write your code here.


total = 0
for i in n:
    total = total * a + int(i)

digits = []
while True:
    if total < b:
        digits.append(total)
        break
    digits.append(total % b)
    total //= b

for d in digits[::-1]:
    print(d, end="")


# 왔다 갔던 구역 2
n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
dict = {}
index = 0

for i in range(n):
    if dir[i] == "L":
        # 음수일 경우
        # 현재 인덱스에서 계산한 인덱스만큼의 거리 arr에  + 1
        for j in range(index - x[i], index):
            dict[j] = dict.get(j, 0) + 1
        index -= x[i]
    elif dir[i] == "R":
        # 양수일 경우
        for j in range(index, index + x[i]):
            dict[j] = dict.get(j, 0) + 1
        index += x[i]

cnt = 0
for x in dict.values():
    if x >= 2:
        cnt += 1

print(cnt)
## 모두 양수일 경우 배열도 좋지만, 음수가 포함되었거나 범위가 불명확할 경우 딕셔너리를 쓰는게 좋다는 것을 배움


# 흰검 칠하기
## 첫번째 시도;;
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
        # 음수 방향일 경우
        for j in range(index - x[i], index):
            dict[j] = dict.get(j, "") + "W"
            ans_dict[j] = "W"

            if dict[j].count("W") >= 2 and dict[j].count("B") >= 2:
                ans_dict[j] = "G"
        index -= x[i]
    elif dir[i] == "R":
        # 양수 방향일 경우
        for j in range(index, index + x[i]):
            dict[j] = dict.get(j, "") + "B"

            ans_dict[j] = "B"

            if dict[j].count("W") >= 2 and dict[j].count("B") >= 2:
                ans_dict[j] = "G"
        index += x[i]

W_cnt = 0
B_cnt = 0
G_cnt = 0

for x in ans_dict.values():
    if x == "W":
        W_cnt += 1
    elif x == "B":
        B_cnt += 1
    elif x == "G":
        G_cnt += 1    

print(W_cnt, B_cnt, G_cnt)


##두번째,, (도움)
n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
dict = {}
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
    if colors.count("W") >= 2 and colors.count("B") >= 2:
        G_cnt += 1
    elif colors[-1] == "W":
        W_cnt += 1
    elif colors[-1] == "B":
        B_cnt += 1

print(W_cnt, B_cnt, G_cnt)