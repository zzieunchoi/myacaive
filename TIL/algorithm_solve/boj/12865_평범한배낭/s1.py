import sys
sys.stdin =open('input.txt','r')

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

D = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j< arr[i-1][0]:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(D[i-1][j], D[i-1][j-arr[i-1][0]] + arr[i-1][1])

print(D[-1][-1])