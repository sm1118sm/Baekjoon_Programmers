import sys

input = sys.stdin.readline

n = int(input())

list1 = []

stack = []


for i in range(n):
    result = list(map(str, input().split()))
    list1.append(result)

for i in range(n):
    if list1[i][0] == "push":
        stack.append(int(list1[i][1]))

    elif list1[i][0] == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    elif list1[i][0] == "size":
        print(len(stack))

    elif list1[i][0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif list1[i][0] == "top":
        if len(stack) != 0:
            print(stack[-1])

        else:
            print(-1)