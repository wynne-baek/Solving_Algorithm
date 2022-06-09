nums = []
max_num = -1
max_idx = 10000
for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        max_idx = i + 1
print(max_num)
print(max_idx)
