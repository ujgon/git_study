# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산하는 알고리즘이다.
# 다익스트라 알고리즘과 마찬가지로 단계별로 거쳐가는 노드를 기준으로 알고리즘을 수행한다.
# 다익스트라 알고리즘과의 차이점은 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다는 것이다.
# 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장한다.
# 플로이드 워셜 알고리즘은 다이나믹 프로그래밍 유형에 속한다.
# 시간 복잡도는 O(n^3)이다.
# 노드의 갯수가 500 이하인 경우가 좋다. 500*500*500은 1억을 넘기 때문

# 특정한 노드 K를 거쳐가는 경우를 확인한다.
# a에서 b로 가는 거리와 a에서 k를 거쳐 b로 갈 때 거리를 비교하여 더 짧은지 확인한다.
# 점화식 : Dab = min(Dab, Dak+Dkb) -> a에서 b로 가는 거리는 기존의 a에서 b로 가는 거리와 a에서 k로 가는 거리, k에서 b로 가는 거리를 비교한다.

INF = int(1e9) # 10억으로 설정

n = int(input())
m = int(input())

# 2차원 리스트를 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신 -> 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 받아서 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용을 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 점화식을 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a,b], graph[a,k]+graph[k][b])


for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
