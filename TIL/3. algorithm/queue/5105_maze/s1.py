import sys
sys.stdin = open('input.txt','r')

#너비우선탐색
def bfs(i, j, N):
    visited = [[0]* N for _ in range(N)]
    queue = []
    queue.append((i,j))
    visited[i][j] = 1
    while queue: # 큐가 비어있지 않다면
        # t<- 디큐
        i, j = queue.pop(0)
        # visit(t): t에서 할일 처리
        if maze[i][j] == 3:
            return visited[i][j] -2
        for di, dj in [[0,1],[1,0],[0, -1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni< N and 0<= nj< N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                #범위 안에 있고, 인접한 곳이고 벽이 아니며 아직 방문하지 않은 곳
                queue.append((ni,nj)) # 인큐
                visited[ni][nj] = visited[i][j] + 1
    return 0 # 도착지를 찾지 못한 경우 
            
#깊이우선탐색
def dfs(i, j, N, c): # 지나온 칸수
    global minV
    if maze[i][j] ==3: #목적지에 도착하면 기존의 최소거리와 비교
        if minV > c:
            minV = c
    else:
        maze[i][j] =1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<= ni < N and 0<= nj < N and maze[ni][nj] != 1:
                dfs(ni, nj, N, c+1)
        maze[i][j] = 0
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    
    #출발점 찾기
    sti = stj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] ==2:
                sti, stj = i, j
                break
    
    # ans_1 = bfs(sti, stj, N)
    #print('#{} {}'.format(t, ans_1))
    minV = 10000
    dfs(sti, stj, N, 0) #c는 지금까지의 칸수를 말함, 처음 시작점을 포함해서 세고 싶으면 1이라고 집어넣으면됨
    if minV== 10000:
        minV = 1
    print('#{} {}'.format(t, minV-1))



