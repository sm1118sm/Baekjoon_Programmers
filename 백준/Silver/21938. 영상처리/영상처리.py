import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                idx = ny * 3 
                r, g, b = graph[nx][idx], graph[nx][idx+1], graph[nx][idx+2]
                avg = (r + g + b) // 3
                if avg >= t:
                    visited[nx][ny] = True
                    q.append((nx, ny))

count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            idx = j * 3
            r, g, b = graph[i][idx], graph[i][idx+1], graph[i][idx+2]
            avg = (r + g + b) // 3
            if avg >= t:
                bfs(i, j)
                count += 1

print(count)