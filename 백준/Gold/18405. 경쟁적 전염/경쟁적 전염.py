import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

data = []
for i in range(n):
    for j in range(n): 
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j)) 

data.sort()
que = deque(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    virus, time, x1, y1 = que.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x1 + dx[i]
        ny = y1 + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                que.append((virus, time + 1, nx, ny))

print(graph[x - 1][y - 1])