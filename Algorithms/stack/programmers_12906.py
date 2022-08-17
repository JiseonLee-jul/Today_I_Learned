# solution using STACK
def solution(arr):
    answer = []
    for num in arr:
        # 1. answer이 빈 array가 아닐 경우 : 이전 num과 비교
        if answer: 
            if answer[-1] == num:
                pass
            else:
                answer.append(num)
        # 2. answer이 빈 array일 경우 : num append        
        else:
            answer.append(num)
    return answer
