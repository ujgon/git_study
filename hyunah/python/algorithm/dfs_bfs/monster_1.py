from collections import deque


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

def solution(maps):

    n = len(maps)
    m = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                    continue

                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
    bfs(0,0)

    result = maps[n-1][m-1]

    if result == 1:
        return -1

    return result


print(result)