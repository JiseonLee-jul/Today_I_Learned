n = int(input())
n_list = list(map(int, input().split()))
cnt = 0

for n in n_list:
    if n == 1:
        # continue
        cnt += 0
    elif n >= 2:
        if all(n % i != 0 for i in range(2, n)):
            cnt += 1
    
print(cnt)
