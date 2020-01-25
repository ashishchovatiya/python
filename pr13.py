a=int(input('Enter a : '))

def prime(a):
    if a>1:
        for i in range(2,a//2):
            if a%i==0:
                print(a,' is not prime')
                break
        else:
            print(a,'is prime')
    elif a==1:
        print('1 is unit number')
    else:
        print('Please Enter positive number which is greater than 1 ')

prime(a)