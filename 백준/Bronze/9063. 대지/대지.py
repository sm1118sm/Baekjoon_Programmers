import sys
input = sys.stdin.readline

n = int(input())

list1 = []
list2 = []

for i in range(n):
    a, b = map(int, input().split())
    list1.append(a)
    list2.append(b)

print((max(list1) - min(list1)) * (max(list2) - min(list2)))
