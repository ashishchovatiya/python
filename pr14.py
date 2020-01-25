n=int(input('how many numbers you want : '));
a=0
b=1
if n ==1:
    print(0)
elif n==0 or n<0:
    print('please enter right number')
else :
    print(a);
    print(b);
    for i in range(2,n):
       c=a+b
       a=b
       b=c
       print(c)

