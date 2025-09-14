import sys
input = sys.stdin.readline

n = int(input())

count = 1
value = set(["ChongChong"])

for _ in range(n):
    a, b = input().split()
    
    if a in value or b in value:
        value.add(a)
        value.add(b)

print(len(value))