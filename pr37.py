import math
print("enter the two prime number P & Q")
p,q=(input().split(" "))
p,q=int(p),int(q)
m=int(input("enter the Msg ="))
N=p*q
Qn=(p-1)*(q-1)
for i in range(2,Qn):
    if(math.gcd(i,Qn)==1):
        e=i
        break
    else:
        pass
for i in range(1,100000):
    d=int((1+i*Qn)/e)
    if(d<Qn and d>0 and (d*e)%Qn==1):
        break
    else:
        pass
print('Value of N is:',N)
print('Value of Fie(N) is:',Qn)
print('Value of e is:',e)
print('Value of d is:',d)
c=(m**e)%N
print("encryption is ",c)
M=(c**d)%N
print("decryption is",M)
