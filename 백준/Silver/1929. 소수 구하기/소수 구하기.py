import sys
import math

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    if i < 2:  # 2보다 작은 숫자는 소수가 아님
        continue
    is_prime = True  # 소수 여부 플래그
    sq = int(math.sqrt(i))  # √i 계산
    for j in range(2, sq + 1):  # 2부터 √i까지 확인
        if i % j == 0:  # 나누어떨어지면 소수가 아님
            is_prime = False
            break
    if is_prime:  # 소수라면 출력
        print(i)