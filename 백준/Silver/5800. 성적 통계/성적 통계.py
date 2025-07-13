import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    list1 = list(map(int, input().split()))

    print(f"Class {i+1}")
    value = sorted(list1[1:])
    result = 0

    for i in range(len(value)-1):
        if result < value[i+1] - value[i]:
            result = value[i+1] - value[i]
    print(f"Max {max(value)}, Min {min(value)}, Largest gap {result}")
