import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())

result = math.gcd(a,b)

print("1" * result)