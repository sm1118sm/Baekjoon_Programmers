import sys
input = sys.stdin.readline

a, b = map(int, input().split())

dic1 = {}

for i in range(a):
    v1, v2 = map(str, input().split())
    dic1[v1] = v2

for j in range(b):
    value = input().rstrip()

    print(dic1[value])


