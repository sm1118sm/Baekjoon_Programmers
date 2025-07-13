import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    value = list(input().strip())
    left = deque()  
    right = deque()  

    for k in value:
        if k == '<':
            if left:
                right.appendleft(left.pop())

        elif k == '>':
            if right:
                left.append(right.popleft())

        elif k == '-':  
            if left:
                left.pop()

        else:
            left.append(k)

    print("".join(left) + "".join(right))
