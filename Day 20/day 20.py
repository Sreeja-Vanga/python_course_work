#built-in modules:

#sys module:
'''import sys

print(sys.argv)
print()
print(sys.path)
print()
print(sys.version)
sys.exit()
print('End')'''

#platform module:
'''import platform
print(platform.system())
print()
print(platform.release())
print()
print(platform.processor())'''

#math module:
import math
'''print(math.e)
print(math.sqrt(16))
print(math.pow(2,3))
print(math.ceil(-12.0006))
print(math.ceil(-12.3))
print(math.ceil(-12.999))
print(math.floor(-12.0006))
print(math.floor(-12.0006))
print(math.floor(-12.0006))

print(math.fabs(-123))#gives float absolute value
print(math.factorial(6))
print(math.gcd(44,12))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(190))
print(math.radians(190))'''

#random module:
'''import random
random.seed(12)
print(random.random())#to get random values in the range of (0,1)
print(random.randint(1,3))#to get random values in the given specific range of integers
print(random.uniform(1,3))# to get float values in the given range
l=['sreeja','vanga','sreekar','sujatha','srinivas']
print(random.choice(l))#to get random values from the list
print(random.choices(l,k=2))#to get multiple random values from a list
print(random.shuffle(l))#to shuffle the elements in the list
print('Before:',l)
print('After:',l)'''

#collections module:
'''import collections
s='sreeja vanga'
l=[1,2,3,5,6,1,7,4,8,9,2,1,5,3,5,3,2]
print(collections.Counter(s))#it gives how many a value is repeating
print(collections.Counter(l))'''

'''d=collections.defaultdict(int)#instead of declaring an empty string,we use defaultdict to initialize with default values
for i in s:
    d[i]+=1
print(d)'''

'''for int-0
for str=' '
for float=0.0
 '''

'''d=collections.deque([])
d.append(10)
d.append(20)
d.popleft()
d.append(30)
d.popleft()
d.append(40)
d.append(50)
d.append(60)
d.popleft()
print(d)'''

'''d=collections.deque([])
d.appendleft(10)
d.appendleft(20)
d.pop()
d.appendleft(30)
d.pop()
d.appendleft(40)
d.appendleft(50)
d.appendleft(60)
d.pop()
print(d)'''


#itertools module:
from itertools import combinations,permutations
print(list(combinations('ABCD',3)))
print(list(permutations('ABCD',3)))

 
