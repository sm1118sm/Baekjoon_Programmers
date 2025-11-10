import sys
input = sys.stdin.readline

n,m = map(int, input().split())

list1 = list(map(int, input().split()))

result = []
maxValue = max(list1)
visited = [False] * (maxValue+1)

def back(num):
    if num == m:
        print(*result)
        return
    
    for i in sorted(list1):
        if not visited[i]:
            result.append(i)
            visited[i] = True
            back(num+1)
            result.pop()
            visited[i] = False   
back(0)