# 내 풀이
# 아래 풀이는 완전 탐색과도 같다.
n = int(input())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if '3' in time:
                count += 1
print(count)