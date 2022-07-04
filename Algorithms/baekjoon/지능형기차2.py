total = 0
max_num = 0
for _ in range(10):
    o_num, i_num = map(int, input().split())
    total = total - o_num + i_num
    if total > max_num:
        max_num = total

print(max_num)
