# 서로소 집합 : 공통 원소가 없는 두 집합
# 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 합집합 : 두개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# 찾기 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

# "합치기 찾기 자료구조(Union Find)"라고도 불린다.

# 1. 합집합
# 서로 연결된 두 노드 A, B를 확인한다.
# 최악의 경우 모든 노드를 확인하게 되어 시간 복잡도는 O(V)가 될 수 있다.
# 경로 압축 : 찾기 함수를 최적화하기 위한 방법으로 경로 압축(Path Compression)을 이용할 수 있다.
# 찾기 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신한다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    # 부모의 값이 루트와 동일해지도록 반복
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화


# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


# 각 노드별 합집합
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)


for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')


print('부모 테이블 : ', end = ' ')
for i in range(1, v+1):
    print(parent[i], end = ' ')