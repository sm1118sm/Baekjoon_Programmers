import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
x_dicts = defaultdict(int)
y_dicts = defaultdict(int)

for s in range(n):
    x, y = map(int, input().split())
    x_dicts[x] += 1
    y_dicts[y] += 1

answer = 0

for x in x_dicts:
    if x_dicts[x] >= 2:
        answer += 1

for y in y_dicts:
    if y_dicts[y] >= 2:
        answer += 1

print(answer)