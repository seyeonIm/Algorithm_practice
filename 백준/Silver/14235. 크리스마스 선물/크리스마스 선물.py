import heapq

n = int(input())
heap = []
# li = list(map(int, sys.stdin.readline().split()) for _ in range(n))

for _ in range(n):
    x = list(map(int, input().split()))

    if x[0] != 0:
        for i in range(x[0]):
            heapq.heappush(heap, -x[i+1])
    else:
        if len(heap):
            print(-heapq.heappop(heap))
        else:
            print(-1)