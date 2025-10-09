import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]
count = 0

while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        count += 1

    cleaned = False

    for _ in range(4):
        d = (d + 3) % 4 
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            r, c = nx, ny
            cleaned = True
            break

    if not cleaned:
        back_d = (d + 2) % 4
        nx = r + dx[back_d]
        ny = c + dy[back_d]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
            r, c = nx, ny
            
        else:
            break

print(count)