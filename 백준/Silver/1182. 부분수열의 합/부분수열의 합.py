import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list1 = list(map(int, input().split()))

count = 0

def back(num, value , cnt):
    global count
    if n == num:
        if value == m and cnt > 0:
            count += 1
        return
    
    back(num+1, value + list1[num], cnt+1)
    back(num+1, value, cnt)
    
back(0,0,0)

print(count)