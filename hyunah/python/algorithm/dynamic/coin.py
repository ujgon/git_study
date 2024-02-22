n, m = map(int, input().split())

k = [0] * n

for i in range(n):
    k[i] = int(input())

d = [10001] * (m*1)

d[0] = 0

result = 0

for i in range(n):
    for j in range(k[i], m+1):



for i in range(2, m+1):

    for j in range(n):
        if i%k[j] == 0:
            d[i] = min(d[i], d[i//k[j]]+1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])
