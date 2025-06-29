import sys
input = sys.stdin.readline

a, b = map(int, input().split())

sumValue = [0]

list1 = list(map(int, input().split()))

result = []

for i in range(len(list1)):
    sumValue.append(sumValue[i] + list1[i])


for i in range(a-b+1):
    result.append(sumValue[i+b] - sumValue[i])

print(max(result))