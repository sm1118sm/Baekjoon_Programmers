import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for g in graph:
    g.sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (n + 1)
visited2 = [False] * (n + 1)

dfs(graph, v, visited)
print()
bfs(graph, v, visited2)
