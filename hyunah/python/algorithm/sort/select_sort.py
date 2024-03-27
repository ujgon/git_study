# 선택 정렬 처리되지 않은 가장 작은 데이터를 선택하여 맨 앞에 있는 데이터와 바꾸는 것을 반복하는 정렬 방식
# O(n^2)
# 선택 정렬 vs 기본 정렬 라이브러리 = 기본 정렬이 훨씬 빠르다.

array = [5, 1, 6, 8, 9, 2, 3, 0, 4, 7]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print(array)


