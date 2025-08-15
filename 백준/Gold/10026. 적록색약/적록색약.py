import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = []
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(input().strip()))

def bfsR(x,y):
    que = deque()
    que.append((x,y))
    visited1[x][y] = True
    global count1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited1[nx][ny] and graph[nx][ny] == 'R':
                visited1[nx][ny] = True
                que.append((nx,ny))
                count1 += 1


def bfsG(x,y):
    que = deque()
    que.append((x,y))
    visited1[x][y] = True
    global count2

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited1[nx][ny] and graph[nx][ny] == 'G':
                visited1[nx][ny] = True
                que.append((nx,ny))
                count2 += 1


def bfsB(x,y):
    que = deque()
    que.append((x,y))
    visited1[x][y] = True
    global count3

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited1[nx][ny] and graph[nx][ny] == 'B':
                visited1[nx][ny] = True
                que.append((nx,ny))
                count3 += 1

def bfsRG(x,y):
    que = deque()
    que.append((x,y))
    visited2[x][y] = True
    global count4

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited2[nx][ny] and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                visited2[nx][ny] = True
                que.append((nx,ny))
                count4 += 1


def bfsB2(x,y):
    que = deque()
    que.append((x,y))
    visited2[x][y] = True
    global count5

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited2[nx][ny] and graph[nx][ny] == 'B':
                visited2[nx][ny] = True
                que.append((nx,ny))
                count5 += 1

list1 = []
list2 = []

for x in range(n):
    for y in range(n):
        if graph[x][y] == 'R' and not visited1[x][y]:
            count1 = 1
            bfsR(x,y)
            list1.append(count1)

        elif graph[x][y] == 'G' and not visited1[x][y]:
            count2 = 1
            bfsG(x,y)
            list1.append(count2)

        elif graph[x][y] == 'B' and not visited1[x][y]:
            count3 = 1
            bfsB(x,y)
            list1.append(count3)
        
for x in range(n):
    for y in range(n):
        if (graph[x][y] == 'R' or graph[x][y] == 'G') and not visited2[x][y]:
            count4 = 1
            bfsRG(x,y)
            list2.append(count4)

        elif graph[x][y] == 'B' and not visited2[x][y]:
            count5 = 1
            bfsB2(x,y)
            list2.append(count5)

print(len(list1), len(list2))