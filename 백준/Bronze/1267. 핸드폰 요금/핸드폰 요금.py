import sys
import math
input = sys.stdin.readline

n = int(input())
list1 = list(map(int, input().split()))

youngsik = 0
minsik = 0

for i in list1:
    if i % 30 != 0:
        youngsik += math.ceil(i / 30) * 10
        minsik += math.ceil(i / 60) * 15
        
    else:
        youngsik += ((i // 30) + 1) * 10
        minsik += ((i // 60) + 1) * 15
    
if youngsik > minsik:
    print(f"M {minsik}")
    
elif youngsik < minsik:
    print(f"Y {youngsik}")
    
else:
    print(f"Y M {minsik}")
    