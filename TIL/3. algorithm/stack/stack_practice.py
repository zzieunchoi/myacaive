# 연습문제_후위표기법 풀이
# 2022-02-23
tokens ='(6+5*(2-8)/2)'
ans_str = ''
stack = []
top = -1
icp = {'*':2, '/':2, '+':1, '-':1, '(':3, ')': None}
isp = {'*':2, '/':2, '+':1, '-':1, '(':0}
for char in tokens:
    if char in icp:
        if char == ')':
            while stack[top] != '(':
                ans_str += stack[top]
                stack.pop()
                top -= 1
            stack.pop()
            top -= 1
        else:
            if stack == []:
                stack.append(char)
                top += 1
            else:
                if isp[stack[top]] < icp[char]:
                    stack.append(char)
                    top += 1
                else:
                    while isp[stack[top]] >= icp[char]:
                        ans_str += stack[top]
                        stack.pop()
                        top -= 1
                    stack.append(char)
                    top += 1
    else:
        ans_str += char
print(ans_str)