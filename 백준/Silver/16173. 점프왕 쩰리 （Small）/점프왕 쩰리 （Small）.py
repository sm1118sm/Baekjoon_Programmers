import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,0]
dy = [0,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()
        value = graph[x][y]

        if value == -1:
            print("HaruHaru")
            return

        for i in range(0,2):
            nx = x + (dx[i] * value)
            ny = y + (dy[i] * value)

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))

    print("Hing")

bfs(0,0)