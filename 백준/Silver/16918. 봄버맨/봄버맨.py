import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(v):
    result = [['O'] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if v[x][y] == 'O':
                result[x][y] = '.'

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c:
                        result[nx][ny] = '.'
    return result

if n == 1:
    for row in graph:
        for j in row:
            print(j, end = '')
        print()

elif n % 2 == 0:
    for _ in range(r):
        print('O' * c)

else:
    bombs1 = bfs(graph)
    bombs2 = bfs(bombs1)

    if n % 4 == 3:
        for row in bombs1:
            for jk in row:
                print(jk, end = '')
            print()

    else:
        for row in bombs2:
            for js in row:
                print(js, end = '')
            print()