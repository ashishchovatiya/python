class Father:
    fatherName = ''

    def __init__(self, y):
        self.fatherName = y


class Mother:
    motherName = ''

    def __init__(self, z):
        self.motherName = z


class Son(Father, Mother):
    sonName = ''

    def __init__(self, x, y, z):
        self.sonName = x
        self.fatherName = y
        self.motherName = z

    def showName(self):
        print("Son's name is " , self.sonName)
        print("Father's name is " , self.fatherName)
        print("Mother's name is " , self.motherName)


a, b, c = map(str, input("enter the son , father and mother name ").split(" "))
p1 = Son(a, b, c)
p1.showName()