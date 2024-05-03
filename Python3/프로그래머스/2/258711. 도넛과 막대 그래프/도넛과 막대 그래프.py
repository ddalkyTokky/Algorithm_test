def solution(edges):
    answer = [0, 0, 0, 0]
    
    temp_dict = {}
    
    for edge in edges:
        if(edge[0] in temp_dict):
            temp_dict[edge[0]][1] += 1
        else:
            temp_dict[edge[0]] = [0, 1]
        if(edge[1] in temp_dict):
            temp_dict[edge[1]][0] += 1
        else:
            temp_dict[edge[1]] = [1, 0]
    
    for key, value in temp_dict.items():
        if(value[0] == 0 and value[1] >= 2):
            answer[0] = key
        elif(value[1] == 0):
            answer[2] += 1
        elif((value[1] == 2) and (value[0] >= 2)):
            answer[3] += 1
            
    answer[1] = (temp_dict[answer[0]][1] - answer[2] - answer[3])
        
    
    return answer