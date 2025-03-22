import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

que = deque([i for i in range(1, n+1)])

list1 = list(map(int, input().split()))

count = 0

for i in list1:
    while True:
        if i == que[0]:
            que.popleft()
            break
            
        else:
            if que.index(i) <= len(que) // 2:
                que.rotate(-1)
                count += 1
                
            else:
                que.rotate(1)
                count += 1

print(count)