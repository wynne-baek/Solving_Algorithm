import heapq
import sys

N = int(sys.stdin.readline())
my_list = []
heapq.heapify(my_list)
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if my_list:
            print(heapq.heappop(my_list))
        else:
            print(0)
    else:
        heapq.heappush(my_list, x)