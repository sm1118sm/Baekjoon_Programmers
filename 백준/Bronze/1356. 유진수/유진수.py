import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
    
list1 = []

for i in range(0, len(n)-1):
    first = 1
    end = 1
    
    for j in range(0, i+1):
        first *= n[j]
        
    for k in range(i+1, len(n)):
        end *= n[k]
        
    if first == end:
        list1.append("YES")
        
    else:
        list1.append("NO")
        
if len(n) <= 1:
    print("NO")
    
else:
    if list1.count("YES") >= 1:
        print("YES")
        
    else:
        print("NO")
    

