# 백준 - 2581번
a = int(input())
b = int(input())
arr = []

for x in range(a, b+1):
    if x == 1:
        continue
    else:
        if all(x % i != 0 for i in range(2, x)):
            arr.append(x)

if len(arr) == 0:
    print('-1')
else:
    print(sum(arr))
    print(arr[0])
