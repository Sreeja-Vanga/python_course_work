#functions:
'''def greet(name):
    print(f'hello {name}')
name=input('enter your name:')
greet(name)'''

#functions with positional arguments:
'''def display(name,email,ph):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'ph:{ph}')
display('sreeja','sreeja@gmail.com','9876523451')
display('sreeja@gmail.com','sreeja','9876523451')
display('sreeja','987654321','sreeja@gmail.com')'''

#functions with keyword arguments:
'''def display(name,email,ph):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'ph:{ph}')
display(name='sreeja',email='sreeja@gmail.com',ph='9876523451')
display(email='sreeja@gmail.com',name='sreeja',ph='9876523451')
display(name='sreeja',ph='987654321',email='sreeja@gmail.com')'''


#functions with default arguments:(default parameters should be at last)
'''def display(name,email,ph=None,cgpa=None):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'ph:{ph}')
    print(f'cgpa:{cgpa}')
display('sreeja','sreeja@gmail.com','9876523451')
display('sreeja@gmail.com','sreeja')
display('sreeja','987654321','sreeja@gmail.com')'''

#functions with variable length of parameters(helps in knowing the count of parameters)(gives output in the form of tuple):
'''def display(*names):
    print(names)

display('sreeja')
display('vanga','bhavya')
display('sree','yuktha','sri')'''

#functions with variable length of parameters(helps in knowing the count of parameters)(gives output in the form of dict(key, val pairs):
'''def display(**names):
    print(names)

display(n1='sreeja')
display(n2='vanga',n3='bhavya')
display(n4='sree',n5='yuktha',n6='sri')'''

#prime number function:
def isprime(n):
    for i in range(2,n//2):
       if n%i==0:
           return False
    return True
n=int(input('enter number:'))
print('Prime Number' if isprime(n) else 'Not a Prime Number')





