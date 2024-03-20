n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))
# 방향이 필요하니 방향 벡터를 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 함수 만들기
def miro2(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if array[nx][ny] == 0:
                continue

            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y]+1
                queue.append((nx, ny))

    return array[x-1][y-1]


print(miro2(0,0))


