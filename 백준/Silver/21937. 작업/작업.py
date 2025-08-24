import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

x = int(input())

visited = [False] * (n + 1)

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = True
    count = 0

    while que:
        current = que.popleft()

        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                count += 1 

    return count

print(bfs(x))