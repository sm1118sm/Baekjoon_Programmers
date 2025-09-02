import sys
input = sys.stdin.readline

a = [0, 1]

num = int(input())

for i in range(1, num):
    a.append(a[i-1] + a[i])

print(a[num])