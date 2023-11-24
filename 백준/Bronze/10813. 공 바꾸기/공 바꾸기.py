import sys
N, M = map(int, input().split())
x = [i for i in range(1, N+1)]

for i in range(M):
    a, b = map(int, input().split())
    c = x[a-1]
    x[a-1] = x[b-1]
    x[b-1] = c

print(*x)