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