class bank:
    money = 0

    def __init__(self, x):
        self.money = x

    def deposit(self, x):
        self.money += x

    def withdrawal(self, y):
        if self.money >= y:
            self.money -= y
        else:
            print("your account balance is low")

    def account(self):
        print("Your account balance is ", self.money)


p1 = bank(0)
p = ''
while(True):
    p = int(input('enter the number 1:check balance 2:deposit 3:withdrawal 4:exit  =>'))
    if p == 1:
        p1.account()
    elif p == 2:
        w = int(input('enter deposit money='))
        p1.deposit(w)
    elif p == 3:
        w = int(input('enter withdrawal money='))
        p1.withdrawal(w)
    elif p == 4:
        p1.account()
        break
    else:
        print('Enter proper choice')
else:
    print('Enter right choice')