import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]

def bfs(x, y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < b and 0 <= ny < a:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    que.append((nx,ny))

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    graph = []
    visited = [[False] * a for _ in range(b)]

    for _ in range(b):
        graph.append(list(map(int, input().split())))

    count = 0

    for x in range(b):
        for y in range(a):
            if not visited[x][y] and graph[x][y] == 1:
                bfs(x,y)
                count += 1

    print(count)