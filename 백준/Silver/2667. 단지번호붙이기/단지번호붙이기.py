import sys
input = sys.stdin.readline

n = int(input())

visited = [[False] * n for _ in range(n)]
graph = []

dx = [-1, 0, 1, 0]  # 상, 좌, 하, 우
dy = [0, -1, 0, 1]

count = 0

def dfs(x, y):
    global count
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True  # ← 여기 수정됨!
                dfs(nx, ny)

for _ in range(n):
    graph.append(list(map(int, input().strip())))

result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for i in sorted(result):
    print(i)