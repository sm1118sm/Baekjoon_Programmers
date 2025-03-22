import sys
input = sys.stdin.readline

stackL = list(input().strip())

stackR = []

m = int(input())

for i in range(m):
    c = input().split()

    if c[0] == "L" and stackL:
        stackR.append(stackL.pop())
        
    elif c[0] == "D" and stackR:
        stackL.append(stackR.pop())
        
    elif c[0] == "B" and stackL:
        stackL.pop()
        
    elif c[0] == "P":
        stackL.append(c[1])

print("".join(stackL + list(reversed(stackR))))