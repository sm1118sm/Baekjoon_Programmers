import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())  

for i in range(n):
    
    data = list(map(int, input().split()))
    
    Ti = data[0]  
    
    soldiers = data[1:]  

    counter = Counter(soldiers) 
    
    most_common_num, most_common_count = counter.most_common(1)[0] 

    if most_common_count > Ti // 2:
        print(most_common_num)
        
    else:
        print("SYJKGW")
