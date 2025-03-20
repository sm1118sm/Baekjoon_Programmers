import sys
input = sys.stdin.readline

n = int(input())
list1 = []

for i in range(n):
    list1.append((int(input()), i))
    
maxValue = 0
bubble = sorted(list1)

for i in range(n):
    if maxValue < bubble[i][1] - i:
        maxValue = bubble[i][1] - i
        
print(maxValue + 1)