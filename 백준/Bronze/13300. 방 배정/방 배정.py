import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0] * 7 for _ in range(2)]

for _ in range(n):
    s, g = map(int, input().split())
    arr[s][g] += 1      
    
result = 0

for i in range(2):
    for j in range(7):
        result += math.ceil(arr[i][j] / k)
        
print(result)