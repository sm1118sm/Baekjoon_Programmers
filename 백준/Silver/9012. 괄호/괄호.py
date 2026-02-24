import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    value = input().strip()

    is_valid = True

    for ch in value:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                is_valid = False
                break

    if stack:
        is_valid = False

    if is_valid:
        print("YES")
    else:
        print("NO")