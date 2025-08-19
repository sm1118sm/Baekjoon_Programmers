import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001

que = deque()
que.append((n, 0))

while que:
    x, time = que.popleft()

    if x == k:
        print(time)
        break

    for i, j in [(x * 2, time), (x - 1, time + 1), (x + 1, time + 1)]:
        if 0 <= i < 100001 and not visited[i]:
            visited[i] = True
            if j == time:
                que.appendleft((i, j))
            else:
                que.append((i, j))