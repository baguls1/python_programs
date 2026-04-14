

class A:
    def __init__(self,name):
       self.name =name
       print(self.name)

    def sum(self,a,b):
        c= a+b
        print(c)

car = A('saurabh')
car.sum(15,14)