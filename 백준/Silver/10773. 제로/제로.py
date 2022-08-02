K = int(input())
nums = []
for _ in range(K):
    money = int(input())
    if money:
        nums.append(money)
    else:
        nums.pop()
print(sum(nums))