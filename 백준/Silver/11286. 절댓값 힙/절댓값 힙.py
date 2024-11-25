import sys
import heapq

input = sys.stdin.readline

heap = []

num = int(input())

for i in range(num):
    value = int(input())

    if value == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (abs(value), value))