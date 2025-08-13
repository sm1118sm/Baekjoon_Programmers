import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())

graph = []
visited = [[False] * c for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(r):
    value = list(input().strip())
    graph.append(value)

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    global sheep
    global wolf

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '#':

                if graph[nx][ny] == 'o':
                    sheep += 1
                    visited[nx][ny] = True
                    que.append((nx,ny))

                elif graph[nx][ny] == 'v':
                    wolf += 1
                    visited[nx][ny] = True
                    que.append((nx,ny))

                elif graph[nx][ny] == '.':
                    visited[nx][ny] = True
                    que.append((nx,ny))

sheepResult, wolfResult = 0, 0

for x in range(r):
    for y in range(c):
        if not visited[x][y] and graph[x][y] != '#':
            sheep, wolf = 0, 0
            if graph[x][y] == 'o':
                sheep += 1
                bfs(x,y)

            elif graph[x][y] == 'v':
                wolf += 1
                bfs(x,y)

            elif graph[x][y] == '.':
                bfs(x,y)

            if sheep > wolf:
                sheepResult += sheep
                wolfResult += 0

            else:
                sheepResult += 0
                wolfResult += wolf

print(sheepResult, wolfResult)