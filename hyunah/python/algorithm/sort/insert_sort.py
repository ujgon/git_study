# 삽입 정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
# 선택 정렬에 비해 구현 난이도는 높은 편이지만 일반적으로 더 효율적으로 동작함
# O(n^2)

array = [5, 1, 6, 8, 9, 2, 3, 0, 4, 7]

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break

# print(array)

for i in range(1, len(array)):
	for j in range(i, 0, -1):
	    if array[j] < array[j-1]:
		    array[j], array[j-1] = array[j-1], array[j]
	    else:
		    break

print(array)