import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
# cnt 초기화
max_num = numbers[-1]
cnt = 1
for i in range(n):
    temp = numbers.pop()
    if max_num < temp:
        cnt += 1
        max_num = temp

print(cnt)