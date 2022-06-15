N = int(input())
nums = list(map(int, input().split()))
max_num = max(nums)
all = 0
for num in nums:
    all += (num/max_num*100)
print(all/N)