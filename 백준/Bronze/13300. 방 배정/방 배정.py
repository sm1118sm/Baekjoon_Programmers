import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())

dictMen = {}
dictWomen = {}

for i in range(n):
    s, y = map(int, input().split())

    if s == 1:
        if y not in dictMen:
            dictMen[y] = 1

        else:
            dictMen[y] += 1

    elif s == 0:
        if y not in dictWomen:
            dictWomen[y] = 1

        else:
            dictWomen[y] += 1

count = 0

for kq in dictMen:
    if dictMen[kq] // k == 0:
        count += 1

    else:
        count += dictMen[kq] / k

for ks in dictWomen:
    if dictWomen[ks] // k == 0:
        count += 1

    else:
        count += dictWomen[ks] / k

print(math.ceil(count))
