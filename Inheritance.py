from classwithconstructor import test0


class childimp(test0):
    num2=200

    def __init__(self):
        test0.__init__(self,2,10)

    def getinher(self):
        return self.num2+self.num+self.summation()


obj = childimp()
print(obj.getinher())


