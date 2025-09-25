import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

n, m = len(A), len(B)
prev = [0] * (m + 1)   # 직전 행
ans = 0

for i in range(1, n + 1):
    cur = [0] * (m + 1)        # 현재 행
    ai = A[i - 1]
    for j in range(1, m + 1):
        if ai == B[j - 1]:
            cur[j] = prev[j - 1] + 1
            if cur[j] > ans:
                ans = cur[j]    # 최댓값 즉시 갱신
        # else: cur[j] = 0  (기본값 0)
    prev = cur                  # 다음 턴을 위해 이전 행 교체

print(ans)
