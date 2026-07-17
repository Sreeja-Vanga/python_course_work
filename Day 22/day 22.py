'''class Flipkart:
      products={'laptop':80000,
              'phone':50000,
              'earphones':900,
              'bags':300}

    @classmethod
    def products(cls):
        print(cls.products)

    def register(self,name,phno):
        self.name=name
        self.phno=phno
        print(f'{welcome{name} and phno is{phno}')

    @staticmethod
    def discount():
        print('hey all,10% discount is going on!,check out!!')
sreeja=Flipkart()
sreeja.register('sreeja','9867235417')
sreeja.discount()
sreeja.products()
saniya=Flipkart()
saniya.register('saniya','987654321')
saniya.discount()
saniya.showProducts()




rina=Flipkart()
rina.register('rina','987654321')

tina=Flipkart()
tina.register('tina','987654321')'''

#using constructor:
class Flipkart:

    if __init__(self,name,phno):
        self.username=name
        self.phno=phno
        print(f'welcome{name} and phno is{phno}')
        
      products={'laptop':80000,
              'phone':50000,
              'earphones':900,
              'bags':300}

    @classmethod
    def products(cls):
        print(cls.products)

    def register(self,name,phno):
        self.name=name
        self.phno=phno
        print(f'{welcome{name} and phno is{phno}')

    @staticmethod
    def discount():
        print('hey all,10% discount is going on!,check out!!')
sreeja=Flipkart('sreeja','9686342671')
