def solution(sequence):
    answer = 0
    
    partial_sum = [sequence[0]]
    flag = 0
    for idx in range(1, len(sequence)):
        current = sequence[idx]
        if(flag == 0):
            current *= -1
        if(partial_sum[-1] < 1):
            partial_sum.append(current)
        else:
            partial_sum.append(current + partial_sum[-1])
        flag = 1 - flag
    answer = max(partial_sum)
    
    partial_sum = [-sequence[0]]
    flag = 1
    for idx in range(1, len(sequence)):
        current = sequence[idx]
        if(flag == 0):
            current *= -1
        if(partial_sum[-1] < 1):
            partial_sum.append(current)
        else:
            partial_sum.append(current + partial_sum[-1])
        flag = 1 - flag
    if(answer < max(partial_sum)):
        answer = max(partial_sum)
    
    return answer