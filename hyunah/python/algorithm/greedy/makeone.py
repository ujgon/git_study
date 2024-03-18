# n, k = map(int, input().split())
# count = 0

# while n != 1:

#     if n % k == 0:
#         n //= k
#     else: n -= 1

#     count+=1

# print(count)

# 시간 복잡도는 어떻게 될까? O(log_k(n))

# 스킬 하나 배웠다
# (n//k)*k
# n이 k로 나누어 떨어지지 않는 경우 n보다 작은 수중 k로 나누어 떨어지는 가장 가까운 수를 알 수 있다.

a, p = map(int, input().split())
result = 0
while True:
    # 나누는 것이 최소의 방법을 구할 수 있으므로 p로 나눌 수 있는 수까지 1로 빼기
    target = (a // p) * p
    result += (a - target)
    a = target
     # 나누어 떨어지는 수만큼 1을 뺀 횟수
    if a < p:
        break
    result += 1
    a //= p
result += (a-1)
print(result)
