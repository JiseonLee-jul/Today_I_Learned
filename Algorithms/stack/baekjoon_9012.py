# 백준 - 9012번 (괄호)

n = int(input())
for _ in range(n):
    stack = []
    s = input()
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif (s[i] == ')'):
            if stack:
                stack.pop()
            else: # )가 새로 들어왔지만 남은 괄호가 없을 경우 : NO
                print('NO')
                break
    else: # break문으로 끊기지 않고 수행됐을경우 else문 수행 
        # break문으로 끊기지 않고 스택이 비어있다면 VPS
        # break문으로 끊기지 않아도 스택이 비어있지 않다면 VPS 아님
        print('YES' if not stack else 'NO')
