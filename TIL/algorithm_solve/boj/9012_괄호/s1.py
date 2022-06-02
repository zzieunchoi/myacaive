import sys
sys.stdin = open('input.txt','r')

N = int(input())
for _ in range(N):
    ans = ""
    stack = []
    bracket = input()
    if len(bracket)%2 == 1:
        print("NO")
    else:
        for i in range(len(bracket)):
            if bracket[i] == "(":
                stack.append(bracket[i])
            elif bracket[i] == ")":
                if "(" in stack:
                    stack.remove("(")
                else:
                    ans = "NO"
                    print(ans)
                    break
        if ans != "NO":
            if stack == []:
                print('YES')
            else:
                print("NO")

