import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
value = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(x):
    que = deque()
    que.append(x)
    visited[x] = True
    global count

    while que:
        a = que.popleft()

        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                value[i] = value[a] + 1

bfs(x)

count = 0

for i in range(len(value)):
    if value[i] == k:
        print(i)
        count += 1

if count == 0:
    print(-1)