# 동적계획법
import sys
x = []
N = int(input())

colors = [list(map(int, input().split())) for _ in range(N)]

for i in range(0, N-1):
    colors[i+1][0] += min(colors[i][1], colors[i][2])
    colors[i+1][1] += min(colors[i][0], colors[i][2])
    colors[i+1][2] += min(colors[i][0], colors[i][1])

res = min(colors[N-1])
print(res)