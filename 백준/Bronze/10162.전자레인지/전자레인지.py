T = int(input())
a = b = c = 0
a = T // 300
b = (T % 300) // 60
if (((T % 300) % 60) % 10 ==0):
    c = ((T % 300) % 60) // 10
    print(f'{a} {b} {c}')
else:
    print(-1)