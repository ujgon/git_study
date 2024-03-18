s = input()
result = 0

for i in s:
    # 0과 1일때는 더하는 것이 더 큰 숫자로 나온다.
    if result == 0 or result == 1:
        result += int(i)
    else:
        result *= int(i)

print(result)