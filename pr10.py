a,b,c=map(int,input('enter a, b & c :').split(' '))
if (a >= b) and (a >= c):
    print('a is maximum',a)

elif (b >= a) and (b >= c):
    print('b is maximum', b)
else:
    print('c is maximum', c)

