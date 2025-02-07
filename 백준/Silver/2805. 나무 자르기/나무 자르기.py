import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

while start <= end:
    h = (start + end) // 2
    wood_sum = sum(tree - h if tree > h else 0 for tree in trees)
    
    if wood_sum >= M:
        result = h
        start = h + 1
    else:
        end = h - 1

print(result)
