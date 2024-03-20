n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))

count = 0

def dfs(x, y):

    if x<0 or y<0 or x>=n or y>=m:
        return False

    if array[x][y] == 0:

        array[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

        return True

    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)