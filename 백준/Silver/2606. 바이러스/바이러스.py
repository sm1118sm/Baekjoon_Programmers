import sys
input = sys.stdin.readline

node = int(input())
edge = int(input())

graph = [[] for _ in range(node+1)]

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (node + 1)

count = 0

def dfs(v):
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

dfs(1)

count = 0

for i in visited:
    if i == 1:
        count += 1

print(count-1)