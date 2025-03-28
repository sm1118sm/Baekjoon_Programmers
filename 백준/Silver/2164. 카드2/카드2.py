import sys
from collections import deque

input = sys.stdin.readline

a = int(input())

deque1 = deque([i for i in range(1, a+1)])

while len(deque1) > 1:
    
    deque1.popleft()
    deque1.append(deque1.popleft())
    
print(deque1[0])