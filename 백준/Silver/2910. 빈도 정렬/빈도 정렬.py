import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list1 = list(map(int, input().split()))

list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

result = []

for i in list2:
    result.append([i, list1.count(i)])

result.sort(key=lambda x : (-x[1]))

for i, q in result:
    for _ in range(q):
        print(i, end = " ")