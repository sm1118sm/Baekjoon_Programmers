import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

q = deque()

q.append([n,0])

def check_range(x):
    return x>=0 and x<100001

visited = [False]*100001

ans = []

while q:
    x, sec = q.popleft()
    if x == k :
        print(sec)
        break

    nx = [x-1, x+1, 2*x]

    for i in nx:
        if check_range(i) and visited[i] == False:
            q.append([i,sec+1])
            visited[i] = True

