import sys
from collections import deque
l=deque([])
for i in range(int(input())):
    n=sys.stdin.readline().split()
    m=n[0]
    if m=='push':
        l.append(n[1])
    elif m=='pop':
        print(-1 if len(l)==0 else l.popleft())
    elif m=='size':
        print(len(l))
    elif m=='empty':
        print(1 if len(l)==0 else 0)
    elif m=='front':
        print(-1 if len(l)==0 else l[0])
    else:
        print(-1 if len(l)==0 else l[-1])