import sys
from itertools import combinations
input = sys.stdin.readline

list1 = []
result = []

for _ in range(9):
    value = int(input())
    list1.append(value)

for i in range(1, len(list1) + 1):
    for j in list(combinations(sorted(list1), i)):
        if sum(list(j)) == 100 and len(list(j)) == 7:
            result.append(list(j))

for k in result[0]:
    print(k)

