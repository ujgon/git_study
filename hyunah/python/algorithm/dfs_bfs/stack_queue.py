from collections import deque
# 그래프 탐색 알고리즘
# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다.
# 자료구조
# 스택 : 선입후출 삽입(append), 삭제(pop) 기능 시간 복잡도 : O(1) 

stack = []
stack.append(4)
stack.append(3)
stack.append(10)
stack.append(1)
stack.pop()
stack.append(5)
stack.pop()
stack.append(6)

print(stack[::-1])
print(stack)


# 큐 : 선입선출, 입구와 출구가 뚫려있는 터널과 같은 모습
# 큐를 구현할 때에는 deque 라이브러리를 사용하는 것을 추천
queue = deque()

queue.append(5)
queue.append(3)
queue.append(7)
queue.append(10)
queue.popleft()
queue.append(8)
queue.popleft()

print(queue)
queue.reverse() # 역순으로 바꾸기
print(queue)
