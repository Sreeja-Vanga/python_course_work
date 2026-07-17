Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(0)
False
b=3.14
type(b)
<class 'float'>
int(b)
3
bool(b)
True
str(b)
'3.14'
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
complex(b)
(3.14+0j)
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
c=2+3j
type(c)
<class 'complex'>
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
set(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
bool(c)
True
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
s="sreeja"
type(s)
<class 'str'>
int(s)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'sreeja'
float(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'sreeja'
complex(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['s', 'r', 'e', 'e', 'j', 'a']
tuple(s)
('s', 'r', 'e', 'e', 'j', 'a')
set(s)
{'j', 's', 'a', 'r', 'e'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
s='10'
type(s)
<class 'str'>
int(s)
10
float(s)
10.0
complex(s)
(10+0j)
l=[1,2,3]
type(l)
<class 'list'>
int(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3]'
complex(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
dict(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
tuple(l)
(1, 2, 3)
set(l)
{1, 2, 3}
bool(l)
True
t=(1,2,3)
type(t)
<class 'tuple'>
int(t)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
flot(t)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    flot(t)
NameError: name 'flot' is not defined. Did you mean: 'float'?
float(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(t)
'(1, 2, 3)'
list(t)
[1, 2, 3]
set(t)
{1, 2, 3}
dict(t)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s=set{1,2,4}
SyntaxError: invalid syntax
s={1,3,6}
type(s)
<class 'set'>
int(s)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
list(s)
[1, 3, 6]
tuple(s)
(1, 3, 6)
dict(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
str(s)
'{1, 3, 6}'
d={'1':2,'2':2}
typr(d)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    typr(d)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(d)
<class 'dict'>
int(d)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)]
SyntaxError: unmatched ']'
complex(d)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
list(d)
['1', '2']
set(d)
{'2', '1'}
list(d)
['1', '2']
tuple(d)
('1', '2')
str(d)
"{'1': 2, '2': 2}"
bool(d)
True
b=True
type(b)
<class 'bool'>
int(b)
1
float(b)
1.0
complex(b)
(1+0j)
str(b)
'True'
list(b)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
d
ict(b)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    ict(b)
NameError: name 'ict' is not defined. Did you mean: 'oct'?
dict(b)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
a=10
b=20.3
c='sreeja'
print(a,b,c)
10 20.3 sreeja
print('a='a,'b='b,'c='c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a=',a,'b=',b,'c=',c)
a= 10 b= 20.3 c= sreeja
print('a=',a,'b=',b,'c=',c,sep='')
a=10b=20.3c=sreeja
print('a=',a,'b=',b,'c=',c,sep=' ')
a= 10 b= 20.3 c= sreeja
print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
20.3
c=
sreeja
print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	20.3	c=	sreeja
print('a=',a,'b=',b,'c=',c,sep='@@@')
a=@@@10@@@b=@@@20.3@@@c=@@@sreeja
print('a=',a,'b=',b,'c=',c,sep='@')
a=@10@b=@20.3@c=@sreeja
print('a=',a,'b=',b,'c=',c,end='@@')
a= 10 b= 20.3 c= sreeja@@
print('a=',a,'b=',b,'c=',c,end='\n\n')
a= 10 b= 20.3 c= sreeja

print(f'a:{a},b:{b},c:{c}')
a:10,b:20.3,c:sreeja
print(f'a:{a} b:{b} c:{c}')
a:10 b:20.3 c:sreeja
print('a=%d b=%f c=%s')
a=%d b=%f c=%s
print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=20.300000 c=sreeja
print('a={} b={} c={}'.format(a,b,c))#formatting method
a=10 b=20.3 c=sreeja
print('a={1} b={2} c={3}'.format(a,b,c))#formatting with index
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    print('a={1} b={2} c={3}'.format(a,b,c))#formatting with index
IndexError: Replacement index 3 out of range for positional args tuple
print('a={0} b={1} c={2}'.format(a,b,c))
a=10 b=20.3 c=sreeja
name=input()
sreeja
name
'sreeja'
n=input('enter the name:')
enter the name:sreeja vanga
n
'sreeja vanga'
type(n)
<class 'str'>
age=input('enter the age:')
enter the age:21
type(age)
<class 'str'>
a=int(input('enter the age:'))
enter the age:21
type(a)
<class 'int'>
'sreeja vanga'.split()
['sreeja', 'vanga']
name=input("enter the names:").split()
enter the names:sreeja vanga
name
['sreeja', 'vanga']
type(name)
<class 'list'>
age=input('enter the ages:').split()
enter the ages:21,20,21
age
['21,20,21']
>>> type(age)
<class 'list'>
>>> list(map(int,input('enter the ages:').split()))
enter the ages:21 20 21
[21, 20, 21]
>>> type(list(map(int,input('enter the ages:').split())))
enter the ages:21
<class 'list'>
>>> age=list(map(int,input('enter the ages:').split()))
enter the ages:21 22 20 21
>>> age
[21, 22, 20, 21]
>>> type(age)
<class 'list'>
>>> list(map(float,input('enter the ages:').split()))
enter the ages:21 22 21 
[21.0, 22.0, 21.0]
>>> names=tuple(input('enter the names:')).split()
enter the names:sreeja vanag
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    names=tuple(input('enter the names:')).split()
AttributeError: 'tuple' object has no attribute 'split'
>>> names=tuple(input('enter the names:').split())
enter the names:sreeja vanga
>>> tuple(map(float,input('enter the ages:').split()))
enter the ages:21 22 23
(21.0, 22.0, 23.0)
>>> age=set(input.split())
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    age=set(input.split())
AttributeError: 'builtin_function_or_method' object has no attribute 'split'
>>> age=set(input().split())
sds ssd sss
>>> age
{'ssd', 'sds', 'sss'}
>>> a=eval(input("enter the dict:"))
enter the dict:{1:2,2:3,3:4}
>>> a
{1: 2, 2: 3, 3: 4}
