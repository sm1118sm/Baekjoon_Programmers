import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    sys.exit()
elif n == 2:
    print(3)
    sys.exit()

a, b = 1, 3

for i in range(3, n+1):
    a, b = b, (b + 2 * a) % 10007  

print(b)