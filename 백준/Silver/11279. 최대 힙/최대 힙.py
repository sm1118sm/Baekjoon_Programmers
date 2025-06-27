import sys
import heapq

input = sys.stdin.readline

heap = []

n = int(input())

for i in range(n):
    a = int(input())

    if a != 0:
        heapq.heappush(heap, -a)
        
    else:
        if len(heap) != 0:
            print(-heapq.heappop(heap))
            
        else:
            print(0)