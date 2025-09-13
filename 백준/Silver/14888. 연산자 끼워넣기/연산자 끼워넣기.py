import sys
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))
value = list(map(int, input().split()))

maxValue = -int(1e9)
minValue = int(1e9)

def dfs(m, result, plus, minus, multiple, divide):
    global maxValue, minValue

    if m == n:
        maxValue = max(maxValue, result)
        minValue = min(minValue, result)
        return
    
    if plus:
        dfs(m+1, result + list1[m], plus-1, minus, multiple, divide)
    
    if minus:
        dfs(m+1, result - list1[m], plus, minus-1, multiple, divide)

    if multiple:
        dfs(m+1, result * list1[m], plus, minus, multiple-1, divide)
    
    if divide:
        if result < 0:
            dfs(m+1, -(-result // list1[m]), plus, minus, multiple, divide-1)
        else:
            dfs(m+1, result // list1[m], plus, minus, multiple, divide-1)

dfs(1, list1[0], value[0], value[1], value[2], value[3])

print(maxValue)
print(minValue)