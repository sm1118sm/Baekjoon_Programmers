import sys
input = sys.stdin.readline

repeat = True

c = []

while repeat:
    
    result = 0
    
    n = int(input())
    
    split1 = list(str(n).strip())
    
    if n == 0:
        repeat = False
        
    else:
            
        for i in split1:
            if int(i) == 1:
                result += 2 + 2
                
            elif int(i) == 2:
                result += 3 + 2
                
            elif int(i) == 3:
                result += 3 + 2
                
            elif int(i) == 4:
                result += 3 + 2
                
            elif int(i) == 5:
                result += 3 + 2
                
            elif int(i) == 6:
                result += 3 + 2
                
            elif int(i) == 7:
                result += 3 + 2
                
            elif int(i) == 8:
                result += 3 + 2
                
            elif int(i) == 9:
                result += 3 + 2
                
            elif int(i) == 0:
                result += 4 + 2
                
        c.append(result-len(split1) + 1)
        
for i in c:
    print(i)