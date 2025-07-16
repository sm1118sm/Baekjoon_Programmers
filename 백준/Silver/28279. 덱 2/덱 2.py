import sys
from collections import deque

input = sys.stdin.readline

deque1 = deque()

n = int(input())

for i in range(n):
    a = list(map(int, input().split()))

    if a[0] == 1:
        deque1.appendleft(a[1])

    elif a[0] == 2:
        deque1.append(a[1])

    elif a[0] == 3:
        if len(deque1) != 0:
            print(deque1.popleft())

        else:
            print(-1)

    elif a[0] == 4:
        if len(deque1) != 0:
            print(deque1.pop())

        else:
            print(-1)

    elif a[0] == 5:
        print(len(deque1))

    elif a[0] == 6:
        if len(deque1) != 0:
            print(0)

        else:
            print(1)

    elif a[0] == 7:
        if len(deque1) != 0:
            print(deque1[0])

        else:
            print(-1)

    elif a[0] == 8:
        if len(deque1) != 0:
            print(deque1[-1])

        else:
            print(-1)