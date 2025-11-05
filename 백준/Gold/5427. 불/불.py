import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fire_bfs():
    while que:
        x, y, time = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= b or ny >= a:
                continue
            
            if graph[nx][ny] != '#' and visited[nx][ny] == 0:
                visited[nx][ny] = time + 1
                que.append((nx,ny,time+1))
                
    return visited

def sang_bfs(i, j):
    que = deque()
    que.append((i,j,1))
    
    while que:
        x, y, time = que.popleft()

        if x == 0 or y == 0 or x == b - 1 or y == a - 1:
            return time

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or ny < 0 or nx >= b or ny >= a:
                continue
            
            if graph[nx][ny] != '#':
                if time + 1 < visit[nx][ny] and visit[nx][ny] != -1 or visit[nx][ny] == 0:
                    que.append((nx,ny,time+1))
                    visit[nx][ny] = -1
                    
    return "IMPOSSIBLE"


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())  
    graph = [list(input().strip()) for _ in range(b)]

    que = deque()
    visited = [[0] * a for _ in range(b)]
    
    for s in range(b):
        for ss in range(a):
            if graph[s][ss] == '*':
                que.append((s,ss,1))
                visited[s][ss] = 1
                
            elif graph[s][ss] == '@':
                nx, ny = s, ss
    
    visit = fire_bfs()
    
    print(sang_bfs(nx, ny))