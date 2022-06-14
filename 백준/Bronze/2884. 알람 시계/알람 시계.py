si, bun = map(int, input().split())
if 45 <= bun:
    print(si, bun-45)
else:
    if si == 0:
        print(23, bun + 15)
    else:
        print(si-1, bun + 15)