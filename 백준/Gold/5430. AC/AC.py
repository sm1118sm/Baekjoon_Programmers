import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    p = input().strip()
    _ = int(input())
    arr = input().strip()[1:-1]

    que = deque()
    if arr:
        que = deque(map(int, arr.split(',')))

    r_count = 0

    for cmd in p:
        if cmd == 'R':
            r_count += 1
        elif cmd == 'D':
            if not que:
                print('error')
                break
            if r_count % 2 == 0:
                que.popleft()
            else:
                que.pop()
    else:
        if r_count % 2 == 0:
            print('[' + ','.join(map(str, que)) + ']')
        else:
            print('[' + ','.join(map(str, reversed(que))) + ']')
