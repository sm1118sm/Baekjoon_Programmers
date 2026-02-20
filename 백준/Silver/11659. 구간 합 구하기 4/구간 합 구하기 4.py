import sys

input = sys.stdin.readline

n, m = map(int, input().split())

list1 = list(map(int, input().split()))

sumList = [0]

sumValue = 0

for i in list1:
    sumValue += i
    sumList.append(sumValue)
    
for j in range(m):
    k, q = map(int, input().split())
    
    print(sumList[q] - sumList[k-1])