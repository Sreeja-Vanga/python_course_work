#encapsulation:
class Instagram:
    def __init__(self,username,password,cf):
        self.username=username
        self.__password=password# ('__' for private)
        self._cf=cf#('_' for protected)
    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password=new_password
    @property
    def accesscf(self):
        return self._cf
    @accesscf.setter
    def accesscf(self,new_frnd):
        self._cf.append(new_frnd)
sreeja=Instagram('sreeja','sreeja@2',['sreeja','bhavya'])
print("before username:",sreeja.username)
sreeja.username='vanga'
print("after username:",sreeja.username)

print("before password:",sreeja.getpassword())
sreeja.setpassword('sreeja123')
print("after password:",sreeja.getpassword())

print("before cf:",sreeja.accesscf)
sreeja.accesscf='yuktha'
print("After cf:",sreeja.accesscf)

      
