## 스택 스택 - 실버 4

N = int(input())
stack = []

while N > 0:
    command = input().split()
    cmd = command[0]

    if(cmd=="push"):
        stack.append(int(command[1]))

    elif(cmd=="pop"):
        if(stack):
            print(-1)
        else:
            print(stack.pop())
    
    elif(cmd=="size"):
        print(len(stack))

    elif(cmd=="empty"):
        if(stack):
            print(1)
        else:
            print(0)

    elif(cmd=="top"):
        if(stack):
            print(-1)
        else:
            print(stack[-1])

    N = N - 1