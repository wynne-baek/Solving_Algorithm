import sys

che = [True] * 1001
che[0], che[1] = False, False

for i in range(2, 1000):
    if che[i]:
        for j in range(2 * i, 1001 , i):
            che[j] = False

N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    if che[number] is True:
        cnt += 1
print(cnt)