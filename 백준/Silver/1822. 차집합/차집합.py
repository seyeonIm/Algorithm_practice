import sys

A, B = map(int, sys.stdin.readline().split())
setA = set(map(int, sys.stdin.readline().split()))
setB = set(map(int, sys.stdin.readline().split()))

A_B = setA - setB
print(len(A_B))
if len(A_B) != 0:
    print(*sorted(A_B))