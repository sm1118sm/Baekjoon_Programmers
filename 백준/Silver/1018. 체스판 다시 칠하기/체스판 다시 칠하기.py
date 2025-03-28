import sys
input = sys.stdin.readline

n1, n2 = map(int,input().split()) 

chess = []

for _ in range(n1):
    chess.append(input().strip()) 

result = [] 

for a in range(n1-7):
    for b in range(n2-7):
        
        index1 = 0
        index2 = 0 

        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0 :
                    if chess[i][j] != 'W':
                        index1 += 1
                    if chess[i][j] != 'B':
                        index2 += 1 
                else:
                    if chess[i][j] != 'B':
                        index1 += 1
                    if chess[i][j] != 'W':
                        index2 += 1 
        result.append(min(index1,index2)) 

print(min(result))