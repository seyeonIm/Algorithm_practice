from collections import deque

def solution(maps):
    answer = bfs(maps)
    return answer

def bfs(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])
    visited = [[False] * m for _ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, dist = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]

            if 0 <= newX < n and 0 <= newY < m and visited[newX][newY] != True and maps[newX][newY] == 1:
                visited[newX][newY] = True
                queue.append((newX, newY, dist+1))

    return -1
