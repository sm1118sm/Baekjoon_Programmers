from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    oil_id = [[0]*m for _ in range(n)]  
    oil_size = dict()                   
    id_counter = 1                      
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and oil_id[i][j] == 0:
                q = deque()
                q.append((i,j))
                oil_id[i][j] = id_counter
                size = 1
                
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and oil_id[nx][ny] == 0:
                                oil_id[nx][ny] = id_counter
                                q.append((nx, ny))
                                size += 1
                oil_size[id_counter] = size
                id_counter += 1
    
    max_oil = 0
    for y in range(m):
        seen = set()
        total = 0
        for x in range(n):
            oid = oil_id[x][y]
            if oid != 0 and oid not in seen:
                total += oil_size[oid]
                seen.add(oid)
        max_oil = max(max_oil, total)
    
    return max_oil
