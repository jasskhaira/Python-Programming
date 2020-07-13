f = open('log.txt','r')

x=f.__next__()
y=f.__next__()
print(x,y)



for line in f:
    print(line.upper(),end=' ')