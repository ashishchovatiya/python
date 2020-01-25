a=int(input('Enter the number : '))
def facti(a):
    res=1
    while a>=1:
        res*=a
        a=a-1
    return res
print(type(a))
if a==0:
    print('Factorial of 0 is 1')
elif a<0:
    print("FActorial of negative values isn't possible")
else:
    print('Factorial value of ',a,' is : ',facti(a))
