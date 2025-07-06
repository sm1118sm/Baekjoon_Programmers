import sys
input = sys.stdin.readline

a = list(map(int, input().strip()))

result = []

while True:
    if len(a) != 1:
        a = list(map(int, str(a[0] * a[1])))
        

    else:
        for i in range(10):
            result.append(a[0])
        break

if len(list(set(result))) == 1:
    print("FA")

else:
    print("NFA")