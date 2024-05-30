def solution(n, roads, sources, destination):
    answer = []
    dict_road = {}
    for r in roads:
        if(r[0] in dict_road):
            dict_road[r[0]].append(r[1])
        else:
            dict_road[r[0]] = [r[1]]
            
        if(r[1] in dict_road):
            dict_road[r[1]].append(r[0])
        else:
            dict_road[r[1]] = [r[0]]
            
    queue = [destination]
    visited = {}
    visited[destination] = 0
    while(len(queue) != 0):
        current = queue.pop(0)
        if(current not in dict_road):
            continue
        for item in dict_road[current]:
            if(item not in visited):
                queue.append(item)
                visited[item] = (visited[current] + 1)      
    for s in sources:
        if(s in visited):
            answer.append(visited[s])
        else:
            answer.append(-1)
    return answer