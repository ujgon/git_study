# 재귀함수
# 연속적으로 함수를 호출하면 실제로는 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
# 이런 특성으로 스택을 사용해야할 때 구현상 스택 라이브러리 대신 재귀함수를 이용하는 경우가 많다.


def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return "1", (n * factorial_recursive(n-1))

print(factorial_iterative(5))
print(factorial_recursive(5))