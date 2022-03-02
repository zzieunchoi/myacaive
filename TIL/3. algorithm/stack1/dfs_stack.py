def dfs(graph, v):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)

visited = [0] * 8
graph = {1: set([2, 3]),
        2: set([4, 5]),
        3: set([5]),
        4: set([6]),
        5: set([6]),
        6: set([7]),
        7: set([])}
root = 1

dfs(graph, 1)
print(visited)