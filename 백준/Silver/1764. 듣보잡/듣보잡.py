import sys

N, M = map(int, input().split())
neverHeard = set()
neverSeen = set()
cnt = 0
res = []

for _ in range(N):
    neverHeard.add(sys.stdin.readline().strip())
for _ in range(M):
    neverSeen.add(sys.stdin.readline().strip())

res = sorted(neverHeard & neverSeen)

print(len(res))
for ss in res:
    print(ss)