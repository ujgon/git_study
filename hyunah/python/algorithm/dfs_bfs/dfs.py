# dfs(Depth-First-Search) : 깊이 우선 탐색
# 깊은 부분을 우선적으로 탐색하는 알고리즘
# 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문을 처리한다.
# 더이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
# 가장 작은 숫자

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5]
]

visited = [False] * 5

dfs(graph, 1, visited)
