import sys
input = sys.stdin.readline

dict = {}

n = int(input())

for _ in range(n):
    value = input().strip().split('.')
    
    if value[1] not in dict:
        dict[value[1]] = 1

    else:
        dict[value[1]] += 1

for i in sorted(dict):
    print(i, dict[i])