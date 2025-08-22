import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
list1 = list(map(int, input().split()))
start = int(input())
visited = [False] * (n)

dx = [-1,1]

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = True

    while que:
        x = que.popleft()

        for i in range(2):
            nx = x + (dx[i] * list1[x])

            if 0 <= nx < n and not visited[nx]:
                visited[nx] = True
                que.append(nx)

bfs(start-1)

count = 0
for i in visited:
    if i:
        count += 1
print(count)