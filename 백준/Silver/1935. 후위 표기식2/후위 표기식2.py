import sys
from collections import deque

input = sys.stdin.readline

num = int(input())

li = list(map(str, input().strip()))

num_li = [0] * num
temp = []

for i in range(num):
    num_li[i] = int(input())

for j in li:
    
    if j.isalpha():
        temp.append(num_li[ord(j)-ord('A')])
        
    else:
        b = temp.pop()
        a = temp.pop()
        
        if j == '+':
            temp.append(a + b)
        elif j == '-':
            temp.append(a - b)
        elif j == '*':
            temp.append(a * b)
        elif j == '/':
            temp.append(a / b)

print('%.2f' % temp[0])