N, H = map(int, input().split())
down = []
up = []
for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()

min_count = N
range_count = 0

def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1, H+1):
    down_count = len(down) - binary(down, i - 0.5, 0, len(down) - 1)
    up_count = len(up) - binary(up, H - i + 0.5, 0, len(up) - 1)

    if min_count == down_count + up_count:
        range_count += 1
    elif min_count > down_count + up_count:
        range_count = 1
        min_count = down_count + up_count
print(min_count, range_count)
