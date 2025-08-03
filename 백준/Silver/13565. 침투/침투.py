import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = []
visited = [[False] * n for _ in range(m)]

for _ in range(m):
    graph.append(list(map(int, input().strip())))

count = 0

for s in range(n):
    if graph[m-1][s] == 0:
        count += 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = 1
                    que.append((nx,ny))

for x in range(n):
    if not visited[0][x] and graph[0][x] == 0:
        visited[0][x] = True
        graph[0][x] = 1
        bfs(0,x)
            
count2 = 0

for ss in range(n):
    if graph[m-1][ss] == 0:
        count2 += 1

if count == count2:
    print("NO")
else:
    print("YES")