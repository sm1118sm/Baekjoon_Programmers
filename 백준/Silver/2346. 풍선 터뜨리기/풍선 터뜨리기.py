import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

list1 = list(map(int, input().split()))

que = deque([(i+1, list1[i]) for i in range(n)])

result = []

while que:
    p, q = que.popleft()

    result.append(p)

    if not que:
        break

    if q < 0:
        que.rotate(-q)

    else:
        que.rotate(-(q - 1))


print(*result)