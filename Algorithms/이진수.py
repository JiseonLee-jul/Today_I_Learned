# 백준 3460
### 이진법 알고리즘
for _ in range(int(input)):
    n = int(input())
    i = 0
    while n >= 1:
        if n % 2 == 1:
            print(i, end = ' ')
        n = n // 2
        i += 1

### 내장함수 사용
for _ in range(int(input())):
    n = int(input())
    b = bin(n)[2:]
    for i in range(len(b)):
        if b[::-1][i] == '1':
            print(i, end = ' ')
