import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    que = deque([1])
    visited[1] = True    

    while que:
        x = que.popleft()

        for i in range(1, 7):
            nx = x + i

            if 0 < nx <= 100 and not visited[nx]:
                if nx in ladder.keys():
                    nx = ladder[nx]

                if nx in snake.keys():
                    nx = snake[nx]

                if not visited[nx]:
                    que.append(nx)
                    visited[nx] = True
                    graph[nx] = graph[x] + 1
    return None

n, m = map(int, input().split())

graph = [0] * 101

visited = [False] * 101

ladder = dict()
snake = dict()

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(m):
    aa, bb = map(int, input().split())
    snake[aa] = bb

bfs()
print(graph[100])