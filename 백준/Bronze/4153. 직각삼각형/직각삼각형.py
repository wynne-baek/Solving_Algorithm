while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    longer = max(a, b, c)
    if a ** 2 + b ** 2 + c ** 2 - longer ** 2 == longer ** 2:
        print('right')
    else:
        print('wrong')