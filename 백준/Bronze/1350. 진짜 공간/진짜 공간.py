import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
size = int(input())

result = 0

for i in list1:
    if i >= size:
        if i % size != 0:
            result += size * (i // size + 1)
            
        else:
            result += size * (i // size)
        
    else:
        if i != 0:
            result += size
        
print(result)