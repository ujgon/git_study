# 병사 배치하기
x = int(input())
array = list(map(int, input().split()))


def soldier(array):
    count = 0
    array_count = len(array)
    i = 1

    while i < len(array):
        if array[i-1] < array[i]:
            count += 1
            array.remove(array[i-1])
            i = i-1
            array_count-=1
        else:
            i += 1

    return count

print(soldier(array))

# 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence)
# 가장 길게 증가하는 부분 수열을 찾거나 가장 길게 감소하는 부분 수열을 찾으면 된다.
# D[]



