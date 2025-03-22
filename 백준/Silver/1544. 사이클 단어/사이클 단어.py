import sys
input = sys.stdin.readline

N = int(input())

word_count = dict()

count = 0

for k in range(N):
    word = input().strip()

    if word in word_count:
        continue
    
    count += 1

    for i in range(len(word)):
        derived_word = word[i:] + word[:i]

        word_count[derived_word] = 1

print(count)