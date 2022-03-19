import sys
sys.stdin = open('input.txt','r')


def bfs(i,j, arr):
    global dist_list, visited
    queue = [[i,j]]
    dist_list = [arr[i][j]]
    visited[i][j] =1

    while queue:
        start = queue.pop(0)
        oi = start[0]
        oj = start[1]
        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni = oi + di
            nj = oj + dj
            if 0<= ni < N and 0<= nj < N and visited[ni][nj] == 0 :
                if arr[ni][nj] == arr[oi][oj] +1:
                    queue.append([ni, nj])
                    visited[ni][nj] =1 
                    dist_list.append(arr[ni][nj])
                    oi= ni
                    oj= nj
                    
    return 
        


# 테스트 케이스
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]


    ans_list = []
    for i in range(N):
        for j in range(N):
            bfs(i, j, arr)
            ans_list.append(dist_list)
    
    max_len = len(ans_list[0])
    for l in ans_list:
        if len(l) >  max_len:
            max_len = len(l)

    min_list = []
    for m in ans_list:
        if len(m) == max_len:
            min_list.append(m[0])
            ans = min(min_list)
    print('#{} {} {}'.format(t, ans, max_len))