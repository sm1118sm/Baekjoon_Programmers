from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [[[0]*m for _ in range(n)] for _ in range(h)]
dist = [[[-1]*m for _ in range(n)] for _ in range(h)]

for z in range(h):
    for x in range(n):
        graph[z][x] = list(map(int, input().split()))

dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

que = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                dist[z][x][y] = 0
                que.append((z, x, y))

while que:
    z, x, y = que.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = 1
                dist[nz][nx][ny] = dist[z][x][y] + 1
                que.append((nz, nx, ny))

result = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                print(-1)
                exit()
            result = max(result, dist[z][x][y])

print(result)