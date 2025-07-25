import sys
input = sys.stdin.readline

a, b = map(int, input().split())

list1 = list(map(int, input().split()))

list1.sort()

sumValue = [0]

for ia in range(a):
    sumValue.append(sumValue[ia] + list1[ia])

for i in range(b):
    k, q = map(int, input().split())

    print(sumValue[q] - sumValue[k-1])