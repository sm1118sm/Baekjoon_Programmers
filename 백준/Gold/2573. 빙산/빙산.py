import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(x, y, visited):
    que = deque()
    que.append((x, y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = True
                que.append((nx, ny))

def melt():
    global graph

    tmp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                count = 0
                
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    
                    if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0:
                        count += 1
                
                tmp[i][j] = count
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                graph[i][j] = max(0, graph[i][j] - tmp[i][j])

def count_ice():
    visited = [[False] * m for _ in range(n)]
    chunks = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                chunks += 1
    
    return chunks

year = 0

while True:
    melt()  
    year += 1
    chunks = count_ice()
    
    if chunks == 0:        
        print(0)
        break
    elif chunks >= 2: 
        print(year)
        break