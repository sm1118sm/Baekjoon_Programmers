import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque()

que.append((1,0))
visited[1] = True

count = 0

while que:
    x, y = que.popleft()

    if y >= 2:
        continue

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            count += 1
            que.append((i, y+1))

print(count)