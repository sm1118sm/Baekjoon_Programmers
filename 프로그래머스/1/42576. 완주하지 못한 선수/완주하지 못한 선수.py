def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    
    for j in participant:
        answer += j

    
    return answer