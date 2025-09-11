import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1000000007
    print(b % 1000000007)