import sys
input = sys.stdin.readline

al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
al2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

value = input().strip()  
search = input().strip() 

setValue = set()
new_value = ''  

for i in value:
    if i not in setValue:
        new_value += i  
        setValue.add(i)  

for j in al:
    if j not in setValue:
        new_value += j

encodeMap = {}
for k in range(26):
    encodeMap[al[k]] = new_value[k]

result = ''

for m in search:
    result += encodeMap[m] 

print(result)