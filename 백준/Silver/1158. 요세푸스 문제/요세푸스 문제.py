import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

deque1 = deque(range(1, n+1))

list1 = []

while deque1: 
    for i in range(k-1):
        deque1.append(deque1.popleft())
    list1.append(deque1.popleft())
    
print(str(list1).replace("[", "<").replace("]", ">"))
    


