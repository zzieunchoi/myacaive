node_count = 7
line_count = 8
route = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
stack = []
graph = [[] for _ in range(node_count+1)]
visited = [0] * (node_count+1)


def dfs(s):
    print(s, stack)
    visited[s] = 1
    if graph[s]:
        stack.append(s)
        for node in graph[s]:
            dfs(node)
    else:
        node = stack.pop()
        return 
    return 

for i in range((len(route)//2)):
    start_node, end_node = route[2*i: 2*i +2]
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)
dfs(1)
print(graph)


