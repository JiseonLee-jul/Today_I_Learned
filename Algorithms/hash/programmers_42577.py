# 1. Double Loop Solution
def solution(phone_book):
    # 비교 횟수 : n*(n-1)/2
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
                break
            if phone_book[j].startswith(phone_book[i]):
                return False
                break
    return True

# 2. Sort and Loop Solution
def solution(phone_book):
    # 1. phone_book sorting
    phone_book.sort()
    
    # 2. sorting 결과를 바탕으로 앞 뒤 요소만 체크
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
            break
    
    return True

# 3. Hash solution
def solution(phone_book):
  # 1. Hash map 생성
    hash_map = {}
    for num in phone_book:
        hash_map[num] = 1

    # 2. 접두어가 Hash map에 존재하는지 찾기
    for num in phone_book:
        s = ''
        for n in num:
            s += n
            if (s in hash_map) and (s != num):
                return False
    return True
