def solution(new_id):
    answer = new_id.lower()
    con = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-', '_']
    for s in answer:
        if s not in con:
            answer = answer.replace(s,'')
            
    dot_list = ['.'* x for x in range(len(answer)-1,1,-1)]        
    for i in dot_list:
        if i in answer:
            answer = answer.replace(i,'.')
    answer = answer.strip('.')
    
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    if len(answer) <= 2:
        while True:
            answer += answer[-1]
            if len(answer) == 3:
                break
    
    return answer
