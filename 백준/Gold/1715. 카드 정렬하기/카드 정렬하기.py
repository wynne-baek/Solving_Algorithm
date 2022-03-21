import heapq
import sys


N = int(sys.stdin.readline())
cards = []
heapq.heapify(cards)
for _ in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(cards, card)
result = 0
while len(cards) != 1:
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    z = x + y
    result += z
    heapq.heappush(cards, z)
print(result)