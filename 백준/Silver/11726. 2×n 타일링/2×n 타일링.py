import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

if n == 1:
    print(1)
    exit(0)

memo = [0] * (n+1)

memo[1] = 1
memo[2] = 2

for i in range(3, n+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 10007

print(memo[n])