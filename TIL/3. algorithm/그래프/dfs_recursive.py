def dfs1(v):
    visited[v] =1
    print(v, end = ' ')
    for w in range(V+1):
        if adjM[v][w]== 1 and visited[w] == 0:
            dfs1(w)
            
def dfs2(v):
    visited[v] =1
    print(v, end = ' ')
    for w in adjL[v]:
        if visited[w] == 0:
            dfs2(w)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0]* (V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] =1
    adjM[n2][n1] =1
    
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)
    
visited = [0] * (V+1)
dfs1(1)
dfs2(1)