Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings
s='sreeja'
type(s)
<class 'str'>
s=s+'vanga'
s
'sreejavanga'
id(s)
2261566801456
fname='sreeja'
lname='vanga'
fname+lname
'sreejavanga'
fname*10
'sreejasreejasreejasreejasreejasreejasreejasreejasreejasreeja'
'#'*10
'##########'
'sreejavanga'
'sreejavanga'
names='sreeja vanga '
names[0]
's'
names[1]
'r'
names[2]
'e'
names[3]
'e'
names[4]
'j'
names[-1]
' '
names[-2]
'a'
names[-3]
'g'
names[-4]
'n'
#slicing:var[start:stop+1:step]
#default-var[0:len(var):1]
names[0:7:1]
'sreeja '
names[8:12:1]
'anga'
names[8:11:1]
'ang'
names[7:12:1]
'vanga'
#negative slicing:
names[-7:]
' vanga '
names[-7:-2:1]
' vang'
#reverse of a string:
names[::-1]
' agnav ajeers'
names[-1:-8:-1]
' agnav '
names[::2]
'sej ag '
#membership:to check whether a particular name in the str
'sreeja' in names
True
'vanga' in names
True
'bahg'not in names
True
'khhsh' not in names
True
#methods:
len(names)
13
sorted(names)#gives in sorted order based on the askci value
[' ', ' ', 'a', 'a', 'a', 'e', 'e', 'g', 'j', 'n', 'r', 's', 'v']
ord('a')
97
ord('b'_
    
SyntaxError: '(' was never closed
ord('v')
    
118
chr(50)
    
'2'
chr(100)
    
'd'
max(names)
    
'v'
min(names)
    
' '
ord(a')
    
SyntaxError: unterminated string literal (detected at line 1)
ord('a')
    
97
ord('g')
    
103
names.upper()
    
'SREEJA VANGA '
names.lower()
    
'sreeja vanga '
names.capitalize()
    
'Sreeja vanga '
names.title()
    
'Sreeja Vanga '
names.swapcase()
    
'SREEJA VANGA '
names.swapcase()
    
'SREEJA VANGA '
names.casefold()
    
'sreeja vanga '
names='Sreeja Vanga '
    
names.swapcase()
    
'sREEJA vANGA '
names.center(10,'*')
    
'Sreeja Vanga '
names.center(12,'*')
    
'Sreeja Vanga '
names.center(50,'*')
    
'******************Sreeja Vanga *******************'
names.center(40,'*')
    
'*************Sreeja Vanga **************'
names.center(30,'*')
    
'********Sreeja Vanga *********'
names.ljust(30,'-')
    
'Sreeja Vanga -----------------'
names.rjust(30,'-')
    
'-----------------Sreeja Vanga '
'5'.zfill(5)
    
'00005'
'522'.zfill(5)
    
'00522'
'513356'.zfill(5)
    
'513356'
'5123'.zfill(5)
    
'05123'
names.find('s')
    
-1
names='Sreeja Vanga'
    
names.find('S')
    
0
names.find('j')
    
4
names.find('b')
    
-1
names.rfind('a')#it gives values from right side(it gives a from sreeja)
    
11
names.rfind('n')
    
9
names.index('a')
    
5
names.rindex('a')
    
11
names.index('b')
...     
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    names.index('b')
ValueError: substring not found
>>> names.rindex('b')
...     
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    names.rindex('b')
ValueError: substring not found
>>> names.count(a')
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> names.count('a')
...             
3
>>> names.count('s')
...             
0
>>> names.coun('j')
...             
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    names.coun('j')
AttributeError: 'str' object has no attribute 'coun'. Did you mean: 'count'?
>>> names.count('j')
...             
1
>>> names.replace('ee','i')
...             
'Srija Vanga'
>>> names.replace('i','ee')
...             
'Sreeja Vanga'
>>> names.replace('aeiou','12345')#to replace vowels to nums but we cannot as it a whole str
...             
'Sreeja Vanga'
>>> names.maketrans('aeiou','12345')# it translates with each and every char
...             
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
