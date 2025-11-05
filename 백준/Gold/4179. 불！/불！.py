import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    que = deque()
    que.append(result)
    for i in fire:
        que.append(i)
        
    while que:
        x, y = que.popleft()
        
        if maps[x][y] == 'J' and (x == 0 or x == r-1 or y == 0 or y == c-1):
            return distance[x][y] + 1       

        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]
            
            if 0 <= nx < r and 0 <= ny < c:
                if maps[x][y] == 'J' and maps[nx][ny] == '.':
                    maps[nx][ny] = 'J'
                    distance[nx][ny] = distance[x][y] + 1
                    que.append((nx, ny))
                    
                elif maps[x][y] == 'F' and (maps[nx][ny] == '.' or maps[nx][ny] == 'J'):
                    maps[nx][ny] = 'F'
                    que.append((nx,ny))
                    
    return 'IMPOSSIBLE'

r, c = map(int, input().split())
maps = []
fire = []

for i in range(r):
    row = list(input())
    maps.append(row)
    for j in range(c):
        if row[j] == 'J':
            result = [i,j]
            
        if row[j] == 'F':
            fire.append((i,j))
            
distance = [[0 for _ in range(c)] for _ in range(r)] 

print(bfs()) 