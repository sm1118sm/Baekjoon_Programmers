import sys
input = sys.stdin.readline

n,m = map(int, input().split())

result = []
list1 = sorted(list(map(int, input().split())))

visited = [False] * n

def back(num):
    if num == m:
        print(*result)
        return
    
    value = 0
    
    for i in range(n):
        if not visited[i] and value != list1[i]:
                visited[i] = True
                result.append(list1[i])
                value = list1[i]
                back(num+1)
                result.pop()
                visited[i] = False             
back(0)