import sys
sys.stdin = open('input1.txt','r')

N = int(input())
command = []
for _ in range(N):
    command.append(input())

stack = []
for i in range(N):
    if command[i][0:4] == "push":
        stack.append(int(command[i][5:(len(command[i]))]))
    elif command[i] == "pop":
        if stack == []:
            print(-1)
        else:
            a = stack.pop()
            print(a)
    elif command[i] == "size":
        print(len(stack))
    elif command[i] == "empty":
        if stack == []:
            print(1)
        else:
            print(0)
    elif command[i] == "top":
        if stack == []:
            print(-1)
        else:
            print(stack[-1])

