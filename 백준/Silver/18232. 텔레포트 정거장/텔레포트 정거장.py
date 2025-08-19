import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

def bfs(start):
    que = deque()
    que.append((start, 0))
    visited[start] = True

    while que:
        x, time = que.popleft()

        if x == e:
            return time

        for k in [x - 1, x + 1]:
            if 1 <= k <= n and not visited[k]:
                visited[k] = True
                que.append((k, time + 1))

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                que.append((i, time + 1))

print(bfs(s))