import sys

def solution(land):
    n = len(land)
    m = len(land[0])
    queue = []
    visited = []
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = [0 for _ in range(m)]
    
    for idx in range(n):
        for jdx in range(m):
            if((land[idx][jdx] == 1) and (visited[idx][jdx] == False)):
                queue.append([idx, jdx])
                count = 0
                visited[idx][jdx] = True
                
                start = sys.maxsize
                end = -sys.maxsize
                while(len(queue) > 0):
                    count += 1
                    x = queue[0][0]
                    y = queue[0][1]
                    queue.pop(0)
                    
                    start = min(y, start)
                    end = max(y, end)

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if((nx >= 0) and (nx < n)):
                            pass
                        else:
                            continue
                        if((ny >= 0) and (ny < m)):
                            pass
                        else:
                            continue
                        
                        if((land[nx][ny] == 1) and (visited[nx][ny] == False)):
                            queue.append([nx, ny])
                            visited[nx][ny] = True
                            
                for i in range(start, end + 1):
                    answer[i] += count
    
    print(answer)
    return max(answer)