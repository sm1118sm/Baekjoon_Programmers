import sys

input = sys.stdin.readline

a = int(input())

list1 = [0, 1]

for i in range(a):
    list1.append(list1[i] + list1[i+1])

print(list1[a])