import sys
input = sys.stdin.readline

n = int(input())
ans = 0

v1 = [0] * n
v2 = [0] * (2*n)
v3 = [0] * (2*n)

def back(num):
    global ans
    
    if n == num:
        ans += 1
        return
    
    for j in range(n):
        if v1[j] == v2[num+j] == v3[num-j] == 0:
            v1[j] = v2[num+j] = v3[num-j] = 1
            back(num+1)
            v1[j] = v2[num+j] = v3[num-j] = 0
            
back(0)
print(ans)