#Inheritance:
#single inheritance:
'''class A:
    def printa(self):
        print("Parent Class-A")
class B(A):
    def printb(self):
        print("Child Class-B")
b=B()
b.printb()
b.printa()'''

#heirachial inheritance:
'''class A:
    def printa(self):
        print("Parent Class-A")
class B(A):
    def printb(self):
        print("Child Class-B")

class C(A):
    def printc(self):
        print("Child Class-C")
class D(A):
    def printd(self):
        print("Child Class-D")


b=B()
b.printb()
b.printa()
c=C()
c.printc()
c.printa()
d=D()
d.printd()
d.printa()'''


#multiple inheritance:
'''class A:
    def printa(self):
        print("Parent Class-A")
class B:
    def printb(self):
        print("Child Class-B")

class C:
    def printc(self):
        print("Child Class-C")
class D(A,B,C):
    def printd(self):
        print("Child Class-D")

d=D()
d.printd()
d.printa()
d.printb()
d.printc()'''


#multilevel inheritance:
'''class A:
    def printa(self):
        print("Parent Class-A")
class B(A):
    def printb(self):
        print("Child Class-B")

class C(B):
    def printc(self):
        print("Child Class-C")
class D(C):
    def printd(self):
        print("Child Class-D")

d=D()
d.printd()
d.printc()
d.printb()
d.printa()'''

#hybrid inheritance:
'''class A:
    def printa(self):
        print("Parent Class-A")
class B(A):
    def printb(self):
        print("Child Class-B")

class C(B,A):
    def printc(self):
        print("Child Class-C")
class D(C):
    def printd(self):
        print("Child Class-D")

d=D()
d.printd()
d.printc()
d.printb()
d.printa()'''

#examples:
#single inheritance:
'''class Instagramv1:
    def post(self):
        print("you can upload posts")
    def reel(self):
        print("you can upload reels")
class Instagramv2(Instagramv1):
    def story(self):
        print("you can upload story")
    def live(self):
        print("you can go live")

sreeja=Instagramv1()
sreeja.post()
sreeja.reel()

garret=Instagramv2()
garret.post()
garret.reel()
garret.story()
garret.live()'''

#multiple,multilevel,hybrid:
'''class Instagramv1:
    def post(self):
        print("you can upload posts")
    def reel(self):
        print("you can upload reels")
class Instagramv2(Instagramv1):
    def story(self):
        print("you can upload story")
    def live(self):
        print("you can go live")
class Whatsapp:
    def wpstatus(self):
        print("You can upload whatsapp status")
class Facebook:
    def fbstory(self):
        print("you can upload facebook story")
class Instagramv3(Instagramv2,Whatsapp,Facebook):
    def crossplatforms(self):
        print("You can upload same on whatsapp status")
        print("you can upload same on facebook story") 
        

dean=Instagramv3()
dean.post()
dean.reel()

dean.post()
dean.reel()
dean.story()
dean.live()


dean.wpstatus()
dean.fbstory()
dean.crossplatforms()'''


'''class Instagramv1:
    def post(self):
        print("you can upload posts")
    def reel(self):
        print("you can upload reels")
class Instagramv2(Instagramv1):
    def story(self):
        print("you can upload story")
    def live(self):
        print("you can go live")
class Whatsapp:
    def wpstatus(self):
        print("You can upload whatsapp status")
class Facebook:
    def fbstory(self):
        print("you can upload facebook story")
class Instagramv3:
    def note(self):
        print("you can update the note")
class Instagramv4:
    def instants(self):
        print("you can upload instant snap")
class Instagramv5(Instagramv2,Instagramv3,Instagramv4,Whatsapp,Facebook):
    def crossplatforms(self):
        print("You can upload same on whatsapp status")
        print("you can upload same on facebook story") 


logan=Instagramv5()
logan.post()
logan.reel()

logan.post()
logan.reel()
logan.story()
logan.live()


logan.wpstatus()
logan.fbstory()
logan.note()
logan.instants()
logan.crossplatforms()'''

#super method:when parent and child class have same method , to acces the methods from both, we use super()
'''class A:
    def print(self):
        print("Class-A")
class B(A):
    def print(self):
        super().print()
        print("Class-B")
b=B()
b.print()'''

#use class name in multiple inheritance:
class A:
    def print(self):
        print("Class-A")
class B:
    def print(self):
        print("Class-B")
class C(A,B):
    def print(self):
        A.print(self)
        B.print(self)
        print("Class-C")
c=C()
c.print()




