stack = []
top = -1
for i in range(0, 10):
    stack.append(i)
    top +=1
print(stack, top)

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]
print(pop())

if top > -1:
    top -= 1
    print(stack[top])