import sys
input = sys.stdin.readline

n = int(input())

graph = [[] * (n+1) for _ in range(n+1)]

repeat = int(input())

for i in range(repeat):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

count = 0

def dfs(graph, v, visited):
    global count
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)
       
dfs(graph, 1, visited)
print(count)


