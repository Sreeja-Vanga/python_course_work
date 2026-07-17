Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,3,3,]
sum(l)
7
any([1,0,'',[],(),set(),{},False])
True
all([1,0,'',[],(),set(),{},False])
False
all([1,2,45,5.5,[1,2,3],'sdr')
    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
all([1,2,45,5.5,[1,2,3],'sdr'])
    
True
#Tuples
    
t=(1,2,3,4)
    
t
    
(1, 2, 3, 4)
t=tuple()
    
t
    
()
t=t=(1,2,3,4)
    
t
    
(1, 2, 3, 4)
t
    
(1, 2, 3, 4)
t
    
(1, 2, 3, 4)
t.add(2)
    
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t.add(2)
AttributeError: 'tuple' object has no attribute 'add'
t.append('s')
    
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t.append('s')
AttributeError: 'tuple' object has no attribute 'append'
t=(1,2,3,1,2,3)
    
t
    
(1, 2, 3, 1, 2, 3)
t=('Garret',1,'hannah',2,[1,2,3],{1:2}{1,2,3})
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t=('Garret',1,'hannah',2,[1,2,3])
    
t
    
('Garret', 1, 'hannah', 2, [1, 2, 3])
t=('Garret',1,'hannah',2,[1,2,3],{1:2,2:2},{1,2,3})
    
t
    
('Garret', 1, 'hannah', 2, [1, 2, 3], {1: 2, 2: 2}, {1, 2, 3})
t[4].append(3)
    
t
    
('Garret', 1, 'hannah', 2, [1, 2, 3, 3], {1: 2, 2: 2}, {1, 2, 3})
a=(1,2,3)
    
x,y,z=a#unpacking and packing
    
x
    
1
y
    
2
z
    
3
#immutability
    
t=(1,2,3,4)
    
t
    
(1, 2, 3, 4)
id(t)
    
2392127087664
t=t+(5,6)
    
t
    
(1, 2, 3, 4, 5, 6)
id(t)
    
2392125669280
#tuple operations:
    
#concat:
    
t=('garret','hannah','logan','grace')
    
t
    
('garret', 'hannah', 'logan', 'grace')
id(t)
    
2392125957968
t=t+('dean','allie')
    
t
    
('garret', 'hannah', 'logan', 'grace', 'dean', 'allie')
id(t)
    
2392125669280
#repeat:
    
t*=6
    
t
    
('garret', 'hannah', 'logan', 'grace', 'dean', 'allie', 'garret', 'hannah', 'logan', 'grace', 'dean', 'allie', 'garret', 'hannah', 'logan', 'grace', 'dean', 'allie', 'garret', 'hannah', 'logan', 'grace', 'dean', 'allie', 'garret', 'hannah', 'logan', 'grace', 'dean', 'allie', 'garret', 'hannah', 'logan', 'grace', 'dean', 'allie')
#indexing:
    
t[2]
    
'logan'
t[6]
    
'garret'
t[-1]
    
'allie'
t[-5]
    
'hannah'
#slicing:
    
t[-1:]
    
('allie',)
t[-1::]
    
('allie',)
t=('garret', 'hannah', 'logan', 'grace', 'dean', 'allie')
    
t
    
('garret', 'hannah', 'logan', 'grace', 'dean', 'allie')
t[-1::-1]
    
('allie', 'dean', 'grace', 'logan', 'hannah', 'garret')
t[:7:1]
    
('garret', 'hannah', 'logan', 'grace', 'dean', 'allie')
t[2:6]
    
('logan', 'grace', 'dean', 'allie')
#membership
    
'sreeja'in t
    
False
'sreeja' not in t
    
True
'hannah' in t
    
True
'hannah not in t
    
SyntaxError: unterminated string literal (detected at line 1)
'hannah' not in t
    
False
#tuple methods:
    
t=(1,1,1,2,3,4,4,4,4,5,6)
    
#count:
    
t.count(1)#how many times a value is repeating
    
3
t(3)
    
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    t(3)
TypeError: 'tuple' object is not callable
t.count(3)
    
1
t.count(4)
    
4
#index-to know where the ele is present
    
t.index(1)
    
0
t.lastindex(1)
    
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    t.lastindex(1)
AttributeError: 'tuple' object has no attribute 'lastindex'
#sorted:
    
sorted(t)
    
[1, 1, 1, 2, 3, 4, 4, 4, 4, 5, 6]
#max value:
    
max(t)
    
6
#min value:
    
min(t)
    
1
#sum
    
sum(t)
    
35
#dict
    
d={}
    
type(d)
    
<class 'dict'>
d={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4,'book no.':[1,2,3,4]}
    
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4,'book no.':[1,2,3,4]}
NameError: name 'b1' is not defined
d={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4,'book no.':['1','2','3','4']}
    
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4,'book no.':['1','2','3','4']}
NameError: name 'b1' is not defined
d={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4}
    
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4}
NameError: name 'b1' is not defined
data={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4,'book no':['1','2','3','4']}
    
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    data={'the deal':b1,'the mistake':b2,'the score':b3,'the goal':b4,'book no':['1','2','3','4']}
NameError: name 'b1' is not defined
d={'the deal':1,'the mistake':2,'the score':3,'the goal':4,'book no.':['1','2','3','4']}
    
d
    
{'the deal': 1, 'the mistake': 2, 'the score': 3, 'the goal': 4, 'book no.': ['1', '2', '3', '4']}
#we cannot have list, set, dict as key:
    
d={}
    
d[1]='int'
    
d[1.1]='float'
    
d
    
{1: 'int', 1.1: 'float'}
d[[1,2,3,4]]='list'
    
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: unhashable type: 'list'
#as list is a mutable type we cannot have it as a key
    
d[{1,2,3,4}]='set'
    
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    d[{1,2,3,4}]='set'
TypeError: unhashable type: 'set'
d[{'1':2,'2':2}]='dict'
    
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    d[{'1':2,'2':2}]='dict'
TypeError: unhashable type: 'dict'
d[(1,2,3)]='tuple'
    
d
    
{1: 'int', 1.1: 'float', (1, 2, 3): 'tuple'}
d['srs']='str'
    
d
    
{1: 'int', 1.1: 'float', (1, 2, 3): 'tuple', 'srs': 'str'}
d[(2+3j)]='complex'
    
d
    
{1: 'int', 1.1: 'float', (1, 2, 3): 'tuple', 'srs': 'str', (2+3j): 'complex'}
#opearations:
    
#we cannot concat using '+' operation:
    
d+{'s':1}
    
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    d+{'s':1}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

#accessing using key
    
d['the deal']
    
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    d['the deal']
KeyError: 'the deal'
d[(1,2,3)]
    
'tuple'
d[1.1]
    
'float'
d.get(1)
    
'int'
d[12]
    
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    d[12]
KeyError: 12
d.get(12)
    
#modification of dict:
    
d={'the deal':1,'the mistake':2,'the score':3,'the goal':4,'book no.':['1','2','3','4']}
    
d
    
{'the deal': 1, 'the mistake': 2, 'the score': 3, 'the goal': 4, 'book no.': ['1', '2', '3', '4']}
d['the deal']='book1'
    
d
    
{'the deal': 'book1', 'the mistake': 2, 'the score': 3, 'the goal': 4, 'book no.': ['1', '2', '3', '4']}
id(d)
    
2392126667968
d['book no'].append('5')#to modify the values list
    
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    d['book no'].append('5')#to modify the values list
KeyError: 'book no'
d['book no.'].append('5')#to modify the values list
    
>>> d
...     
{'the deal': 'book1', 'the mistake': 2, 'the score': 3, 'the goal': 4, 'book no.': ['1', '2', '3', '4', '5']}
>>> id(d)
...     
2392126667968
>>> #updating a dict:
...     
>>> d.update({'author':'elle kennedy'})
...     
>>> d
...     
{'the deal': 'book1', 'the mistake': 2, 'the score': 3, 'the goal': 4, 'book no.': ['1', '2', '3', '4', '5'], 'author': 'elle kennedy'}
>>> #deletion:
...     
>>> data.pop('author')
...     
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    data.pop('author')
NameError: name 'data' is not defined
>>> d.pop('author')
...     
'elle kennedy'
>>> d
...     
{'the deal': 'book1', 'the mistake': 2, 'the score': 3, 'the goal': 4, 'book no.': ['1', '2', '3', '4', '5']}
>>> d.popitem('the goal',4)#to del specific item
...     
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    d.popitem('the goal',4)#to del specific item
TypeError: dict.popitem() takes no arguments (2 given)
>>> del d['book no.']
...     
>>> d
...     
{'the deal': 'book1', 'the mistake': 2, 'the score': 3, 'the goal': 4}
>>> d.popitem()
...     
('the goal', 4)
