def solution(m, n, puddles):
    # n,m
    # 오른쪽, 아래쪽 []
    answer = 0
    board = []
    # m=4
    # n=3
    # puddles=[[2,1], [1,2]]
    # 초기화
    for i in range(n):
        if i == 0:
            board.append([1 for x in range(m)])
        else:
            board.append([0 for x in range(m)])
        board[i][0] = 1
    # print(board)
    
    for puddle in puddles:
        x, y = puddle
        board[y-1][x-1] = 0  # 웅덩이 위치를 0으로 설정

        # 첫 번째 행에 웅덩이가 있는 경우
        if y == 1:
            for j in range(x-1, m):
                board[0][j] = 0  # 웅덩이 이후의 모든 칸을 0으로 설정

        # 첫 번째 열에 웅덩이가 있는 경우
        if x == 1:
            for i in range(y-1, n):
                board[i][0] = 0  # 웅덩이 이후의 모든 칸을 0으로 설정
        
                       
    print("look")
    print(board)
    
    
    for i in range(1, n):
        for j in range(1, m):
            # 웅덩이 여러 개 있을 수 있음 ㅠㅠ
            if [j+1,i+1] in puddles:
                # board 재정의 아래 사각형 가로 세로 값 puddles 값과 유지
                continue
                
            
            board[i][j] += board[i][j-1] + board[i-1][j]
            
    print(board)
    
    print(board[n-1][m-1])
    answer = board[n-1][m-1]
    answer %= 1000000007
    
    # 1 1 1 1
    # 1 2 3 4
    # 1 3 6 10
    
    
    return answer