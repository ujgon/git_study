# 1로 만들기
# 각각의 값으로 나눴을 때 가장 적게 횟수가 나오는 경우
# 최적 부분 구조와 중복 부분 문제

n = int(input())

d = [0] * 30001

for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

    if i%5 == 0:
        d[i] = min(d[i], d[i//5] + 1)


print(d[x])