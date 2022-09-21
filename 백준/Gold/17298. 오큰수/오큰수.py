import sys
from collections import deque

N = int(input())
nums = list(map(int, input().split()))

answer = [-1] * N
stack = deque()

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        answer[idx] = nums[i]
    stack.append(i)
print(*answer)