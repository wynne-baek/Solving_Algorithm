a = int(input())
for i in range(a):
    arr = sorted(list(map(int, input().split())))
    print(arr[-3])