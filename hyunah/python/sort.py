# 정렬 알고리즘
# sort()
# 리스트형의 메소드로 리스트 원본값을 직접 수정한다.
# 입력값을 리스트로만 받을 수 있다.

# sorted() 
# 리스트 원본 값을 유지하고 리스트 외에도 입력값을 받을 수 있다.

# 결론 : 원본이 필요 없고 시간, 공간 절약을 위해서는 sort() 함수를 사용, 원본을 유지하고 리스트 외 다른 자료형을 정렬할 때에는 sorted() 사용

# 버블 정렬 O(N^2)
def bubbleSort(arr):

    length = len(arr) - 1
    
    for i in range(length):
        for j in range(length-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr



arr = [1,10,4,2,6]

print(bubbleSort(arr))

# 개선된 버블 정렬 O(N)
def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        

        arr[j+1] = key

