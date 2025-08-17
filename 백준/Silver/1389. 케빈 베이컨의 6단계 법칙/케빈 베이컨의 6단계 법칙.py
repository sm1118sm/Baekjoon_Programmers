import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    visited = [False] * (n+1)
    dist = [-1] * (n+1)
    que = deque()
    que.append(v)
    visited[v] = True
    dist[v] = 0

    while que:
        x = que.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                dist[i] = dist[x] + 1

    return dist

result = 999999
count = 0

for x in range(1, n+1):
        a = bfs(x)
        if result > sum(a[1:]):
            result = sum(a[1:])
            count = x

print(count)