# 백준 - 2693번
cnt = int(input())
for _ in range(cnt):
    n_list = list(map(int, input().split()))
    n_list.sort()
    print(n_list[-3])
