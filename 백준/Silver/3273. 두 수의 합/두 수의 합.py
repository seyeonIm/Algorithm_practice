import sys
n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

cnt = 0
seen = set()

for i in range(n):
    complement = x - seq[i]
    if complement in seen:
        cnt += 1
    seen.add(seq[i])

print(cnt)