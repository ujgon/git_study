# 계수 정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
# 계수 정렬은 데이터의 크기 범위가 제한되어있어 정수 형태로 표현할 수 있을 때 사용 가능
# 시간 복잡도 : O(N+K)
# 최종 리스트에 각 데이터가 몇 번 등장했는지 그 횟수가 기록된다.

array = [5, 1, 6, 8, 9, 2, 3, 0, 4, 7]

# 모든 원소를 포함하는 리스트 선언
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end='')


