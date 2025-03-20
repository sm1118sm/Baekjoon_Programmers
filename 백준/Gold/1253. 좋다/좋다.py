import sys
input = sys.stdin.readline

n = int(input())
result = 0
a = list(map(int, input().split()))
a.sort()

for i in range(n):
    find = a[i]
    j = 0
    k = n - 1
    while j < k:
        if a[j] + a[k] == find:
            if j != i and k != i:
                result += 1
                break
                
            elif j == i:
                j += 1
                
            elif k == i:
                k -= 1
                
        elif a[j] + a[k] < find:
            j += 1
            
        else:
            k -= 1
            
print(result)