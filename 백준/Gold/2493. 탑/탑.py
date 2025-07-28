import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))
stack = []
result = [0] * n  

for i in range(n):
    current_height = heights[i]

    while stack and stack[-1][1] < current_height:
        stack.pop()
    
    if stack:
        result[i] = stack[-1][0] + 1 

    
    stack.append((i, current_height))

print(' '.join(map(str, result)))
