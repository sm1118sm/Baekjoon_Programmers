import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().strip().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        global count
        count += 1
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True
                    que.append((nx,ny))

list1 = []

for x in range(n):
    for y in range(m):
        if not visited[x][y] and graph[x][y] == 1:
            count = 0
            bfs(x,y)
            list1.append(count)

if list1:
    print(len(list1))
    print(max(list1))

else:
    print(0)
    print(0)