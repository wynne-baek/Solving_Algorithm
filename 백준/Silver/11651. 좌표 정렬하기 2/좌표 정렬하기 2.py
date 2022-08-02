import sys

T = int(input())
spot = []
for _ in range(T):
    x, y = map(int, input().split())
    spot.append((y, x))
spot.sort()
for dot in spot:
    print(dot[1], dot[0])