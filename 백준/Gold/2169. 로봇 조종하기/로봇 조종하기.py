import sys

# 탐사한 지역들의 가치의 합이 최대
N, M = map(int, input().split())

# 10 25 7 8 13 //
# 68 24 -78 63 32
# 12 -69 100 -29 -25
# -16 -22 -57 -33 99
# 7 -76 -11 77 15

dp = [] # 왼/오/아래O 위X
for _ in range(N):
    dp.append(list(map(int, input().split())))

# 첫 번째 행 업데이트
for i in range(1, M):
    dp[0][i] += dp[0][i-1]

# 왼->오 vs 오->왼 윗->아래 값 비교해서 DP 업데이트
for i in range(1, N):
    left2right = dp[i][:] # temp로 한행씩(단,dp0행 제외) 최종 DP 업데이트
    right2left = dp[i][:]

    for j in range(M):
        if j == 0: # 첫번째 열은 따로 빼서 업데이트(dp바로 윗값 더하기)
            left2right[0] += dp[i-1][0]
        else:
            left2right[j] += max(dp[i-1][j], left2right[j-1])
    
    #print(f'{i}행은 {left2right}')

    for j in range(M-1,-1, -1):
        if j == M-1:
            right2left[M-1] += dp[i-1][M-1]
        else:
            right2left[j] += max(dp[i-1][j], right2left[j+1])

    for j in range(M):
        dp[i][j] = max(left2right[j], right2left[j])


# print(dp)
print(dp[N-1][M-1])




# 오 -> 왼