class operatoroverload:
    #number = 0

    def __init__(self, x):
        self.x = x

    def __gt__(self, other):
        if self.x > other.x:
            return 1
        else:
            return 0


a, b = map(int, input("enter the two number for object p1 and p2 = ").split(" "))
num1 = operatoroverload(a)
num2 = operatoroverload(b)
if num1 > num2:
    print('num1 is gt',a)
else:
    print('num2 is gt',b)