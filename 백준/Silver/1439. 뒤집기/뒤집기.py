import sys
input = sys.stdin.readline

s = input().strip()
count = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
print((count + 1) // 2)