#plomorphism:
#method overriding:
'''class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f'Hello {self.name}, Welcome to the Hotstar')
    def login(self):
        print("you can login")
    def search(self):
        print("you can search")
    def categories(self):
        print("you can see divisions")
    def playcontrollers(self):
        print("you can pause,resume and play")
    def livesports(self):
        print("you can watch the sports on live")

    def ads(self):
        print("ads will run")
    def movies(self):
        print("limited movie access")
    def downloads(self):
        print("Can't download")
    def quality(self):
        print("clarity will be limited")


class Premium(Hotstar):
    def ads(self):
        print("ads will not run")
    def movies(self):
        print("unlimited movie access")
    def downloads(self):
        print("Can download and watch offline")
    def quality(self):
        print("clarity will be high")

sreeja=Hotstar('sreeja')
sreeja.login()
sreeja.search()
sreeja.categories()
sreeja.playcontrollers()
sreeja.livesports()
sreeja.movies()
sreeja.downloads()
sreeja.quality()



allie=Premium('allie')
sreeja.login()
sreeja.search()
sreeja.categories()
sreeja.playcontrollers()
sreeja.livesports()
sreeja.movies()
sreeja.downloads()
sreeja.quality()
'''

#operator overriding:
'''class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+other.num
    def __sub__(self,other):
        return self.num-other.num
    def __mul__(self,other):
        return self.num*other.num
    def __eq__(self,other):
        return self.num==other.num
    def __lt__(self,other):
        return self.num<other.num
    def __gt__(self,other):
        return self.num>other.num
a=Number(10)
b=Number(20)
print(a+b)
print(a-b)
print(a*b)
print(a==b)
print(a<b)
print(a>b)'''

#Abstraction:
from abc import ABC, abstractmethod

class Phonepay(ABC):

    def input(self):
        print("You can scan or enter the number")

    def amount(self):
        print("Enter the amount to pay")

    def pin(self):
        print("Enter the pin")

    @abstractmethod
    def verification(self):
        pass

    def paymentstatus(self):
        print("Amount transferred successfully / failed")


class HDFC(Phonepay):

    def verification(self):
        print("Verification completed through HDFC")


class SBI(Phonepay):

    def verification(self):
        print("Verification completed through SBI")


class UNION(Phonepay):

    def verification(self):
        print("Verification completed through UNION")


saniya = HDFC()
saniya.input()
saniya.amount()
saniya.pin()
saniya.verification()
saniya.paymentstatus()


tina = SBI()
tina.input()
tina.amount()
tina.pin()
tina.verification()
tina.paymentstatus()

rina = UNION()
rina.input()
rina.amount()
rina.pin()
rina.verification()
rina.paymentstatus()


