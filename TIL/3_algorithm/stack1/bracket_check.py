# 괄호검사
# 2022-02-24

str = '((()((((()()((()())((())))))'
stack = []
top = -1

for char in str:
    if char == '(':
        stack.append(char)
        top +=1
    else:
        stack.pop()
        top -=1

if not stack:
    print(1)
else:
    print(0)