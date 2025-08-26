import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
visited = [False] * 100001

def bfs(n, time):
    que = deque()
    que.append((n, time))
    visited[n] = True

    while que:
        x, time = que.popleft()

        if x == m:
            return time

        for i in [x-1, x+1, x*2]:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                que.append((i, time+1))

print(bfs(n,0))