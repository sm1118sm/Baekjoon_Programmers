import sys
input = sys.stdin.readline

n, L = map(int, input().split())
x = list(map(int, input().split()))

list1 = [0] * (n + 1)
for i in range(n):
    list1[i + 1] = list1[i] + x[i]

result = True
for i in range(n - 1):
    count = n - (i + 1)
    if count == 0:
        continue  

    total = list1[n] - list1[i + 1]
    avg = total / count

    if not (x[i] - L < avg < x[i] + L):
        result = False
        break

if result:
    print("stable")

else:
    print("unstable")