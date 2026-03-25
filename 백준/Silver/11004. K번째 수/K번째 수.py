import sys
input = sys.stdin.readline

a, b = map(int, input().split())
list1 = list(map(int, input().split()))

list1.sort()
print(list1[b-1])