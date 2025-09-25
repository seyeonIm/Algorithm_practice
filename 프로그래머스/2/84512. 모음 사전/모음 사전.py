def solution(word):
    vowels = ['A','E','I','O','U']
    cnt = 0

    for a in vowels:
        s1 = a
        cnt += 1
        if s1 == word: return cnt

        for b in vowels:
            s2 = s1 + b
            cnt += 1
            if s2 == word: return cnt

            for c in vowels:
                s3 = s2 + c
                cnt += 1
                if s3 == word: return cnt

                for d in vowels:
                    s4 = s3 + d
                    cnt += 1
                    if s4 == word: return cnt

                    for e in vowels:
                        s5 = s4 + e
                        cnt += 1
                        if s5 == word: return cnt
