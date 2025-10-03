def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []

    for a in vowels:
        words.append(a)
        for b in vowels:
            words.append(a+b)
            for c in vowels:
                words.append(a+b+c)
                for d in vowels:
                    words.append(a+b+c+d)
                    for e in vowels:
                        words.append(a+b+c+d+e)
                        
    print(words)
    answer = words.index(word) + 1
    return answer