import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

sumValue = [0]

list1 = list(map(int, input().split()))

for i in range(n):
    sumValue.append(sumValue[i] + list1[i])

count = int(input())

for i in range(count):
    a, b = map(int, input().split())

    print(str(sumValue[b] - sumValue[a-1]) + "\n")
    