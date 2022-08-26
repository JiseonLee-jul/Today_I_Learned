def solution(numbers):
    # 자릿수별 정렬을 위해 str타입으로 변환
    numbers = list(map(str, numbers))
    numbers.sort(reverse = True, key = lambda x: x*3)
    
    return str(int(''.join(numbers)))
