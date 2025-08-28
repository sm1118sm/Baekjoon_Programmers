import sys

input = sys.stdin.readline

n = int(input())

dict1 = {}

for i in range(n):
    name, value = map(str, input().split())

    if name not in dict1:
        dict1[name] = value
    else:
        dict1[name] = value
    
    
newDict1 = sorted(dict1.items(), reverse=True)  
     
for (j, k) in newDict1:
    if k == 'enter':
        print(j)
    
    elif k == 'leave':
        continue
