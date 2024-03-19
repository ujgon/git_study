# stack 자료구조는 선입후출 자료구조이다.
# stack 자료구조는 삽입과 삭제 두가지로만 동작한다.
stack = []

stack.append(2)
stack.append(1)
stack.append(3)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.append(9)

print(stack[::-1])
print(stack)