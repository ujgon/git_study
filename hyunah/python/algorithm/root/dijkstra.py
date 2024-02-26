# 다익스트라 최단 경로 알고리즘
# 특정한 노드에서 출발해서 다른 모든 노드로 가는 최단 경로 계산
# 음의 간선이 없는 경우에 정상적으로 동작함
# 최단 경로 알고리즘은 그리디 알고리즘으로 분류됨
# 매 상황에서 가장 비용이 적은 노드를 선택

# 즉, 각 노드별로 노드의 최단 거리 정보를 가지고 있음
# 그리고 한번 처리된 노드의 최단 거리 값은 고정되어 더이상 바뀌지 않는다.

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 반복 처리
        now = get_smallest_node()
        visited[now] = True
    for j in graph[now]:
        cost = distance[now] + j[1]
        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[j[0]]:
            distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])