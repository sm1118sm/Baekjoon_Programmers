import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

dx = [-2,-1,1,2,-2,-1,1,2]
dy = [-1,-2,-2,-1,1,2,2,1]

def bfs(x, y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    graph[x][y] = 0


    while que:
        x, y = que.popleft()
        
        if x == x2 and y == y2:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx,ny))


for _ in range(n):
    l = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    graph = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]

    print(bfs(x1,y1))