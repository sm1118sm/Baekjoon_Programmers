def solution(array, commands):
    answer = []
    
    for i in commands:
        value2 = array[i[0]-1:i[1]]
        answer.append(sorted(value2)[i[2]-1])
        
    return answer