### 백준 - 10818번
# 내장함수 사용한 코드
cnt = int(input())
num_list = [n for n in map(int, input().split())]
print(min(num_list), max(num_list))

# 알고리즘을 이용한 코드
cnt = int(input())
num_list = [n for n in map(int, input().split())]
max = num_list[0]
min = num_list[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)
