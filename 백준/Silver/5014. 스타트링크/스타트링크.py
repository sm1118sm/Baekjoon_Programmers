import sys
input = sys.stdin.readline
from collections import deque

f,s,g,u,d = map(int, input().split())

visited = [False] * (f+1)

def bfs(s):
    que = deque()
    que.append((s, 0))
    visited[s] = True
    
    while que:
        x, count = que.popleft()
        
        if x == g:
            return count
        
        for i in [x+u, x-d]:
            if 0 < i <= f and not visited[i]:
                visited[i] = True
                que.append((i, count+1))
                
    return 'use the stairs'

print(bfs(s))