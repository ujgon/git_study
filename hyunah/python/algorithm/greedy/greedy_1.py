# 그리디 알고리즘
# 탐욕적으로 얻은 해가 최적의 해가 되는 상황에서 사용할 수 있다.
# 시간 복잡도 분석 : O(K)

# 1이 될 때까지 N에서 1을 빼거나 N을 K로 나눔

N = 25
K = 5
count = 0

while N > 1:
    
    if N/K >= 1 and N%K == 0:
      N /= K
    else:
      N -= 1
    
    print("N : ", N)
    
    count += 1

print(count)

# 위 방식은 데이터가 적은 경우 모든 N을 검사하면서 할 수 있지만, 만약 10만개를 넘어가는 데이터 수라면 아래 방식이 더 맞다.

result = 0
N = 25
K = 5

while True:
   number = (N // K) * K # KeyPoint! 나눌 수 - (몫*나누는 수) = 나누는 수가 딱 떨어지게 하는 수
   result += N - number 

   N = number

   if N < K:
      break
   
   result += 1
   N //= K

result += (N-1)
print(result)

# 이 방법이 효율적인 이유는?
# 큰 수로 나눈다면 기하급수적으로 빠르게 줄일 수 있다.

