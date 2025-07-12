import sys
input = sys.stdin.readline

a, b = map(int, input().split())
list1 = list(map(int, input().split()))

sumValue = [0]

result = []

for i in range(a):
    sumValue.append(sumValue[i] + list1[i])

for j in range(a-b+1):
    result.append(sumValue[b+j] - sumValue[j])

print(max(result))