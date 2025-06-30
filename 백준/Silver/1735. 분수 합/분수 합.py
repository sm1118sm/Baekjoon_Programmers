import sys
import math
input = sys.stdin.readline

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

upValue = list1[0] * list2[1] + list1[1] * list2[0]
downValue = list1[1] * list2[1]

print(upValue // math.gcd(upValue, downValue), end = " ")
print(downValue // math.gcd(upValue, downValue))