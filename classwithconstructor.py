class test0:
    num=100 #class variable


    def __init__(self,a,b):
        self.a = a #instance variables
        self.b = b
        print("i am called automatically when object is cretaed")


    def test1(self):
        print("i am a method")

    def summation(self):
        return self.a+self.b+self.num

obj = test0(2,3)
obj.test1()
print(obj.summation())



class test4:
    num=10

    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("yes")

    def test5(self):
        print("yes")

    def multiplication(self):
        return self.a*self.b*self.num

obj = test4(4,5)
obj.test5()
print(obj.multiplication())