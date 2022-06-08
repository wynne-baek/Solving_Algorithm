import sys
from collections import deque

def bfs(storage, ripe):
    global N
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while ripe:
        z, x, y, cnt = ripe.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (0 <= nx < N and 0 <= ny < M and 0 <= nz < H ) and storage[nz][nx][ny] == 0:
                storage[nz][nx][ny] = cnt + 1
                ripe.append((nz, nx, ny, cnt + 1))


M, N, H = map(int, input().split())
storage = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for __ in range(H)]
# print(storage)
ripe = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if storage[k][i][j] == 1:
                ripe.append((k, i, j, 1))
# print(ripe)
bfs(storage, ripe)
max_date = 0
# print(storage)
for floor in storage:
    for line in floor:
        if max_date < max(line):
            max_date = max(line)
        if line.count(0) > 0:
            print(-1)
            exit(0)
else:
    print(max_date-1)