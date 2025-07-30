import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())


def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return 
    
    if graph[y][x] == 0:
        return 
    
    graph[y][x] = 0
    
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)


for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())

        graph[y][x] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(j, i)
                count += 1

    print(count)