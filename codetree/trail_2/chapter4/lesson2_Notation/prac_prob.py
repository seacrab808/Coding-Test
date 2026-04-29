# 여러가지 진수 변환(4,8진수)
N, B = map(int, input().split())

# Please write your code here.

digits = []

while N > 0:
    digits.append(N % B)
    N //= B

for d in digits[::-1]:
    print(d, end="")