a, b = map(int, input("enter the two number A & B for A/B  = ").split(' '))
try:
    c = a / b
except ZeroDivisionError:
    print('Division by Zero Exception')
else:
    print('A/B = ', c)