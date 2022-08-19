# do_work : 하루 작업량 적용하는 함수
def do_work(progresses, speeds):
    for i, (progress, speed) in enumerate(zip(progresses, speeds)):
            progresses[i] = progress + speed
    return progresses

def solution(progresses, speeds):
    answer = []
    # 전체 과정 반복 : progresses가 빈 리스트가 되기 전까지
    while progresses != []:
        # 1. 배포 가능 : 몇 개 배포 가능한지 세어보기
        cnt = 0
        while progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
            # progresses가 빈 리스트일 때 while 탈출
            if progresses == []:
                break
        # 1-1. 배포 가능할 때, answer에 append
        if cnt != 0:
            answer.append(cnt)    
        # 2. 배포 불가능 : 하루 작업 실시하기
        progresses = do_work(progresses, speeds)
        
    return answer
