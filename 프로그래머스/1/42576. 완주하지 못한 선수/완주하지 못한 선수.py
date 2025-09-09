from collections import Counter

def solution(participant, completion):
    answer = ''
    
    cp = Counter(participant)
    cc = Counter(completion)
    
    cp.subtract(cc)
    
    result = []
    
    for i,j in cp.items():
        if j > 0:
            result.extend([i] * j)
            
    result2 = []
    
    for i in participant:
        if i in result:
            result2.append(i)
            result.remove(i)
            
    for kk in result2:
        answer += kk
        
    return answer
