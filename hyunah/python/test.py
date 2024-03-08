n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (i+1, a, b, a+b))





# import sys

# T = int(input())

# for i in range(T):
#     a,b = map(int,sys.stdin.readline().split())
#     print(f"Case #{i+1}: {a} + {b} = {a+b}")