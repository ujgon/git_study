from collections import deque

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def miro(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        print(queue)
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if array[nx][ny] == 0:
                continue

            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))


    return array[n-1][m-1]

print(miro(0,0))
