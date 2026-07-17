Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='sreeja vanga'
for i in s:
    print(s)

    
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
sreeja vanga
for i in s:
    print(i)

    
s
r
e
e
j
a
 
v
a
n
g
a
s='sreeja'
for i in enumerate(s):
    print(i)

    
(0, 's')
(1, 'r')
(2, 'e')
(3, 'e')
(4, 'j')
(5, 'a')
for i in enumerate(s):
    print(i[0],i[1])

    
0 s
1 r
2 e
3 e
4 j
5 a
>>> # to access index and values of a list:
>>> s=['s','r','e','e','j','a']
>>> for i in enumerate(s):
...     print(i[0],i[1],i)
... 
...     
0 s (0, 's')
1 r (1, 'r')
2 e (2, 'e')
3 e (3, 'e')
4 j (4, 'j')
5 a (5, 'a')
>>> 
>>> # to access index and values of a tuple:
>>> t=('s','d','a','s')
>>> for i in enumerate(t):
...     print(i[0],i[1],i)
... 
...     
0 s (0, 's')
1 d (1, 'd')
2 a (2, 'a')
3 s (3, 's')
>>> pin=1234
>>> for i in range(5):
...     entered_pin=int(input('enter the pin:'))
...     if entered_pin==pin:
...         print('login succesfully')
...         break
...     else:
...         print('Invalid')
... else:
...     print('Limit Exceeds')
... 
...     
enter the pin:1234
login succesfully
