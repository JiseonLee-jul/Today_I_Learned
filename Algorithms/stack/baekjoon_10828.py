# 백준 - 10828번
# 입출력 속도 비교 sys.stdin.readline() > raw_input() > input()
import sys
# n : 명령의 수
n = int(sys.stdin.readline())
# 초기 스택 설정
stack = []

### 스택 프로그램 작성 : Last-in-First-Out
for _ in range(n):
    op = sys.stdin.readline().split()
    
    # push : 정수 x 스택에 추가
    if op[0] == 'push':
        stack.append(op[1])
    # pop : 스택에서 맨 위의 정수 빼고, 그 수를 출력
    elif op[0] == 'pop':
        # 스택이 비었으면 -1 출력
        print(-1 if stack == [] else stack.pop())
    # size : 스택의 정수 개수 출력
    elif op[0] == 'size':
        print(len(stack))
    # empty : 스택이 비어있으면 1, 아니면 0 출력
    elif op[0] == 'empty':
        print(1 if stack == [] else 0)
    # top : 스택의 가장 위에 있는 정수 출력
    elif op[0] == 'top':
        # 스택이 비었으면 -1 출력
        print(-1 if stack == [] else stack[-1])
