import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
visited = [[False] * m for _ in range(n)]
result = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    value = list(map(int, input().split()))
    graph.append(value)

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    que.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                    result.append(graph[nx][ny])

for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            if graph[x][y] == 2:
                bfs(x,y)

for i in graph:
    for j in i:
        if j != 0:
            print(j-2, end=" ")
        else:
            print(0, end = " ")
    print()