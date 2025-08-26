import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
visited = [False] * 100001
timeValue = [0] * 100001
minTime = float('inf')
result = 0

def bfs(n, time):
    que = deque()
    que.append((n, time))
    visited[n] = True
    global minTime, result
    timeValue[n] = 0

    while que:
        x, time = que.popleft()

        if x == m:
            if time < minTime:
                minTime = time
                result = 1

            elif time == minTime:
                result += 1            
            continue

        for i in [x-1, x+1, x*2]:
            if 0 <= i <= 100000:
                if not visited[i]:
                    visited[i] = True
                    timeValue[i] = time + 1
                    que.append((i, time + 1))

                elif time+1 == timeValue[i]:
                    que.append((i, time+1))

bfs(n,0)
print(minTime)
print(result)