from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0)) # 처음단어, 전환수
    
    visited = [False] * len(words)

    while queue:
        word, step = queue.popleft()

        if word == target:
            return step    
        
        
#                 for i in range(len(word)):
#             for char in 'abcdefghijklmnopqrstuvwxyz':
#                 new_word = list(word)
#                 new_word[i] = char
#                 new_word = ''.join(new_word)

#                 if new_word in words and new_word not in visited:
#                     visited.add(new_word)
#                     queue.append((new_word, step + 1))
        
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                
                # visited[words에서 word의 index]
                if new_word in words and not visited[words.index(new_word)]:
                    visited[words.index(new_word)] = True
                    queue.append((new_word, step + 1))

def solution(begin, target, words):
    if target not in words:
        return 0

    answer = bfs(begin, target, words)
    return answer
