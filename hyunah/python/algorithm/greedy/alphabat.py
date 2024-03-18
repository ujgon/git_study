a = input()
array = []
alphabat = []
number = 0
for i in a:
    array.append(i)
for i in array:
    if ord(i) >= 48 and ord(i) <= 57:
        number += int(i)
    else:
        alphabat.append(i)
result = ""
alphabat.sort()
for i in alphabat:
    result += i

print(result + str(number))

# 이테코
data = input()
result = []
value = 0

for x in data:
    # 알파벳인 경우
    if x.isalpha():
        result.append(x)
    else:
        value += x

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
