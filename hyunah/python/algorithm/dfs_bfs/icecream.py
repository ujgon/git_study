# DFS 활용 - 지점을 갈 때마다 상,하,좌,우 살펴보면서 방문을 진행하는 과정 반복

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):

    if x <= -1 or y <= -1 or x > n or y > m:
        return False

    if graph[x][y] == 0:
        graph[x][y] == 1
        bfs[x+1][y]
        bfs[x][y+1]
        bfs[x-1][y]
        bfs[x][y-1]

        return True

    return False


result = 0

for i in range(n):
    for j in range(m):

        if bfs(i, j):
            result += 1

print(result)
