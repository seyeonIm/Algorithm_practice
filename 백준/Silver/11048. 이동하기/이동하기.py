import sys 

# DP (오,아,오른쪽아래 대각선) 이동 가능
N, M = map(int, input().split())
board = []
for _ in range(N,):
    board.append(list(map(int, input().split())))

# 1 2 3 4
# 0 0 0 5
# 9 8 7 6

# 첫 행 업데이트
for i in range(1, M):
    board[0][i] += board[0][i-1]

# print(board)

for i in range(1, N):
    for j in range(M):
        if j == 0:
            board[i][0] += board[i-1][0]
        else:
            board[i][j] += max(board[i][j-1], board[i-1][j], board[i-1][j-1])


print(board[N-1][M-1])
