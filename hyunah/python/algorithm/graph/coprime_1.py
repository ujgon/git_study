# 서로소 집합을 활용한 사이클 판별

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break

    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")