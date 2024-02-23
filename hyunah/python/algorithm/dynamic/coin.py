n, m = map(int, input().split())

k = [0] * n

for i in range(n):
    k[i] = int(input())

d = [10001] * (m+1)

d[0] = 0

result = 0

for i in range(n):
    for j in range(k[i], m+1):
        print("j :", j)
        if d[j - k[i]] != 10001:
            d[j] = min(d[j], d[j-k[i]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])
