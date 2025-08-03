import sys
input = sys.stdin.readline

stack = []

list1 = list(input().strip())

for j in list1:
    if j == '<' and not stack:
        stack.append(j)

    elif j == '<' and stack:
        for ss in stack[::-1]:
            print(ss,end="")

        stack.clear()
        stack.append(j)

    elif j == ' ' and stack and '<' not in stack:
        for sss in stack[::-1]:
            print(sss,end="")
        
        print(end=" ")
        stack.clear()

    elif j == '>':
        stack.append(j)
        for sk in stack:
            print(sk,end="")

        stack.clear()

    else:
        stack.append(j)

if stack:
    for result in stack[::-1]:
        print(result,end="")
