import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j):
    que = deque()
    que.append((i, j))
    dist[i][j] = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and graph[nx][ny] == 'L':
                que.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    
    return dist[x][y]

for _ in range(n):
    graph.append(list(input().strip()))

value = 0
for i in range(n):
    for j in range(m):
        dist = [[-1] * m for _ in range(n)]
        if graph[i][j] == 'L':
            value = max(value, bfs(i, j))
print(value)