import sys

n = int(input())
k = int(input())
cards = [] # depth
visited = [False] * n
results = set()

for _ in range(n):
    cards.append(sys.stdin.readline().strip())

def dfs(path):
    if len(path) == k:
        results.add(''.join(path))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(path + [cards[i]])

            visited[i] = False


dfs([])
print(len(results))
