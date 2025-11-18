import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

current = list1[0]
sumValue = list1[0]

for i in range(1, n):
    value = list1[i]
    
    current = max(value, current + value)
    
    if current > sumValue:
        sumValue = current
        
print(sumValue)