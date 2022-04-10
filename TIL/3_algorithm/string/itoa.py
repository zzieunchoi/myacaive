# itoa 함수 구현
# 2022-02-16

def itoa(i):
    s = ''
    while i > 0:
        s += chr(ord('0') + i%10)
        i = i//10
    return s[::-1]

print(itoa(456), type(itoa(456)))