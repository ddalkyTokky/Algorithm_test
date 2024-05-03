def solution(weights):
    answer = 0
    
    dict1 = {}
    for w in weights:
        if(w in dict1):
            dict1[w] += 1
        else:
            dict1[w] = 1
            
    for k, v in dict1.items():
        if(v >= 2):
            answer += ((v - 1) * v / 2)
            
    for k in dict1:
        if((k * 2 / 3) in dict1):
            answer += (dict1[(k * 2 / 3)] * dict1[k])
        if((k / 2) in dict1):
            answer += (dict1[(k / 2)] * dict1[k])
        if((k * 3 / 4) in dict1):
            answer += (dict1[(k * 3 / 4)] * dict1[k])
                
    
    return answer