# 최적화 문제를 결정 문제(예, 아니요)로 바꾸어 해결하는 기법
# 예) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 파라메트릭 서치 문제는 이진 탐색을 이용해서 해결

# 이 값으로 조건을 만족할 수 있는가? -> 조건 만족 여부(예, 아니요)에 따라서 탐색 범위를 좁혀서 해결
# 큰 탐색 범위인 경우 선형탐색보다는 이진 탐색을 떠올려야 한다.
from bisect import bisect_left, bisect_right


n, x = map(int, input().split())
a = list(map(int, input().split()))

# x = 2
# a = [1, 1, 1, 5, 8, 9, 6]

def search(a, x):
    right = bisect_right(a, x)
    left = bisect_left(a, x)

    return right - left


result = search(a, x)

if(result == 0):
    print(-1)
else:
    print(result)

