def solution(phone_book):
    stack = []
    for i in phone_book:
        for j in phone_book:

            if j.startswith(i) and i!=j:
                stack.append(j)
    if stack:
        return False
    else:
        return True
