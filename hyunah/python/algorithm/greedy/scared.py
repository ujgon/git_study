# 내 풀이
# 내림차순
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
result = 0

while len(a) != 0:
    del a[0: a[0]]
    result += 1
print(result)

# 이테코
# 오름차순
# 여기서 내가 놓친 것은 모든 사람들이 그룹에 들어가야할 필요가 없다는 것이다.
# 위에서는 모든 사람들이 그룹에 속하는 경우 중 가장 많은 그룹인 경우로 생각하고 풀어서 내림차순 해법이 맞지만
# 모든 사람들이 그룹에 들어갈 필요가 없다면 오름차순으로 적은 공포도로 그룹을 구성하는 것이 맞다.
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1
        count = 0
print(result)