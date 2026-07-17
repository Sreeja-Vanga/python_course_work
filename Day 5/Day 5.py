Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
names='sreeja bhavya yuktha'
names
'sreeja bhavya yuktha'
names.split()
['sreeja', 'bhavya', 'yuktha']
names.split(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    names.split(a)
NameError: name 'a' is not defined
names.split(,2)
SyntaxError: invalid syntax
names.split('',2)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    names.split('',2)
ValueError: empty separator
names.split('a')
['sreej', ' bh', 'vy', ' yukth', '']
names.split(' ',2)
['sreeja', 'bhavya', 'yuktha']
names.split(' ',1)
['sreeja', 'bhavya yuktha']
names.rsplit(' ',1)
['sreeja bhavya', 'yuktha']
names.partition(' ')
('sreeja', ' ', 'bhavya yuktha')
names='sreeja bhavya yuktha'
names.partition(' ')
('sreeja', ' ', 'bhavya yuktha')
names='sreeja,bhavya yuktha'
names.partition(',')
('sreeja', ',', 'bhavya yuktha')
names.rpartition(' ')
('sreeja,bhavya', ' ', 'yuktha')
names.partition(',')
('sreeja', ',', 'bhavya yuktha')
names.rpartition(',')
('sreeja', ',', 'bhavya yuktha')
l=['sreeja' ,'bhavya', 'yuktha']
l
['sreeja', 'bhavya', 'yuktha']
''.join(l)
'sreejabhavyayuktha'
','.join(l)
'sreeja,bhavya,yuktha'
'.'.join()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    '.'.join()
TypeError: str.join() takes exactly one argument (0 given)
'.'.join(l)
'sreeja.bhavya.yuktha'
'-'.join(l)
'sreeja-bhavya-yuktha'
h='     sreeja   vanga'
h.strip()
'sreeja   vanga'
h.lstrip()
'sreeja   vanga'
h.rstrip()
'     sreeja   vanga'
s='hello Hé! Bonjour!'
s
'hello Hé! Bonjour!'
s.encode()
b'hello H\xc3\xa9! Bonjour!'
s.decode()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
'hello Hé! Bonjour!'.decode()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    'hello Hé! Bonjour!'.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
b'hello H\xc3\xa9! Bonjour!'.decode()
'hello Hé! Bonjour!'
#string testing methods:
name='the deal1'
name.startswith('t'))
SyntaxError: unmatched ')'
name.startswith('t')
True
name.startswith('d')
False
name.endswith('1')
True
name.endswith('t')
False
name.isalpha()
False
name.isalnum()
False
n='123'
n.isalnum()
True
n='adef'
n.isalpha()
True
n='agvd123'
n.isalpha()
False
n.isalnum()
True
n.islower()
True
n.isupper()
False
n.isspace()
False
n.istitle()
False
'hannah garret allie dean'.istitle()
False
'hannah garret allie dean'.islower()
True
'hannah garret allie dean'.isupper()
False
'hannah garret allie dean'.isspace()
False
'     '.isspace()
True
'var'.isidentifier()
True
'@var'.isidentifier()
False
'4567'.isdecimal()
True
'jna'.isdecimal()
False
'4567'.isdigit()
True
'4567'.isnumeric()
True
'23II'.isnumeric()
False
's23'isdigit()
SyntaxError: invalid syntax
's23'.isdigit()
False
#list operations:
l=['garret','logan','dean','tucker']
l
['garret', 'logan', 'dean', 'tucker']
l+'hunter'
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    l+'hunter'
TypeError: can only concatenate list (not "str") to list
l.append('hunter')
l
['garret', 'logan', 'dean', 'tucker', 'hunter']
l=['hannah','grace','allie','sabrina']
l+l
['hannah', 'grace', 'allie', 'sabrina', 'hannah', 'grace', 'allie', 'sabrina']
#indexing
l[0]
'hannah'
l[3]
'sabrina'
l[2]
'allie'
#slicing
l+l[0:3]
['hannah', 'grace', 'allie', 'sabrina', 'hannah', 'grace', 'allie']
l2=l+l
l2
['hannah', 'grace', 'allie', 'sabrina', 'hannah', 'grace', 'allie', 'sabrina']
l2[0:3]
['hannah', 'grace', 'allie']
l2[0:4]
['hannah', 'grace', 'allie', 'sabrina']
l2[4:-1]
['hannah', 'grace', 'allie']
l2[4:]
['hannah', 'grace', 'allie', 'sabrina']
l2[::-1]
['sabrina', 'allie', 'grace', 'hannah', 'sabrina', 'allie', 'grace', 'hannah']
l2[1::2]
['grace', 'sabrina', 'grace', 'sabrina']
#membership
'hannah' in l2
True
'jake' in l2
False
'jake'  not in l2
True
'hannah'  not in l2
False
l=[]#empty
l=list()#empty using constructor
l
[]
l=['hannah','grace','allie','brenna']
l
['hannah', 'grace', 'allie', 'brenna']
id(l)
2186489522688
l[3]
'brenna'
l[3]='sabrina'
l
['hannah', 'grace', 'allie', 'sabrina']
id(l)
2186489522688
#to add element
l.append('garret')
l
['hannah', 'grace', 'allie', 'sabrina', 'garret']
l.insert('logan',2)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    l.insert('logan',2)
TypeError: 'str' object cannot be interpreted as an integer
l.insert(2,'logan')
l
['hannah', 'grace', 'logan', 'allie', 'sabrina', 'garret']
l.extend(['tucker','dean'])#add multiple elements at the end
l
['hannah', 'grace', 'logan', 'allie', 'sabrina', 'garret', 'tucker', 'dean']
l.remove('logan')
l
['hannah', 'grace', 'allie', 'sabrina', 'garret', 'tucker', 'dean']
l.pop(4)#to delete using index
'garret'
l
['hannah', 'grace', 'allie', 'sabrina', 'tucker', 'dean']
del l[4]
l
['hannah', 'grace', 'allie', 'sabrina', 'dean']
l.pop()#to delete at last
'dean'\
l
['hannah', 'grace', 'allie', 'sabrina']
#sort
sorted(1)
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    sorted(1)
TypeError: 'int' object is not iterable
l.sorted(l)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    l.sorted(l)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
l.sorted(1)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    l.sorted(1)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
sorted(l)
['allie', 'grace', 'hannah', 'sabrina']
max(l)
'sabrina'
min(l)
'allie'
l.index('allie')
2
l.index(0)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    l.index(0)
ValueError: 0 is not in list
l.index('hannah')
0
l.count()
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> l.count('hannah')
1
>>> l.sort()#to sort the elements permanently
>>> l
['allie', 'grace', 'hannah', 'sabrina']
>>> l.reverse()
>>> l
['sabrina', 'hannah', 'grace', 'allie']
>>> #shallow copy is to maintain a orginal list and modify on duplicate list
>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> m=l
>>> m
[1, 2, 3, 4]
>>> l.append(5)
>>> l
[1, 2, 3, 4, 5]
>>> m
[1, 2, 3, 4, 5]
>>> m.appen(6)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    m.appen(6)
AttributeError: 'list' object has no attribute 'appen'. Did you mean: 'append'?
>>> m.append(6)
>>> m
[1, 2, 3, 4, 5, 6]
>>> l
[1, 2, 3, 4, 5, 6]
>>> #to avoid changes in both lists and maitain the orginal list we use copy()
>>> n=l.copy()
>>> n
[1, 2, 3, 4, 5, 6]
>>> l.append(7)
>>> l
[1, 2, 3, 4, 5, 6, 7]
>>> n
[1, 2, 3, 4, 5, 6]
