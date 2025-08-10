import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
result = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(first, search):
    que = deque()
    que.append(first)
    visited[first] = True

    while que:
        x = que.popleft()

        if search == x:
            return result[x]

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                result[i] = result[x] + 1

a = bfs(a,b)

if a == None:
    print(-1)

else:
    print(a)