# Stack : balanced parentheses
def solution(s):
    stack = []
    # 문자열의 괄호 하나씩 확인
    for i in s:
        # 1. '(' 입력 : 스택에 push
        if i == '(':
            stack.append(i)
        # 2. ')' 입력 : 조건에 맞게 처리
        else:
            # 2-1. 빈 스택이 아닐 때 : 스택 안에 '('만 있으므로 pop 
            if stack:
                stack.pop()
            # 2-2. 빈 스택일 때 : return False   
            else:
                return False
                break # for문 탈출
    
    else: # break문으로 끊기지 않고 수행됐으면 else문 실행
        return stack == []
