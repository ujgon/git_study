# 파이썬의 장점을 살린 퀵정렬 방법

array = [5, 1, 6, 8, 9, 2, 3, 0, 4, 7]

def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]  # pivot 보다 작으면 left_side 리스트에 담김
    right_side = [x for x in tail if x > pivot]  # pivot 보다 크면 right_side 리스트에 담김

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))