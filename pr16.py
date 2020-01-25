n=int(input('enter the total value'))
arr=[]
for i in range(0,n) :
    print('enter arr[',i+1,']' )
    k=int(input())
    arr.append(k)

print('array before sorting',arr)
for i in range(0,n):
    for j in range(i,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print('array after sorting',arr)