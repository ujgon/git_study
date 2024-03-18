# 내 풀이
n = input()
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]
array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = array.index(n[0]) + 1
# 아스키 코드를 활욜해도 좋다.
# ord? 유니코드 정소를 반환한다. 예를 들어 ord('a') 는 97을 반환한다.
# column = int(ord(n[0])) - int(ord('a')) + 1
y = int(n[1])
count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 9 or ny > 9:
        continue

    count += 1

print(count)
