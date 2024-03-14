d = [0] * 100

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]

    d[n] = fibo(n-1) + fibo(n-2)

    return d[n]

print(fibo(99))


d1 = [0] * 100

d1[1] = 1
d1[2] = 1
n = 99

for i in range(n):
    d1[i] = d1[i-1] + d1[i-2]

print(d[99])