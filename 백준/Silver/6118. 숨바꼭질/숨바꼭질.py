import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(v):
    visited = [False] * (n+1)
    dist = [-1] * (n+1)
    
    que = deque()
    que.append(v)
    visited[v] = True
    dist[v] = 0

    while que:
        x = que.popleft()

        for i in graph[x]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                dist[i] = dist[x] + 1

    return dist

dist1 = bfs(1)

maxValue = 0
maxValueIndex = 0

for ss in range(len(dist1)):
    if dist1[ss] > maxValue:
        maxValue = dist1[ss]
        maxValueIndex = ss

print(maxValueIndex, maxValue, dist1.count(maxValue))