import sys
input = sys.stdin.readline
from collections import deque

N = int(input()) 
balloons = list(map(int, input().split()))  


dq = deque([(i + 1, balloons[i]) for i in range(N)])

result = []

while dq:
    idx, move = dq.popleft()
    result.append(idx)

    if len(dq) == 0:
        break

    if move > 0:
        dq.rotate(-(move - 1))
    else:
        dq.rotate(-move)

for i in result:
    print(i, end = " ")
