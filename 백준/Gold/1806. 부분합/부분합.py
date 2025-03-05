import sys
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# print(arr)
# 10 15
# 5 1 3 5 10 7 4 9 2 8

left = 0              
right = 0             
min_length = N + 1    # 최소 구간 길이
temp_sum = arr[0]     # 현재 합

left = 0
right = 0
min_length = N+1
temp_sum = arr[0]

# 종료 조건 1. left<=right 2. right가 인덱스 N-1 넘어가면 안됨
while (left<=right):
    if temp_sum >= S:
        min_length = min(min_length, right-left+1)
        # 최소길이 비교 후 왼쪽만 이동
        temp_sum -= arr[left]
        left += 1
    else:
        right += 1
        if right < N:
            temp_sum += arr[right]
        else:
            break
if min_length == N+1:
    print(0)
else:
    print(min_length)