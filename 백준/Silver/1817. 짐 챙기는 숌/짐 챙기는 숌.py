import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N > 0:
    books = list(map(int, input().split()))
    weight, cnt = 0, 1
    for book in books:
        if weight + book <= M:
            weight += book
        else:
            weight = book
            cnt += 1
    print(cnt)
else:
    print(0)