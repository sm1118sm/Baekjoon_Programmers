import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visted1 = [False] * (n+1)
visted2 = [False] * (n+1)


def dfs(v):
    visted1[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not visted1[i] and graph[v][i]:
            dfs(i)


def bfs(v):
    que = deque([v])
    visted2[v] = True
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not visted2[i] and graph[v][i]:
                que.append(i)
                visted2[i] = True

dfs(v)
print()
bfs(v)

    