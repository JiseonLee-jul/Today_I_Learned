def solution(citations):
    citations.sort(reverse = True)
    for i, h in enumerate(citations): 
        if i >= h:
            return i
    return len(citations) 
