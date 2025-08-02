import sys
input = sys.stdin.readline
from collections import deque

m,n,k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        global count
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx,ny))

list1 = []

for x in range(m):
    for y in range(n):
        if not visited[x][y] and graph[x][y] == 0:
            count = 0
            bfs(x,y)
            list1.append(count)

print(len(list1))
print(*sorted(list1))