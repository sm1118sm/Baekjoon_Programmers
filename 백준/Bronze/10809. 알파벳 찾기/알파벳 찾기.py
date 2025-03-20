import sys
input = sys.stdin.readline

al = "abcdefghijklmnopqrstuvwxyz"

list1 = [-1] * 26

n = list(input().strip())

for lk in range(len(n)):
    if list1[al.index(n[lk])] == -1:
        list1[al.index(n[lk])] = lk

for i in list1:
    print(i, end = " ")