n = 5
for i in range(n*2-1, 0, -1):
    print("%s%s" % (" "*abs(i-n), "*"*(n-abs(i-n))))