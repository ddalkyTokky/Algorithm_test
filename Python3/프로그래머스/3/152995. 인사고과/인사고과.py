def solution(scores):
    if(len(scores) == 1):
        return 1
    
    rank = 1
    
    a = scores[0][0]
    b = scores[0][1]
    ab = a + b
    
    stack = [[-1, -1]]
    
    scores = scores[1 : ]
    scores.sort(key = lambda x : (-x[0], x[1]))
    
    for s in scores:
        na = s[0]
        nb = s[1]
        nab = na + nb
        if((na > a) and (nb > b)):
            return -1
        if(nab > ab):
            while(len(stack) != 0):
                current = stack[-1]
                if((nb < current[1]) and (na < current[0])):
                    break
                else:
                    stack.pop()
            if(len(stack) == 0):
                stack.append(s)
                rank += 1
    return rank
    
            