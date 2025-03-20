import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
list1 = list(map(int, input().split()))

list1.sort()

count = 0
front = 0
end = n - 1

while front < end:
    if list1[front] + list1[end] < m:
        front += 1
        
    elif list1[front] + list1[end] > m:
        end -= 1
        
    else:
        count += 1
        front += 1
        end -= 1
        
print(count)