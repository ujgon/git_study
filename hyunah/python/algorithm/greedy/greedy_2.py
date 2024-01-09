# 문자열 하나씩 자르기
word = "567"
result = 0

arr = list(word)

for i in range (len(arr)):

    number = int(arr[i])

    if result != 0 and number != 0:
        result *= number
    else:
        result += number

print(result)


