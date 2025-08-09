import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int, input().split())

graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x, y):
    que = deque()
    visited[x][y] = True
    que.append((x,y))

    while que:
        x, y = que.popleft()

        if x == r2 and y == c2:
            return graph[x][y]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx,ny))

result = bfs(r1,c1)

if result == None:
    print(-1)

else:
    print(result)