import sys

def primelist(num):
    arr = [True] * (num+1)
    arr[0], arr[1] = False, False
    m = int(num ** 0.5)
    for i in range(2, m+1):
        if arr[i] == True:
            for j in range(i+i, N+1, i):
                arr[j] = False
    return arr

M, N = map(int, sys.stdin.readline().split())
arr = primelist(N)
for idx in range(M, N+1):
    if arr[idx] == True:
        print(idx)