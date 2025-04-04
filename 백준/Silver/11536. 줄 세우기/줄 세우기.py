import sys
input = sys.stdin.readline

n = int(input())

list1 = []

for i in range(n):
    value = input().rstrip('\n')
    list1.append(value)

sortedList = list(sorted(list1))
reversedList = list(sorted(list1, reverse=True))

if list1 == reversedList:
    print("DECREASING")

elif list1 == sortedList:
    print("INCREASING")

else:
    print("NEITHER")