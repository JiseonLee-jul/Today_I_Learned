def solution(priorities, location):
    answer = 0
    while True:
        # 1. 첫번째 요소의 중요도가 가장 높을 때 : 인쇄(pop)
        if priorities[0] == max(priorities):
            priorities.pop(0)
            answer += 1
            # 첫번째 요소가 요청한 문서였다면 : while 탈출 후 결과 도출
            if location == 0:
                break
            else:
                # 앞으로 한 칸 이동
                location -= 1
        # 2. 첫번째 요소의 중요도가 가장 높지 않다면 : pop -> push
        else:
            J = priorities.pop(0)
            priorities.append(J)
            # 첫번째 요소가 요청한 문서였다면 : 대기목록 맨 뒤로 보내기
            if location == 0:
                location = len(priorities) - 1
            else:
                # 앞으로 한 칸 이동
                location -= 1
    
    return answer
