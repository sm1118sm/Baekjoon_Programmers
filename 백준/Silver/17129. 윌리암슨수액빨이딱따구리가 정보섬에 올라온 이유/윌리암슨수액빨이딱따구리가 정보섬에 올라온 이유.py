import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []
dist = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []

for i in range(n):
    value = list(map(int, input().strip()))
    graph.append(value)
    for j in range(m):
        if value[j] == 2:
            result.append((i,j))

def bfs(result):
    que = deque()
    for x, y in result:
        que.append((x,y))
        visited[x][y] = True
        dist[x][y] = 0

    while que:
        x, y = que.popleft()

        if (graph[x][y] == 3 or graph[x][y] == 4 or graph[x][y] == 5):
            print('TAK')
            return dist[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                que.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1

    return 'NIE'

print(bfs(result))