from collections import deque

def solution(begin, target, words):
    queue = deque([(begin, 0)])  # (단어, 단계 수)
    visited = [False] * len(words)  # 단어의 방문 여부 기록

    while queue:
        word, step = queue.popleft()

        if word == target:
            return step

        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word in words and not visited[words.index(new_word)]:
                    visited[words.index(new_word)] = True
                    queue.append((new_word, step + 1))

    return 0  # 변환할 수 없는 경우