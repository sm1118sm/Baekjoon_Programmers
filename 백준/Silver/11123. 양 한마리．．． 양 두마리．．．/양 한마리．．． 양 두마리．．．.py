import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    global count
    
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == '#':
                    visited[nx][ny] = True
                    count += 1
                    que.append((nx,ny))
                
for _ in range(n):
    graph = []
    h, w = map(int, input().split())
    visited = [[False] * w for _ in range(h)]
    for _ in range(h):
        list1 = list(input().strip())
        graph.append(list1)

    result = []
    for x in range(h):
        for y in range(w):
            if not visited[x][y] and graph[x][y] == "#":
                count = 0
                bfs(x,y)
                result.append(count)
    
    print(len(result)) 