import sys

N = int(sys.stdin.readline())

word_count = dict()

count = 0

for s in range(N):
    word = sys.stdin.readline().rstrip()

    if word in word_count:
        continue
    
    count += 1

    for i in range(len(word)):
        derived_word = word[i:] + word[:i]

        word_count[derived_word] = 1

print(count)