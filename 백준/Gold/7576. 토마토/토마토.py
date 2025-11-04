import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

count = 0

que = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((j,i))


def bfs():
    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = graph[b][a] + 1
                que.append((nx,ny))


bfs()

for s in graph:
    for j in s:
        if j == 0:
            print(-1)
            exit(0)

    count = max(count, max(s))

print(count-1)