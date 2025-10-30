import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x,y):
    visited[y][x] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx] and graph[ny][nx] == 1:
                dfs(nx, ny)

for _ in range(n):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1

    print(count)