# 음료수 얼려먹기
# 구멍이 뚫려있는 부분이 0, 칸막이가 존재하는 부분이 1
# 한쪽이라도 붙어있으면 연결되어있는 것으로 간주

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))
count = 0

def baverage(x, y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if array[x][y] == 0:
        array[x][y] = 1

        baverage(x-1, y)
        baverage(x, y-1)
        baverage(x+1, y)
        baverage(x, y+1)

        return True
    return False

for i in range(n):
    for j in range(m):
        if baverage(i, j) == True:
            count += 1

print(count)




