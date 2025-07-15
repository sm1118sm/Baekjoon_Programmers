import sys
input = sys.stdin.readline

n = int(input())
room = [list(input().strip()) for _ in range(n)]

width = 0
height = 0

for i in range(n):
    cnt = 0
    for j in range(n):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                width += 1
            cnt = 0
    if cnt >= 2:
        width += 1


for j in range(n):
    cnt = 0
    for i in range(n):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                height += 1
            cnt = 0
    if cnt >= 2:
        height += 1

print(width, height)