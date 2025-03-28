import sys

input = sys.stdin.readline

stack = []

n = int(input())

for i in range(n):
    list1 = list(map(int, input().split()))

    if list1[0] == 1:
        stack.append(list1[1])

    elif list1[0] == 2:
        if len(stack) != 0:
            print(stack.pop())

        else:
            print(-1)

    elif list1[0] == 3:
        print(len(stack))
        

    elif list1[0] == 4:
        if len(stack) != 0:
            print(0)

        else:
            print(1)

    elif list1[0] == 5:
        if len(stack) != 0:
            print(stack[-1])

        else:
            print(-1)
        