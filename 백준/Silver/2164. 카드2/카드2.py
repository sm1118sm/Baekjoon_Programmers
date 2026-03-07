import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

que = deque([i for i in range(1, n+1)])

while True:
    if len(que) == 1:
        print(*que)
        break

    que.popleft()
    que.append(que.popleft())