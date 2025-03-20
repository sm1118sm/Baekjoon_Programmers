import sys
input = sys.stdin.readline

a, b = map(int, input().split())

list1 = [i for i in range(1, a+1)]

for i in range(b):
    s, y = map(int, input().split())

    newList1 = list1[s-1 : y]

    newList1.reverse()

    list1[s-1 : y] = newList1


for j in list1:
    print(j, end=" ")
