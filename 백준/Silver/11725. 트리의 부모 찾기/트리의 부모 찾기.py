import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    que = deque()
    que.append(v)
    visited[v] = True

    while que:
        x = que.popleft()

        for i in graph[x]:
            if not visited[i]:
                que.append(i)
                result[i] = x
                visited[i] = True

bfs(1)

for i in result[2:]:
    print(i)