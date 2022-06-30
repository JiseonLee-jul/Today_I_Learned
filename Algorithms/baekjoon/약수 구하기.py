### 약수 구하기 - 백준 2501
# 내 코드
N, K = map(int, input().split())

l = []
for i in range(1, N+1):
    if N % i == 0:
        l.append(i)

if len(l) >= K:
    answer = l[K-1]
else:
    answer = 0

print(answer)


# 참고할 코드
N, K = map(int, input().split())

result = 0

for i in range(1, N + 1):
    if N % i == 0:
        K -= 1
        if K == 0:
            result = i
            break

print(result)
