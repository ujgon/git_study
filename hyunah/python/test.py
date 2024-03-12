n=int(input())

for i in range(n-1):
    print(' '*(n-i-1)+'*'+' '*(2*i-1)+'*'*(i and 1))
    
print('*'*(2*n-1))
