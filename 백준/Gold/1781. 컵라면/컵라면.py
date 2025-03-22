import sys
from heapq import *
from collections import deque

input = sys.stdin.readline

length = int(input())

board = []

for i in range(length):
    deadline, cup_noodle = map(int, input().split())
    board.append((deadline, cup_noodle,))
    
board.sort(key=lambda x: (x[0], -x[1]))

board = deque(board)

pq, time = [], 1

while board:
    cur = board.popleft()
    
    if cur[0] >= time:
        
        heappush(pq, cur[1])
        time += 1
    elif pq[0] < cur[1]:
        
        heappop(pq)
        heappush(pq, cur[1])
        
print(sum(pq))