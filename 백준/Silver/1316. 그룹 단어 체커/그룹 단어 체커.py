# 문자열
import sys

N = int(sys.stdin.readline())
group_word = N
for i in range(N):
    word = sys.stdin.readline().strip()
    for j in range(len(word)-1):
        if word[j] == word[j+1]: # 같으면 넘어가고
            continue
        elif word[j] in word[j+1:]:
            group_word -= 1
            break

print(group_word)