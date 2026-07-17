Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Token:
    
SyntaxError: invalid syntax
my_var=10
my_var
10
type(my_var)
<class 'int'>
a=10
b='sreeja'
c=3.14
a
10
b
'sreeja'
c
3.14
type(a)
<class 'int'>
type(b)
<class 'str'>
type(c)
<class 'float'>
#datatypes
#numerical:
#int,float,complex:
a=10
type(a)
<class 'int'>
b=3.14
type(b)
<class 'float'>
c=2+2i
SyntaxError: invalid decimal literal
c=2+i
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    c=2+i
NameError: name 'i' is not defined. Did you mean: 'id'?
c=2+2j
type(c)
<class 'complex'>
#sequencial:str(immutable),list(mutable),tuple(immutable)
a='sreeja'
b=['apple',1,'hi']
c=('hi','hello',8)
type(a)
<class 'str'>
type(b)
<class 'list'>
type(c)
<class 'tuple'>
>>> #mapping:set(no duplicate values),dict(key value pairs):
>>> a={'hi','g'}
>>> a
{'hi', 'g'}
>>> type(a)
<class 'set'>
>>> a=set{}
SyntaxError: invalid syntax
>>> a=set()
>>> a
set()
>>> b={'name':sreeja,'age':21}
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    b={'name':sreeja,'age':21}
NameError: name 'sreeja' is not defined
>>> b={'name':'sreeja','age':21}
>>> b
{'name': 'sreeja', 'age': 21}
>>> type(b)
<class 'dict'>
>>> #None:null values
>>> a=None
>>> type(a)
<class 'NoneType'>
>>> b=bool
>>> type(b)
<class 'type'>
>>> 
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keywird.kwlist))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(len(keywird.kwlist))
NameError: name 'keywird' is not defined. Did you mean: 'keyword'?
>>> print(len(keyword.kwlist))
35
