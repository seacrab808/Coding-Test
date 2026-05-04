# 2진수로 변환하기
n = int(input())

# Please write your code here.

digits = []

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2


for i in digits[::-1]:
    print(i, end="")


# 십진수로 변환하기