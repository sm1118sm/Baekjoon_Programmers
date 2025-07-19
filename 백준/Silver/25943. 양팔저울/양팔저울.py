import sys
input = sys.stdin.readline

weights = [100, 50, 20, 10, 5, 2, 1]

n = int(input())
stones = list(map(int, input().split()))

left = stones[0]
right = stones[1]

for i in range(2, n):
    if left == right:
        left += stones[i]
    elif left < right:
        left += stones[i]
    else:
        right += stones[i]

diff = abs(left - right)

count = 0
for w in weights:
    count += diff // w
    diff %= w

print(count)