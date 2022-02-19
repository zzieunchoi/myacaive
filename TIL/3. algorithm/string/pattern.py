# 고지식한 패턴 검색 알고리즘
# 2022-02-16

def my_len(a):
    cnt = 0
    for i in a:
        cnt += 1
    return cnt

p = 'is'
t = 'this is a book'
M = my_len(p)
N = my_len(t)

def BruteForce(p,t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M:
        return i -M
    else:
        return -1

print(BruteForce(p, t))

def my_find(p, t):
    my_find_list = []
    for i in range(len(t)-1):
        my_find_list[i] = (p[i], p[i+1])
        if p == my_find_list[i]:
            return i
