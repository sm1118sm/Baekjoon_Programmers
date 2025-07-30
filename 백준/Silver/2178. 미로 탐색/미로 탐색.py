import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

a, b = map(int, input().split())

graph = [[0] * b for _ in range(a)]
visited = [[False] * b for _ in range(a)]

for i in range(a):
    value = list(input().strip()) 
    for j in range(b):
        graph[i][j] = int(value[j])

def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True

    while que:
        now = que.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]

            if 0 <= x < a and 0 <= y < b:
                if (not visited[x][y]) and (graph[x][y] != 0):
                    visited[x][y] = True
                    graph[x][y] = graph[now[0]][now[1]] + 1
                    que.append((x, y))

bfs(0, 0)
print(graph[a-1][b-1])
