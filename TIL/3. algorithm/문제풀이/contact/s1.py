# 1238_contact 풀이

import sys
sys.stdin = open('input.txt','r')

def contact(start):
    queue = []
    queue.append(start)
    visited[start] = 1
    
    while queue:
        a = queue.pop(0)
        for next in graph[a]:
            if visited[next] == 0:
                visited[next] =1
                queue.append(next)
                distance[next] = distance[a] + 1
    return

T = 10
for t in range(1, T+1):
    N , start_node = map(int, input().split())
    data = list(map(int, input().split()))
    K = max(data)

    graph = [[]*(K+1) for _ in range(K+1)]
    visited = [0] * (K+1)
    distance = [0] * (K+1)

    for i in range(0, len(data), 2):
        graph[data[i]].append(data[i+1])
   
    contact(start_node)
    
    for i in range(K+1):
        if distance[i] == max(distance):
            ans = i
    print('#{} {}'.format(t, ans))

