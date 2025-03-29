import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input()
pq = []

for i in range(n):
    heapq.heappush(pq, (s[i], i))  

removed_indices = set()
for _ in range(m):
    if pq:
        char, index = heapq.heappop(pq)
        removed_indices.add(index)

result = []
for i in range(n):
    if i not in removed_indices:
        result.append(s[i])

print("".join(result))