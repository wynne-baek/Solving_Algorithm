import sys

T = int(input())
nums = [True]*10001
nums[0], nums[1] = False, False
for i in range(2, 101):
    for j in range(2, len(nums)//i):
        nums[i*j] = False
# print(nums)
for _ in range(T):
    n = int(input())
    result = []
    for idx in range(n//2 + 1):
        if nums[idx] and nums[n-idx]:
            result.append((abs(idx-n+idx), idx, n-idx))
    result = sorted(result)
    # print(result)
    print(result[0][1], result[0][2])