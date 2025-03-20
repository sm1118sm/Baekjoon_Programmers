import sys

input = sys.stdin.readline

N = int(input())

left = 1
right = 1
val = 1
result = 1
while left <= right and right < N:
    if val > N:
        val -= left
        left += 1

    else:
        if val == N:
            result += 1
        right += 1
        val += right

print(result)