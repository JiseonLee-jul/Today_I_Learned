# 코드업 6096
# 리스트 공간 생성
baduk = [[]*19 for _ in range(19)]

# 입력값 받기
for i in range(19):
    baduk[i] = list(map(int, input().split()))

n = int(input())

# 십자 뒤집기
for i in range(n):
    x, y = map(int, input().split())
    
    # 가로 뒤집기
    for j in range(19):
        if baduk[x-1][j] == 0:
            baduk[x-1][j] = 1
        else :
            baduk[x-1][j] = 0
    # 세로 뒤집기        
    for j in range(19):
        if baduk[j][y-1] == 0:
            baduk[j][y-1] = 1
        else :
            baduk[j][y-1] = 0

# 출력    
for i in range(19):
    for j in range(19):
        print(baduk[i][j], end = ' ')
    print()
