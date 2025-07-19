import sys
input = sys.stdin.readline

r, c = map(int, input().split())

rank = ['1','2','3','4','5','6','7','8','9']

count = [0] * 9

result = []

for i in range(r):
    value = list(map(str, input().strip()))

    index = 0
    intValue = 0

    for j in range(len(value)):
        if value[j] in rank:
            intValue = int(value[j])
            break
        else:
            index += 1
    if index != c:
        result.append([intValue, index])

start = 1

result.sort(key=lambda x : x[1], reverse=True)

maxValue = result[0][1]

for s, q in result:

    if maxValue > q:
        maxValue = q 
        start += 1

    count[s-1] = start
    
for jj in count:
    print(jj)