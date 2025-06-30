import sys
input = sys.stdin.readline

n = int(input())

list1 = list(map(int, input().split()))

list2 = list(set(list1))

list2.sort()

dic1 = {}

count = 0

for i in list2:
    dic1[i] = count
    count += 1

for k in list1:
    print(dic1[k], end = " ")