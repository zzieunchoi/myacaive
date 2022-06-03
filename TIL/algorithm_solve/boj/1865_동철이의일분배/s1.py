import sys
sys.stdin = open('input.txt','r')

def work(person, percentage):
    global max_percentage
    # 가지치기
    if percentage <= max_percentage:
        return
    # 종료조건
    if person == N:
        if max_percentage < percentage:
            max_percentage = percentage
        return
    # 재귀
    for i in range(N):
        if visited[i] ==0:
            visited[i] =1
            work(person +1, percentage * arr[person][i])
            visited[i] =0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    
    visited = [0] * (N+1)
    max_percentage = 0
    work(0, 1)


    print(f'#{t} {max_percentage*100:.6f}')