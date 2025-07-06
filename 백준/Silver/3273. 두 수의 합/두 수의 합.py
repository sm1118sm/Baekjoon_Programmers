import sys
input = sys.stdin.readline

n = int(input())

numbers = sorted(list(map(int, input().split())))

x = int(input())

result = 0
left = 0
right = n-1

while left < right:

    now = numbers[left] + numbers[right]

    if now == x:
        result += 1
        left += 1

    elif now < x:
        left += 1

    else:
        right -= 1
        
print(result)