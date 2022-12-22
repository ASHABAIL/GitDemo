#from pywin.Demos.dyndlg import test1


class childimp():

    num3=5
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("i have called")

    def cilcls(self):
        return self.num3 +self.a+self.b


obj = childimp(2,4)
print(obj.cilcls())