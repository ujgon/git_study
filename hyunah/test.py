import time

array = [i for i in range(100000000)]

start = time.time()
array[::-1]
end = time.time()

print("[::-1] 소요 시간 :", end-start)

start = time.time()
reversed(array)
end = time.time()

print("reversed() 소요 시간 :", end-start)
