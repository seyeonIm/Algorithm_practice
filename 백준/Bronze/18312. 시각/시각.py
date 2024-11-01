N, K = map(int, input().split())

cnt = 0


# total = s + m * 60 + 60 * 60 * h
for h in range(0, N+1): 
    for m in range(0, 60):
        for s in range(0, 60):
            if s // 10 == K or s % 10 == K or h // 10 == K or h % 10 == K or m // 10 == K or m % 10 == K:
                cnt += 1

print(cnt)