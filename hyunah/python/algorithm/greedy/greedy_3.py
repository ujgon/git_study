p = 5
n = "2 3 1 2 2"
arr = list(map(int, n.split(" ")))

# 1. 숫자 크기별로 정렬 - 오름차순
arr.sort()

result = 0
count = 0

# 2. 숫자 크기만큼 자르기
for i in arr:
    count += 1

    if count >=i:
        result += 1
        count = 0

print(result)