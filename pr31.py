def A(a=None ,b=None ,c=None):
    if a != None and b!= None and c != None:
        return a + b + c
    elif a != None and b != None:
        return a + b
    else:
        pass


x, y, z = map(int, input("enter the number=").split(" "))
print(A(x, y))
print(A(x, y, z))