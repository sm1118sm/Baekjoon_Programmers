import sys
import heapq

input = sys.stdin.readline

heap = []

n = int(input())

for i in range(n):
    a = int(input())
    
    if a == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        
        else:
            print(0)

    else:
        heapq.heappush(heap, a)