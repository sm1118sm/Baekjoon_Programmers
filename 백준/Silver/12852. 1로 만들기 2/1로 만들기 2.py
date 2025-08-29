import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dist = [-1] * (10**6+1)
value = [-1] * (10**6+1)

def bfs(start):
    que = deque()
    que.append(start)
    dist[start] = 0

    while que:
        x = que.popleft()

        if x == 1:
            return dist[x]

        if x % 3 == 0 and dist[x//3] == -1 and 0 <= x//3 < 10 ** 6 + 1:
            dist[x//3] = dist[x] + 1
            value[x//3] = x
            que.append(x//3)
        
        if x % 2 == 0 and dist[x//2] == -1 and 0 <= x//2 < 10 ** 6 + 1:
            dist[x//2] = dist[x] + 1
            value[x//2] = x
            que.append(x//2)

        if x-1 > 0 and dist[x-1] == -1 and 0 <= x-1 < 10 ** 6 + 1:
            dist[x-1] = dist[x] + 1
            value[x-1] = x
            que.append(x-1)
            
print(bfs(n))

list1 = []
startValue = 1

while startValue != -1:
    list1.append(startValue)
    startValue = value[startValue]

list1.reverse()
print(*list1)