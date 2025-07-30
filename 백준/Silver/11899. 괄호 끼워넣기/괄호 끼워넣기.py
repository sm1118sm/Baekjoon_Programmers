import sys
input = sys.stdin.readline

list1 = list(input().strip())

stack = []

for i in list1:
    if not stack:
        stack.append(i)

    else:
        if i == '(':
            stack.append('(')

        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            
            else:
                stack.append(')')

print(len(stack))