import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(x, y)
                count += 1
    
    print(count)