# BFS(Breadth-First Search)
# 너비 우선 탐색이라고도 하며 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
# 큐 알고리즘을 이용(선입선출이라 그런가?)
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
