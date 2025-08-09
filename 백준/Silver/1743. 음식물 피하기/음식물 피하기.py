import sys
input = sys.stdin.readline
from collections import deque

n,m,k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1

def bfs(x, y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        global count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    count += 1
                    que.append((nx,ny))

list1 = []

for x in range(n):
    for y in range(m):
        if not visited[x][y] and graph[x][y] == 1:
            count = 1
            bfs(x,y)
            list1.append(count)

print(max(list1))