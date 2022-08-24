from itertools import combinations 

def solution(clothes):
    # 1. clothes dict 만들기 : ex) {'headgear' : 2, 'eyewear' : 1}
    clothes_dict = {}
    for piece, category in clothes:
        if category in clothes_dict.keys():
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 1
    
    # 2. 부분집합 경우의 수 세기 : (2+1) * (1+1) - 1
    answer = 1
    for value in clothes_dict.values():
        answer *= (value + 1)
         
    return answer - 1
