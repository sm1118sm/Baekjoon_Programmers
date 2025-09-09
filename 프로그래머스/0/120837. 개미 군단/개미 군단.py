def solution(hp):
    answer = 0
    list1 = [5,3,1]
    
    for i in list1:
        if hp // i > 0:
            answer += hp // i
            hp = hp % i
            
    return answer