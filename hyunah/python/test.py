n = int(input())

for i in range(n):
    m = int(input())

    d = [0] * (10*m+1)

    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, m+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    print(d[m])