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


