class Animal:
    def __init__(self, x):
        self.AnimalName = x

    def show(self):
        print("animal type name ", self.AnimalName)


class Dog(Animal):
    def __init__(self, y):
        super().__init__(y)



s=input("enter the Dog type=")
p1 = Dog(s)
p1.show()