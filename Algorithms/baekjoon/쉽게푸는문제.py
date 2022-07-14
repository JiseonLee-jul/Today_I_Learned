# 백준 -  1292번
a, b = map(int, input().split())
arr = [0]
for i in range(50):
    for j in range(i):
        arr.append(i)
print(sum(arr[a:b+1]))


a, b = map(int, input().split())
arr = []
for i in range(50) :
    for j in range(i):
        if len(arr) == b :
            break
        arr.append(i)
print(sum(arr[a-1:b]))
