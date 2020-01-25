n=int(input('enter the total value : '))
arr=[]
for i in range(0,n) :
    print('enter arr[',i+1,']' )
    k=int(input())
    arr.append(k)

a=int(input('Enter the number of which you want to know the position :'))
print('Index of ',a,'is :',arr.index(a))
