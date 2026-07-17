Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a,b,c=[10,20,30]
a
10
b
20
c
30
a,b,c=list(map(int,input("enter the values of a, b, c:").split())
           10
           
SyntaxError: '(' was never closed
a,b,c=list(map(int,input("enter the values of a, b, c:").split()))
           
enter the values of a, b, c:10,20,40
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a,b,c=list(map(int,input("enter the values of a, b, c:").split()))
ValueError: invalid literal for int() with base 10: '10,20,40'
a,b,c=list(map(int,input("enter the values of a, b, c:").split()))
           
enter the values of a, b, c:10 20 30 
a
           
10
b
           
20
c
           
30
email,password=input("enter the email and password:").split()
           
enter the email and password:sreejavanga0@gmail.com sreeja
email
           
'sreejavanga0@gmail.com'
password
           
'sreeja'
#python operators
           
a=10
           
b=20
           
a+b
           
30
a-b
           
-10
a/b
           
0.5
a//b#floor division gives only integer part but not the decimal part
           
0
a*b
           
200
a%b
           
10
a**b
           
100000000000000000000
10%20
           
10
20%10
           
0
10**2
           
100
a==b
           
False
a!=b
           
True
a>b
           
False
a<b
           
True
a<=b
           
True
a>=b
           
False
a=40
           
a+=30
           
a
           
70
a-=a
           
a
           
0
a=70
           
a+=10
           
a
           
80
a-=30
           
a
           
50
a*2=2
           
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a*=2
           
a
           
100
a/=3
           
a
           
33.333333333333336
a//=3
           
a
           
11.0
a%=2
           
a
           
1.0
a**=2
           
a
           
1.0
a=6
           
a%2==0 and a%3==0 and a%6==0
           
True
a=32
           
a%2==0 and a%3==0 and a%6==0
           
False
a%2==0 or a%3==0 or a%6==0
           
True
not a%2==0
           
False
a=13
           
not a%2==0
           
True
#mem op are used for the datatypes  str,list,tuple,set,dict.
           
'p' in 'python'
           
True
's' in 'python'
           
False
'p' not in 'python'
           
False
's' not in 'python'
           
True
l=[1,2,3,4]
           
l
           
[1, 2, 3, 4]
1 in l
           
True
2 inl
           
SyntaxError: invalid syntax
2 in l
           
True
2 not in l
           
False
60 in l
           
False
1 not in l
           
False
set={1,2,3,4}
           
1 in set
           
True
2 not in set
           
False
40 in l
           
False
40 not in set
           
True
40 in set
           
False
d={1:2,2:3,3:4,4:5}
           
6 in d
           
False
1 in d
           
True
6 not in d
           
True
1 not in d
           
False
#identity
           
a=[1,2,3,4]
           
b=[1,2,3,4]
           
a==b
           
True
a is b
           
False
id(a)
           
1965405741632
id(b)
           
1965450123392
c=a
           
c is a
           
True
id(c)
           
1965405741632
id(a)
           
1965405741632
a==c
           
True
a is not b
           
True
a is not c
           
False
e=[1,2]
           
e
           
[1, 2]
id(e)
           
1965450478912
e=a
           
e is a
           
True
id(e)
           
1965405741632
#bitwise
           
10&11
           
10
7&13
           
5
14&11
...            
10
>>> 2^3
...            
1
>>> 12^15
...            
3
>>> 10^20
...            
30
>>> 10>>20
...            
0
>>> 10<<1
...            
20
>>> 10<<2
...            
40
>>> 10<<3
...            
80
>>> 10<<4
...            
160
>>> 10>>1
...            
5
>>> 10>>2
...            
2
>>> 10>>3
...            
1
>>> 10>>4
...            
0
>>> 10>>5
...            
0
