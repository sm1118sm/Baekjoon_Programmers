import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
stack = []
expected = 1  # 받을 간식 번호

for student in line:
    # 일단 줄의 학생을 스택에 넣는다
    stack.append(student)
    
    # 스택에서 꺼낼 수 있는 조건을 확인
    while stack and stack[-1] == expected:
        stack.pop()
        expected += 1

# 모두 간식을 받았는지 확인
if not stack:
    print("Nice")
else:
    print("Sad")
