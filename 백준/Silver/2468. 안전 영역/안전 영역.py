import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

maxValue = 0
min_height = min(map(min, graph))
max_height = max(map(max, graph))

for height in range(min_height-1, max_height+1):
    visited = [[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height:
                visited[i][j] = True

    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                count += 1

    maxValue = max(maxValue, count)

print(maxValue)