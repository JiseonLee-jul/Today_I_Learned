# 백준 - 10870번
### 내 풀이
num = int(input())
pivot = [0, 1]

for _ in range(num - 1):
    pivot.append(pivot[-1] + pivot[-2])
print(pivot[num])

### 재귀함수
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input())
print(fibonacci(num))
