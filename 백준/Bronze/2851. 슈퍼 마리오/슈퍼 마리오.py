import sys
input = sys.stdin.readline

sumValue = [0]

for i in range(10):
    value = int(input())
    sumValue.append(sumValue[i] + value)

result = []

for i in sumValue:
    result.append(abs(100 - i))

count = 0
value = 100

for i in result:
    if i <= value:
        value = i
        count += 1

print(sumValue[count-1])