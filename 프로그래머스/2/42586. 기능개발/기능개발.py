def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append((100 - progresses[i]) // speeds[i])
            
        else:
            days.append((100 - progresses[i]) // speeds[i] + 1)
    
    
    now = days[0]   
    count = 1       
    
    for i in range(1, len(days)):
        if days[i] <= now:   
            count += 1
        else:                
            answer.append(count)
            now = days[i]
            count = 1
    answer.append(count)      
        
    return answer