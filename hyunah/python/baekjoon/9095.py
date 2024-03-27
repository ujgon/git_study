n = int(input())
array = [0] * (n+1)
array[1] = 9
array[2] = 17

for i in range(3, n+1):
    array[i] = array[i-1] + 18

print(array[n]%1000000000)