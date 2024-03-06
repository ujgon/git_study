# 최소 신장 트리 알고리즘
# 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않은 부분 그래프를 의미한다.
# 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 한다.
# 모든 노드가 연결은 되어있지만 각 노드들끼리는 꼭 다 연결되지 않아도 되는 경우
# 예시 ) N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 방법

# 크루스칼 알고리즘
# 그리디 알고리즘으로 분류되며 최소 신장 트리 알고리즘이 포함된다.

# 과정
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 현재의 간선이 사이클을 발생시키는지 확인
# 사이클이 발생하지 않으면 최소 신장 트리에 포함시킨다.
# 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
# 3. 모든 간선에 대하여 2번의 과정을 반복한다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화하기


edges = []
result = 0


for i in range(1, v+1):
    parent[i] = i


for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


edges.sort()


for edge in edges:
    cost, a, b = edge
    if find_parent(parent, e) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


print(result)

# 크루스칼 알고리즘 성능 분석
# 크루스칼 알고리즘 간선의 개수가 E개 일 때 시간복잡도는 O(ElogE)의 시간 복잡도를 가진다.
