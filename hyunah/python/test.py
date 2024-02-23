def solution(N, trees):

    answer = 0
    array = [0]*len(trees)

    # 가장 작은 x값을 가진 좌표 찾기
    for i in range(len(trees)):
        array.append(trees[i][0])

    small_x = array.index(min(array))

    small_y = trees[small_x][1]

    # 해당 좌표의 y값보다 작은 다른 좌표 값의 갯수 구하기
    for i in range(len(trees)):
        if small_y <= trees[i][1] and i != small_x :
            answer += 1

    return answer

lst = [[4, 3], [3, 1], [2, 2], [1, 4]]
print(solution(5, lst ))
