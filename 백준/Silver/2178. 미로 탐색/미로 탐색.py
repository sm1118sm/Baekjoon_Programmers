import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    que = deque()
    que.append((x,y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx,ny))

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            bfs(x,y)

print(graph[n-1][m-1])