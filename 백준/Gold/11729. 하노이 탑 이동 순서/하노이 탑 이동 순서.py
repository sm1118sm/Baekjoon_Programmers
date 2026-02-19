import sys
input = sys.stdin.readline

n = int(input())
result = []

def hanoi(n, start, end, aux):
    if n == 1:
        print(start, end)
        return

    # 1) n-1개를 보조 기둥으로 이동
    hanoi(n - 1, start, aux, end)

    # 2) 가장 큰 원반 이동
    print(start, end)

    # 3) n-1개를 목표 기둥으로 이동
    hanoi(n - 1, aux, end, start)

# 전체 이동 횟수 출력 (2^n - 1)
print(2**n - 1)

# 하노이 실행
hanoi(n, 1, 3, 2)