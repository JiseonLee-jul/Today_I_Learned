# 백준 - 2309번
h_list = [int(input()) for _ in range(9)]
a = 0
b = 0
for i in range(8):
    for j in range(i + 1, 9):
        if sum(h_list) - (h_list[i] + h_list[j]) == 100:
            a, b = h_list[i], h_list[j]
            
h_list.remove(a)
h_list.remove(b)
h_list.sort()
for n in h_list:
    print(n)
