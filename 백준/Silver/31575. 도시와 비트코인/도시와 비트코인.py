from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]

dx = [1, 0]
dy = [0, 1]

queue = deque()
queue.append((0, 0))
visited[0][0] = True

while queue:
    x, y = queue.popleft()

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[ny][nx] and grid[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny))

if visited[M-1][N-1]:
    print("Yes")
else:
    print("No")