def allow(str1, str2):
    h1 = int(str1[0 : 2])
    m1 = int(str1[3 : ])
    h2 = int(str2[0 : 2])
    m2 = int(str2[3 : ])
    
    m1 += 10
    if(m1 >= 60):
        h1 += 1
        m1 -= 60
        
    if(h2 > h1):
        return True
    elif(h1 == h2):
        if(m2 >= m1):
            return True
    return False

def solution(book_time):
    queue = []
    max_queue_size = 1
    
    book_time.sort()
    
    for time in book_time:
        for q in queue:
            if(allow(q[1], time[0])):
                queue.remove(q)
                break
        queue.append(time)
        if(max_queue_size < len(queue)):
            max_queue_size = len(queue)
    
    return max_queue_size