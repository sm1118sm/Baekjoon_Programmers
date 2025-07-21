import sys
from collections import deque
input = sys.stdin.readline

n, k, m = map(int, input().split())

que = deque([i for i in range(1, n+1)])

result = []

count = 0

while que:
    if count == m:
        for s in range(m):
            if que:
                que.rotate(k)
                b = que.popleft()
                result.append(b)

        count = 0

    else:
        que.rotate(-k)
        a = que.pop()
        result.append(a)
        count += 1

for j in result:
    print(j)