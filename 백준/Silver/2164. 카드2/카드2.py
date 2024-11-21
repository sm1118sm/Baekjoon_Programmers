from collections import deque

n = int(input())

list1 = deque()

for i in range(1, n+1):
    list1.append(i)

while len(list1) > 1:
    list1.popleft()
    list1.append(list1.popleft())

print(list1[0])
