import sys

data = sys.stdin.read().splitlines()

# 도시 가치 정보 저장
w = []

for i in range(10):
    w.append(list(map(int, data[i].split())))

# 소유 상태, 트레이드 제시, 담보 상태
own = data[10]
trade = data[11]
mortgage = data[12]

# 현금 정보
cash1 = int(data[13])  # 내 현금
cash2 = int(data[14])  # 상대 현금
trade_cash1 = int(data[15])  # 내가 제시한 현금
trade_cash2 = int(data[16])  # 상대가 제시한 현금

# 가중치 및 페널티
A = int(data[17])
B = int(data[18])

# 초기 재산 가치 계산
v1 = 0
v2 = 0
for i in range(10):
    count1 = sum(1 for j in range(4) if own[4*i+j] == '1')
    count2 = sum(1 for j in range(4) if own[4*i+j] == '2')
    
    if count1 > 0:
        v1 += w[i][count1-1]
        
    if count2 > 0:
        v2 += w[i][count2-1]

v1 += (cash1 * A) // 100

v2 += (cash2 * A) // 100

v1 -= sum(B for j in range(40) if mortgage[j] == '1' and own[j] == '1')

v2 -= sum(B for j in range(40) if mortgage[j] == '1' and own[j] == '2')

diff_before = v1 - v2

# 트레이드 적용
own = list(own)
cash1 -= trade_cash1
cash2 -= trade_cash2
cash1 += trade_cash2
cash2 += trade_cash1

for i in range(40):
    if trade[i] == '1':
        own[i] = '1'
        
    elif trade[i] == '2':
        own[i] = '2'

# 트레이드 후 재산 가치 계산
v1 = 0
v2 = 0
for i in range(10):
    count1 = sum(1 for j in range(4) if own[4*i+j] == '1')
    
    count2 = sum(1 for j in range(4) if own[4*i+j] == '2')
    
    if count1 > 0:
        v1 += w[i][count1-1]
        
    if count2 > 0:
        v2 += w[i][count2-1]

v1 += (cash1 * A) // 100
v2 += (cash2 * A) // 100

v1 -= sum(B for j in range(40) if mortgage[j] == '1' and own[j] == '1')
v2 -= sum(B for j in range(40) if mortgage[j] == '1' and own[j] == '2')

diff_after = v1 - v2

# 결과 출력
if diff_after >= diff_before:
    print("YES")
else:
    print("NO")
