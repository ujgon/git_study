# 재귀함수
# 자기 자신을 호출하는 함수
# 재귀함수를 풀이해서 사용할 때에는 반드시 종료 조건을 명시해야한다.

def recursive_function(i):
    if i==100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)


def factorial_recursive(n):
    if n <= 1:
        return 1

    return n*factorial_recursive(n-1)


print(factorial_recursive(5))