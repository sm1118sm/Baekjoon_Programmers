import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]  
visited = [list(input().strip()) for _ in range(n)]  

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

bomb = False 

for i in range(n):
    for j in range(n):
        if visited[i][j] == 'x': 
            if graph[i][j] == '*':  
                bomb = True
            else:  
                count = 0
                for k in range(8):
                    nx = i + dx[k] 
                    ny = j + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '*':
                        count += 1
                visited[i][j] = str(count)

for i in range(n):
    for j in range(n):
        if bomb and graph[i][j] == '*':
            print('*', end='')
        else:
            print(visited[i][j], end='')
    print()