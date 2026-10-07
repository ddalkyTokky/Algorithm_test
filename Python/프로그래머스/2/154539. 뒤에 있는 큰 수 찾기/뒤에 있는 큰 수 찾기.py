def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = [0]
    
    for i in range(1, len(numbers)):
        while(len(stack) != 0):
            if(numbers[i] > numbers[stack[-1]]):
                answer[stack[-1]] = numbers[i]
                stack.pop(-1)
            else:
                break
            
        stack.append(i)
    
    return answer