# 금광 문제
T = int(input())
n, m = map(int, input().split())
array = []
for i in range(m):
    array.append(list(map(int, input().split())))

d = [[0] * n for i in range(m)]


for j in range(1, m):
    for i in range(n):
        if i==0: left_up = 0
        else: left_up = dp[i-1][j-1]
        if i==n-1: left_down = 0
        else: left_up = dp[i]
        left = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0

for i in range(n):
    result = max(result, dp[i][m-1])

print(result)