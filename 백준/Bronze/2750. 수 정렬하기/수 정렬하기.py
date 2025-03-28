import sys
input = sys.stdin.readline

n = int(input())

list1 = []

for _ in range(n):
    list1.append(int(input()))

list1.sort()

for i in range(n):
    print(list1[i])