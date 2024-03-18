# 내 풀이
# 방향성은 잘 잡았지만 좀 더 깔끔한 해결법이 필요해보인다..
n = int(input())
a = list(input().split())
dx = [1, -1, 0, 0]  # D, U, R, L
dy = [0, 0, 1, -1]

x, y = 1, 1

for i in a:
    if i == 'D':
        if x + dx[0] > 0:
            x += dx[0]
    if i == 'U':
        if x + dx[1] > 0:
            x += dx[1]
    if i == 'R':
        if y + dy[2] > 0:
            y += dy[2]
    if i == 'L':
        if y + dy[3] > 0:
            y += dy[3]

print(x, "", y)

# 이코테
n = int(input())
a = input().split() # 이렇게만 해도 list가 되는구나
x, y = 1, 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
map = ['D', 'U', 'R', 'L']

for i in a:
    for m in range(len(map)):
        if map[m] == a:
            nx = x + dx[m]
            ny = y + dy[m]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x = nx
    y = ny

print(x, y)
