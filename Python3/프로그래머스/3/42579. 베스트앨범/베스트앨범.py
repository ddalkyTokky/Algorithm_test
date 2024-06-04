def solution(genres, plays):    
    n = len(genres)
    gd = {}

    for idx in range(n):
        if(genres[idx] in gd):
            gd[genres[idx]] += plays[idx]
        else:
            gd[genres[idx]] = plays[idx]
    
    statics = []
    for idx in range(n):
        statics.append([idx, genres[idx], gd[genres[idx]], plays[idx]])
    
    statics.sort(key = lambda x :(-x[2], -x[3], x[0]))
    
    cd = {}
    answer = []
    for static in statics:
        if(static[1] in cd):
            if(cd[static[1]] == 1):
                cd[static[1]] += 1
                answer.append(static[0])
        else:
            cd[static[1]] = 1
            answer.append(static[0])
    
    return answer