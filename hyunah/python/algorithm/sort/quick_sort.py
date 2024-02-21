# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘
# 기본적인 퀵정렬은 첫번째 데이터를 기준 데이터(Pivot)로 설정
# Java, C++, Pytho도 정렬을 퀵정렬 기반으로 채택함

array = [5, 1, 6, 8, 9, 2, 3, 0, 4, 7]

def quick_sort(array, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while (left <= right):

        while (left <= end and array[left] <= array[pivot]):

            left += 1

        while (right > start and array[right] >= array[pivot]):

            right -= 1

        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)

