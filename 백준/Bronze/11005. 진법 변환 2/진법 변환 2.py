from collections import deque
import sys
input = sys.stdin.readline

al = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

list1 = deque([])

a, b = map(int, input().split())

while True:
    
    if a < b:
        list1.appendleft(al[a])
        break

    mod = a % b
    a = a // b
    list1.appendleft(al[mod])

for i in list1:
    print(i, end="")

