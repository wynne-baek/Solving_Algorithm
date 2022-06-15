N = int(input())
dots = []
for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))
dots = sorted(dots)
for dot in dots:
    print(dot[0], dot[1])
