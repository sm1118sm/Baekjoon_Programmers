import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

que = deque()

while True:
    a = int(input())

    if a == -1:
        break

    if n < len(que):
        continue

    else:
        if n == len(que) and a == 0:
            que.popleft()

        elif n > len(que):
            if a != 0:
                que.append(a)

            elif a == 0:
                que.popleft()

if que:
    print(*que)

else:
    print(-1)