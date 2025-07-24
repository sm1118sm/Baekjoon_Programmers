import sys
input = sys.stdin.readline

n = int(input())

list1 = list(map(int, input().split()))

result = 0
result2 = 0

value = list1[0]
value2 = list1[-1]

maxValue = []

for i in range(len(list1)):
    if list1[i] >= value:
        result += 1
        value = list1[i]
        maxValue.append(result)

    else:
        result = 1
        value = list1[i]
        maxValue.append(result)

for s in list1[::-1]:
    if s >= value2:
        result2 += 1
        value2 = s
        maxValue.append(result2)

    else:
        result2 = 1
        value2 = s
        maxValue.append(result2)

print(max(maxValue))