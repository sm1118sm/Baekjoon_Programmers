import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

result = 0

for i in range(n - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        need = scores[i] - (scores[i + 1] - 1)
        result += need
        scores[i] = scores[i + 1] - 1

print(result)