Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={1:1,2:4,3:9,4:16,5:25}
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#to get the keys of a dict
d.keys()
dict_keys([1, 2, 3, 4, 5])
#to get items
d.items()
dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
#len
len(d)
5
#to get only values
d.values()
dict_values([1, 4, 9, 16, 25])
#to get max and min values
max(d)
5
min(d)
1
#max and min only with keys
#to access by get() method
d.get(5,0)
25
d.get(6,0)
0
sorted(d)
[1, 2, 3, 4, 5]
d.setdefault(6,36)
36
d.setdefault(5,0)
25
#set:
s=set()#declaration
s=(1,3,4,32,45,76,54,32,45,12,22,2,22,2,2,235}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
s={1,3,4,32,45,76,54,32,45,12,22,2,22,2,2,235}
s
{32, 1, 2, 3, 4, 235, 12, 45, 76, 22, 54}
s=set()
s.add(1)#set can have int
s
{1}
s.add(1.2)
s
{1, 1.2}
s.add('sd')
s
{1, 'sd', 1.2}
s.add(2+1j)
s
{1, (2+1j), 'sd', 1.2}
s.list([1,2,3])#set cannot have list as it is mutable
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.list([1,2,3])#set cannot have list as it is mutable
AttributeError: 'set' object has no attribute 'list'
s.set({1,2,3,3})#set cannot have set as it is mutable
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.set({1,2,3,3})#set cannot have set as it is mutable
AttributeError: 'set' object has no attribute 'set'
s.add((1,2,3,3))#set can have tuple
s
{1, 1.2, (2+1j), 'sd', (1, 2, 3, 3)}
s.add({1:1,2:2})#set cannot have dict
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.add({1:1,2:2})#set cannot have dict
TypeError: unhashable type: 'dict'
s.add(0)
s
{0, 1, 1.2, (2+1j), 'sd', (1, 2, 3, 3)}
s.add(True)
s
{0, 1, 1.2, (2+1j), 'sd', (1, 2, 3, 3)}
s.add(1)
s
{0, 1, 1.2, (2+1j), 'sd', (1, 2, 3, 3)}
s.add(False)
s
{0, 1, 1.2, (2+1j), 'sd', (1, 2, 3, 3)}
#we have no operations like repetition, concat,slicing, indexing,accessing in set except membership
{1,2,3}+{4,5,6}
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    {1,2,3}+{4,5,6}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1,2,3}*2
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    {1,2,3}*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'



#membership is possible
0 in s
True
23 in s
False
2 not in s
True
1 not in s
False


#set operations:

#union
a={1,2,3}
a
{1, 2, 3}
b
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    b
NameError: name 'b' is not defined
b={4,5,1,2}
b
{1, 2, 4, 5}
a|b
{1, 2, 3, 4, 5}
#intersection
a&b
{1, 2}
#difference
a-b
{3}
#symm diff
a^b
{3, 4, 5}
#subset
a<b
False
a<{1,2,3,4}
True
#superset
a>b
False
{1,2,3,4}>a
True
#disjoint
a.isdisjoint(b)
False
{1,2,3}.isdisjoint({4,5,6})
True


a.isunion(b)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.isunion(b)
AttributeError: 'set' object has no attribute 'isunion'. Did you mean: 'union'?
a.issubset(b)
False
a.issuperset(B)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.issuperset(B)
NameError: name 'B' is not defined. Did you mean: 'b'?
>>> 
>>> 
>>> 
>>> #methods:
>>> sum(a)
6
>>> max(a)
3
>>> min(a)
1
>>> sorted(a)
[1, 2, 3]
>>> len(a)
3
>>> a.add(4)
>>> a
{1, 2, 3, 4}
>>> a.update({5,6,7})
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.pop()
1
>>> #pop randomly deletes
>>> a.popitem(7)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.popitem(7)
AttributeError: 'set' object has no attribute 'popitem'
>>> a.clear()
>>> a
set()
>>> #to delete a particular value
>>> b.remove(2)
>>> b
{1, 4, 5}
>>> 
>>> #to remove an elements which is not present in the set throws an error
>>> b.remove(100)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    b.remove(100)
KeyError: 100

 
#to remove the ele which is not present in the set can be done by discard
b.discard(12)
b
{1, 4, 5}


# when we use union or intersection the set values of a and b are not changed
a={1,2,3}
b={1,4,5,3}
a
{1, 2, 3}
b
{1, 3, 4, 5}
a.union(b)
{1, 2, 3, 4, 5}
a
{1, 2, 3}
b
{1, 3, 4, 5}
a.intersection(b)
{1, 3}
a
{1, 2, 3}
b
{1, 3, 4, 5}

#but when we use intersection_update the result is going to save in a
a.intersection_update(b)
a
{1, 3}
b
{1, 3, 4, 5}
#shallow copy to copy the orginal set ignores any modifications
c=a
c
{1, 3}
a
{1, 3}
c.add(4)
c
{1, 3, 4}
a
{1, 3, 4}
b.copy()
{1, 3, 4, 5}
d=b.copy()
b
{1, 3, 4, 5}
d
{1, 3, 4, 5}
b.add(10)
b
{1, 3, 4, 5, 10}
d
{1, 3, 4, 5}
