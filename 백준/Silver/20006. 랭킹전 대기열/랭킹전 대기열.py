p, m = map(int, input().split())

rooms = []  

for _ in range(p):
    level, name = input().split()
    if len(rooms) == 0:     
        rooms.append([[int(level), name]])    
        
    else:    
        for room in rooms:      
            first_lv = room[0][0]     
            if len(room) < m and first_level - 10 <= int(level) <= first_level + 10:
                room.append([level, name])  
                break     
                
        else:     
            rooms.append([[int(level), name]])     
    
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room.sort(key=lambda x:x[1]) 
    
    for player in room:
        print(player[0], player[1])
