import sys
input = sys.stdin.readline

num = input().strip()

count = [0]*10

for i in num:
    count[int(i)] += 1

six_nine = count[6] + count[9]

count[6] = (six_nine + 1) // 2
count[9] = 0

print(max(count))