n = 5

h = 0
m = 0
s = 0

result = 0

for i in range (n+1):
    for j in range (60):
         for p in range (60):
              if '3' in str(i) + str(j) + str(p):
                   result += 1

print(result)