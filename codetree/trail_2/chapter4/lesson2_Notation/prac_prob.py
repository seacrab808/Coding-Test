# 여러가지 진수 변환(4,8진수)
N, B = map(int, input().split())

# Please write your code here.

digits = []

while N > 0:
    digits.append(N % B)
    N //= B

for d in digits[::-1]:
    print(d, end="")


# 십진수와 이진수 2
N = input()

# Please write your code here.
total = 0

for i in N:
    total = total * 2 + int(i)

mul = total * 17

digits = []

while True:
    if mul < 2:
        digits.append(mul)
        break
    
    digits.append(mul % 2)
    mul //= 2

for i in digits[::-1]:
    print(i, end="")