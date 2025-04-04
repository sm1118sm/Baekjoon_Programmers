import sys
from itertools import combinations
input = sys.stdin.readline

list1 = [64, 32, 16, 8, 4, 2, 1]

x = int(input())

result = 0
for j in range(len(list1)):
    for i in combinations(list1, j):
        if sum(i) == x:
            print(len(i))