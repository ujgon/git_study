# 전보 문제
# 방향성이 있는 그래프
# 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 구분하여 출력

# 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있음

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []

    # 시작 노드로 가기 위한 최단 거리를 0으로 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q: #q가 비어있지 않다면
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)


for _ in range(m):
    x, y, z = map(int, input().split())
    # X번 노드에서 Y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드를 제외해야해서 count - 1
print(count - 1, max_distance)

