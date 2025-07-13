import sys
input = sys.stdin.readline

n = int(input())

count = 0

for i in range(n):
    stack = []
    value = list(input().strip())
    for k in value:
        if len(stack) != 0:
            if stack[-1] == k:
                stack.pop()
            else:
                stack.append(k)
        else:
            stack.append(k)
            
    if len(stack) == 0:
        count += 1

print(count)